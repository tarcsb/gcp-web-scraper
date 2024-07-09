resource "google_pubsub_topic" "scraping_topic" {
  name = "scraping-topic"
}

resource "google_pubsub_subscription" "scraping_subscription" {
  name  = "scraping-subscription"
  topic = google_pubsub_topic.scraping_topic.name
}
