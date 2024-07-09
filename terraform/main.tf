provider "google" {
  project     = var.project_id
  region      = var.region
  credentials = file("${path.module}/../${var.google_application_credentials}")
}

module "compute_instance" {
  source = "./modules/google_compute_instance"
}

module "cloudfunctions_function" {
  source = "./modules/google_cloudfunctions_function"
}

module "storage_bucket" {
  source = "./modules/google_storage_bucket"
}

module "pubsub" {
  source = "./modules/google_pubsub"
}
