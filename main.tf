provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_compute_instance" "web_scraper" {
  name         = "web-scraper"
  machine_type = "f1-micro"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-10"
    }
  }

  network_interface {
    network = "default"

    access_config {
      // Ephemeral IP
    }
  }

  metadata_startup_script = <<-EOT
    #!/bin/bash
    sudo apt-get update
    sudo apt-get install -y python3-pip
    pip3 install requests beautifulsoup4 monday
    # Clone the repository and set up the scraper script
    git clone https://github.com/tarcsb/gcp-web-scraper.git /home/scraper
    python3 /home/scraper/scraper.py
  EOT
}

