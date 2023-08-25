terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = ">= 3.8"
    }
  }

  backend "azurerm" {
    resource_group_name  = "Cohort25_JacWoo_ProjectExercise"
    storage_account_name = "jacwooterraformstate"
    container_name       = "state"
    key                  = "terraform.tfstate"
  }
}

provider "azurerm" {
  features {}
}

data "azurerm_resource_group" "main" {
  name     = "Cohort25_JacWoo_ProjectExercise"
}

resource "azurerm_service_plan" "main" {
  name                = "${var.prefix}-terraformed-asp"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  os_type             = "Linux"
  sku_name            = "B1"
}

resource "azurerm_linux_web_app" "main" {
  name                = "${var.prefix}-terraformed-jsw-todo-app"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  service_plan_id     = azurerm_service_plan.main.id

  site_config {
    application_stack {
      docker_image_name     = "jackiew104/todo-app:prod"
    }
  }

  app_settings = {
    "DOCKER_REGISTRY_SERVER_URL" = "https://index.docker.io"
    "FLASK_APP" = "todo_app/app"
    "FLASK_ENV" = var.flask_env
    "SECRET_KEY" = var.flask_secret_key
    "COSMOS_CONNECTION_STRING" = azurerm_cosmosdb_account.main.connection_strings[0]
    "COSMOS_DB_NAME" = azurerm_cosmosdb_mongo_database.main.name
    "DEFAULT_LOG_LEVEL" = var.log_level
  }
}

resource "azurerm_cosmosdb_account" "main" {
  name                = "${var.prefix}-terraformed-jsw-todo-app-db"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  offer_type          = "Standard"
  kind                = "MongoDB"
  
  # lifecycle { 
  #   prevent_destroy = true 
  # }

  capabilities {
    name = "EnableServerless"
  }

  consistency_policy {
    consistency_level = "Strong"
  }

  geo_location {
    location = "uksouth"
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
  name                = "${var.prefix}-terraformed-db"
  resource_group_name = data.azurerm_resource_group.main.name
  account_name        = azurerm_cosmosdb_account.main.name
}
