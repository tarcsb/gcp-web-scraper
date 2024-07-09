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
REQUIRED_VARS=("GCP_PROJECT_ID" "GOOGLE_APPLICATION_CREDENTIALS")
for VAR in "${REQUIRED_VARS[@]}"; do
  if [ -z "${!VAR}" ]; then
    print_message "Environment variable $VAR is not set. Please ensure .env contains $VAR."
    exit 1
  fi
done

# Check if the JSON key file exists
KEY_FILE="$SCRIPT_DIR/../$GOOGLE_APPLICATION_CREDENTIALS"
if [ ! -f "$KEY_FILE" ]; then
  print_message "The JSON key file $KEY_FILE does not exist. Please check the file path."
  exit 1
fi

print_message "Authenticating with Google Cloud"
gcloud auth activate-service-account --key-file="$KEY_FILE" || { print_message "Failed to authenticate with Google Cloud"; exit 1; }

print_message "Setting the project to $GCP_PROJECT_ID"
gcloud config set project $GCP_PROJECT_ID || { print_message "Failed to set GCP project"; exit 1; }

print_message "Destroying Terraform managed infrastructure"
# Navigate to the Terraform directory
cd "$SCRIPT_DIR/../terraform" || exit

print_message "Destroying resources managed by Terraform"
retry terraform destroy -auto-approve || { print_message "Failed to destroy Terraform managed infrastructure"; exit 1; }

# Navigate back to project root
cd "$SCRIPT_DIR/.." || exit

print_message "Teardown script completed successfully"
