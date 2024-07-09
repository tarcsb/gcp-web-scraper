resource "google_storage_bucket" "scraper_bucket" {
  name     = "${var.project_id}-scraper-bucket"
  location = var.region
}

resource "google_storage_bucket_object" "scraper_code" {
  name   = "scraper.py"
  bucket = google_storage_bucket.scraper_bucket.name
  source = "../src/scraper.py"
}
