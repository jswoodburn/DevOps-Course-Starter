variable "prefix" {
  description = "The prefix used for all resources in this environment"
}

variable "flask-env" {
  description = "Flask app environment variable"
}

variable "flask-secret-key" {
  description = "Flask secret key"
  sensitive = true
}