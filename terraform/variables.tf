variable "project_id" {
  description = "The ID of the GCP project"
  type        = string
}

variable "region" {
  description = "The GCP region"
  type        = string
  default     = "us-central1"
}

variable "google_application_credentials" {
  description = "The path to the GCP credentials file"
  type        = string
}

variable "monday_api_key" {
  description = "API key for Monday.com"
  type        = string
}

variable "website_url" {
  description = "The URL of the website to scrape"
  type        = string
}

variable "board_id" {
  description = "The ID of the Monday.com board"
  type        = string
}

variable "group_id" {
  description = "The ID of the Monday.com group"
  type        = string
}

variable "zone" {
  description = "The GCP zone"
  type        = string
  default     = "us-central1-a"
}

variable "machine_type" {
  description = "The machine type for the GCP instance"
  type        = string
  default     = "f1-micro"
}
