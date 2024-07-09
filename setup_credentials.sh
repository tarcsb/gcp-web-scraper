#!/bin/bash

# Function to print messages
function print_message() {
  echo "======================================="
  echo "$1"
  echo "======================================="
}

# Function to prompt for an environment variable
function prompt_for_env_var() {
  local var_name="$1"
  local prompt_message="$2"
  if ! grep -q "$var_name=" .env; then
    echo "$prompt_message"
    read -r value
    echo "$var_name=$value" >> .env
  fi
}

print_message "Setting up credentials and environment variables"

if [ ! -f ".env" ]; then
  touch .env
fi

prompt_for_env_var "GCP_PROJECT_ID" "Enter your GCP Project ID:"
echo "GOOGLE_APPLICATION_CREDENTIALS=secrets/gcp-key.json" >> .env
prompt_for_env_var "MONDAY_API_KEY" "Enter your Monday.com API Key:"
prompt_for_env_var "SCRAPE_URL" "Enter the website URL to scrape:"
prompt_for_env_var "BOARD_ID" "Enter your Monday.com Board ID:"
prompt_for_env_var "GROUP_ID" "Enter your Monday.com Group ID:"

print_message "Credentials and environment variables setup complete"
