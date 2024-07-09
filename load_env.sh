#!/bin/bash

# Load environment variables from .env file
if [ -f .env ]; then
  export $(cat .env | grep -v '^#' | xargs)
else
  echo ".env file not found. Please ensure it exists and contains the necessary variables."
  exit 1
fi

# Export variables as TF_VAR_* for Terraform
export TF_VAR_project_id=$GCP_PROJECT_ID
export TF_VAR_google_application_credentials=$GOOGLE_APPLICATION_CREDENTIALS
export TF_VAR_monday_api_key=$MONDAY_API_KEY
export TF_VAR_website_url=$SCRAPE_URL
export TF_VAR_board_id=$BOARD_ID
export TF_VAR_group_id=$GROUP_ID

echo "Environment variables loaded and exported for Terraform."
