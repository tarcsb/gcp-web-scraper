#!/bin/bash

# Function to print messages
function print_message() {
  echo "======================================="
  echo "$1"
  echo "======================================="
}

print_message "Authenticating with Google Cloud"
gcloud auth login

print_message "Setting the project to plewak-414307"
gcloud config set project plewak-414307

print_message "Granting Storage Admin role"
gcloud projects add-iam-policy-binding plewak-414307 \
  --member="serviceAccount:sa-plewak@plewak-414307.iam.gserviceaccount.com" \
  --role="roles/storage.admin"

print_message "Granting Compute Admin role"
gcloud projects add-iam-policy-binding plewak-414307 \
  --member="serviceAccount:sa-plewak@plewak-414307.iam.gserviceaccount.com" \
  --role="roles/compute.admin"

print_message "Granting Service Account User role"
gcloud projects add-iam-policy-binding plewak-414307 \
  --member="serviceAccount:sa-plewak@plewak-414307.iam.gserviceaccount.com" \
  --role="roles/iam.serviceAccountUser"

print_message "Enabling Compute Engine API"
gcloud services enable compute.googleapis.com

print_message "Enabling Cloud Functions API"
gcloud services enable cloudfunctions.googleapis.com

print_message "Enabling Cloud Storage API"
gcloud services enable storage.googleapis.com

print_message "Enabling Cloud Resource Manager API"
gcloud services enable cloudresourcemanager.googleapis.com

print_message "All roles granted and APIs enabled successfully"

