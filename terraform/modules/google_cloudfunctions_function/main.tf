resource "google_cloudfunctions_function" "scraper_function" {
  name        = "web_scraper"
  description = "Cloud Function to scrape websites"
  runtime     = "python39"

  entry_point = "main"
  source_archive_bucket = var.bucket_name
  source_archive_object = var.source_archive_object
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

output "scraper_function_url" {
  value = google_cloudfunctions_function.scraper_function.https_trigger_url
}
