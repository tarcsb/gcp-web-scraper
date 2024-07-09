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

output "instance_ip" {
  value = google_compute_instance.web_scraper.network_interface[0].access_config[0].nat_ip
}
