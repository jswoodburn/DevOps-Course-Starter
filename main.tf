terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = ">= 3.8"
    }
  }
}

provider "azurerm" {
  features {}
}

data "azurerm_resource_group" "main" {
  name     = "Cohort25_JacWoo_ProjectExercise"
}

resource "azurerm_service_plan" "main" {
  name                = "terraformed-asp"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  os_type             = "Linux"
  sku_name            = "B1"
}

resource "azurerm_linux_web_app" "main" {
  name                = "terraformed-jsw-todo-app"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  service_plan_id     = azurerm_service_plan.main.id

  site_config {
    application_stack {
      docker_image     = "jackiew104/todo-app"
      docker_image_tag = "prod"
    }
  }

  app_settings = {
    "DOCKER_REGISTRY_SERVER_URL" = "https://index.docker.io"
    "FLASK_APP" = "todo_app/app"
    "FLASK_ENV" = "development"
    "SECRET_KEY" = "SECRET_KEY"
    "COSMOS_CONNECTION_STRING" = azurerm_cosmosdb_account.main.connection_strings[0]
    "COSMOS_DB_NAME" = azurerm_cosmosdb_mongo_database.main.name
  }
}

resource "azurerm_cosmosdb_account" "main" {
  name                = "terraformed-jsw-todo-app"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  offer_type          = "Standard"
  kind                = "MongoDB"
  
  lifecycle { 
    prevent_destroy = true 
  }

  capabilities {
    name = "EnableServerless"
  }

# TODO exercise-12: not sure if this is right
  consistency_policy {
    consistency_level = "Strong"
  }

  geo_location {
    location          = "uksouth"
    failover_priority = 0
  }

  capabilities {
    name = "MongoDBv3.4"
  }

  capabilities {
    name = "EnableMongo"
  }
}

resource "azurerm_cosmosdb_mongo_database" "main" {
  name                = "terraformed-dev-db"  # TODO exercise-12: make this rely on env variables
  resource_group_name = data.azurerm_resource_group.main.name
  account_name        = azurerm_cosmosdb_account.main.name
}