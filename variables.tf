variable "prefix" {
  description = "The prefix used for all resources in this environment"
}

variable "flask_env" {
  description = "Flask app environment variable"
}

variable "flask_secret_key" {
  description = "Flask secret key"
  sensitive = true
}
