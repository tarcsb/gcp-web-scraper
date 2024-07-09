output "instance_ip" {
  value = google_compute_instance.web_scraper.network_interface[0].access_config[0].nat_ip
}

output "scraper_function_url" {
  value = google_cloudfunctions_function.scraper_function.https_trigger_url
}
