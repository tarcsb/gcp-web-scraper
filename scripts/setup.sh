#!/bin/bash

# Function to print messages with timestamps
function print_message() {
  echo "======================================="
  echo "$(date '+%Y-%m-%d %H:%M:%S') - $1"
  echo "======================================="
}

# Function to check if a command exists
function check_command() {
  if ! command -v $1 &> /dev/null; then
    echo "$1 could not be found. Please install $1."
    exit 1
  fi
}

# Function to retry a command with a timeout
function retry {
  local n=1
  local max=5
  local delay=10
  while true; do
    "$@" && break || {
      if [[ $n -lt $max ]]; then
        ((n++))
        print_message "Command failed. Attempt $n/$max:"
        sleep $delay;
      else
        print_message "The command has failed after $n attempts."
        return 1
      fi
    }
  done
}

print_message "Checking for required tools"
check_command gcloud
check_command jq
check_command terraform

print_message "Setting up credentials and environment variables"

# Define the path to the .env file
SCRIPT_DIR="$(dirname "$0")"
ENV_FILE="$SCRIPT_DIR/../.env"

# Load environment variables from .env file
if [ -f "$ENV_FILE" ]; then
  export $(grep -v '^#' "$ENV_FILE" | xargs)
else
  print_message ".env file not found in the gcp-web-scraper/ directory. Please ensure it exists and contains the necessary variables."
  exit 1
fi

# Verify that the necessary variables are set
REQUIRED_VARS=("GCP_PROJECT_ID" "GOOGLE_APPLICATION_CREDENTIALS" "MONDAY_API_KEY" "WEBSITE_URL" "BOARD_ID" "GROUP_ID" "ZONE")
for VAR in "${REQUIRED_VARS[@]}"; do
  if [ -z "${!VAR}" ]; then
    print_message "Environment variable $VAR is not set. Please ensure .env contains $VAR."
    exit 1
  fi
done

# Check if the JSON key file exists and is valid JSON
KEY_FILE="$SCRIPT_DIR/../$GOOGLE_APPLICATION_CREDENTIALS"
if [ ! -f "$KEY_FILE" ]; then
  print_message "The JSON key file $KEY_FILE does not exist. Please check the file path."
  exit 1
fi

if ! jq empty "$KEY_FILE" >/dev/null 2>&1; then
  print_message "The JSON key file is not valid. Please check the file and ensure it is correctly formatted."
  exit 1
fi

print_message "Authenticating with Google Cloud"
gcloud auth activate-service-account --key-file="$KEY_FILE" || { print_message "Failed to authenticate with Google Cloud"; exit 1; }

print_message "Setting the project to $GCP_PROJECT_ID"
gcloud config set project $GCP_PROJECT_ID || { print_message "Failed to set GCP project"; exit 1; }

print_message "Granting necessary roles to the service account"
# Grant Storage Admin role
gcloud projects add-iam-policy-binding $GCP_PROJECT_ID \
  --member="serviceAccount:sa-plewak@plewak-414307.iam.gserviceaccount.com" \
  --role="roles/storage.admin" || { print_message "Failed to grant Storage Admin role"; exit 1; }

# Grant Compute Admin role
gcloud projects add-iam-policy-binding $GCP_PROJECT_ID \
  --member="serviceAccount:sa-plewak@plewak-414307.iam.gserviceaccount.com" \
  --role="roles/compute.admin" || { print_message "Failed to grant Compute Admin role"; exit 1; }

# Grant Service Account User role
gcloud projects add-iam-policy-binding $GCP_PROJECT_ID \
  --member="serviceAccount:sa-plewak@plewak-414307.iam.gserviceaccount.com" \
  --role="roles/iam.serviceAccountUser" || { print_message "Failed to grant Service Account User role"; exit 1; }

print_message "Enabling necessary APIs"
gcloud services enable compute.googleapis.com || { print_message "Failed to enable Compute Engine API"; exit 1; }
gcloud services enable cloudfunctions.googleapis.com || { print_message "Failed to enable Cloud Functions API"; exit 1; }
gcloud services enable storage.googleapis.com || { print_message "Failed to enable Cloud Storage API"; exit 1; }
gcloud services enable cloudresourcemanager.googleapis.com || { print_message "Failed to enable Cloud Resource Manager API"; exit 1; }

print_message "Environment variables loaded and exported for Terraform."

# Export variables as TF_VAR_* for Terraform
export TF_VAR_project_id=$GCP_PROJECT_ID
export TF_VAR_google_application_credentials=$GOOGLE_APPLICATION_CREDENTIALS
export TF_VAR_monday_api_key=$MONDAY_API_KEY
export TF_VAR_website_url=$WEBSITE_URL
export TF_VAR_board_id=$BOARD_ID
export TF_VAR_group_id=$GROUP_ID
export TF_VAR_zone=$ZONE

print_message "Cleaning previous Terraform state"
# Navigate to the Terraform directory
cd "$SCRIPT_DIR/../terraform" || exit

# Remove Terraform state files if they exist
rm -f terraform.tfstate*
rm -f .terraform.lock.hcl

print_message "Initializing Terraform"
retry terraform init || { print_message "Failed to initialize Terraform"; exit 1; }

print_message "Applying Terraform configuration"
retry terraform apply -auto-approve || { print_message "Failed to apply Terraform configuration"; exit 1; }

# Navigate back to project root
cd "$SCRIPT_DIR/.." || exit

print_message "Setup script completed successfully"
