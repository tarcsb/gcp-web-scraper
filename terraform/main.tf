provider "google" {
  project     = var.project_id
  region      = var.region
  credentials = file("${path.module}/../${var.google_application_credentials}")
}

resource "google_storage_bucket" "scraper_bucket" {
  name     = "${var.project_id}-scraper-bucket"
  location = var.region
}

resource "google_storage_bucket_object" "scraper_code" {
  name   = "scraper.py"
  bucket = google_storage_bucket.scraper_bucket.name
  source = "../src/scraper.py"
}

resource "google_cloudfunctions_function" "scraper_function" {
  name        = "web_scraper"
  description = "Cloud Function to scrape websites"
  runtime     = "python39"

  entry_point = "main"
  source_archive_bucket = google_storage_bucket.scraper_bucket.name
  source_archive_object = google_storage_bucket_object.scraper_code.name
  trigger_http = true

  available_memory_mb   = 128
  timeout               = 60

  environment_variables = {
    MONDAY_API_KEY = var.monday_api_key
    WEBSITE_URL    = var.website_url
    BOARD_ID       = var.board_id
    GROUP_ID       = var.group_id
  }
}

resource "google_compute_instance" "web_scraper" {
  name         = "web-scraper"
  machine_type = var.machine_type
  zone         = var.zone

  boot_disk {
    initialize_params {
      image = "projects/debian-cloud/global/images/family/debian-10"
    }
  }

  network_interface {
    network = "default"

    access_config {
      // Ephemeral IP
    }
  }
}
