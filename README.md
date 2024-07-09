# GCP Web Scraper

## Author

**Jeff Plewak**
- Email: jrp.plewak@gmail.com
- Phone: ‪(561) 316-7986
- GitHub: [github.com/tarcsb](https://github.com/tarcsb)
- LinkedIn: [linkedin.com/in/plewak](https://linkedin.com/in/plewak)

## Project Overview

This project is designed to scrape data from a specified website, upload the scraped data to Google Cloud Storage, and update a Monday.com board with the scraped information. The project is built using Python and Terraform, and it leverages various cloud and automation technologies for efficient data processing and deployment.

## Features

- Web scraping using Python's `requests` and `beautifulsoup4` libraries.
- Uploads scraped data to Google Cloud Storage.
- Updates a Monday.com board with the scraped data.
- Infrastructure managed with Terraform.
- Detailed logging and error handling.
- Retry mechanisms for transient errors.
- Secure management of secrets using Google Secret Manager.
- Event-driven architecture with Google Pub/Sub.
- Analytics using Google Cloud Logging and Monitoring.

## Technical Skills Utilized

- **Languages**: Python, JavaScript (Node.js)
- **Frameworks & Libraries**: Flask, BeautifulSoup, Monday API
- **Cloud & DevOps**: Google Cloud Platform (GCP), Terraform
- **Data Engineering**: Google Cloud Storage
- **Testing**: PyTest, unittest
- **Agile Methodologies**: SCRUM, Kanban
- **Tools**: GitHub, Jira, CI/CD pipelines

## Requirements

- Python 3.7+
- Google Cloud SDK
- Terraform

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/tarcsb/gcp-web-scraper.git
   cd gcp-web-scraper
