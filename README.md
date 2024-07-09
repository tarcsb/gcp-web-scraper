curl -X POST -H "Authorization: YOUR_MONDAY_API_KEY" \
-H "Content-Type: application/json" \
-d '{"query":"{ boards { id name } }"}' \
https://api.monday.com/v2


cd terraform
terraform init

terraform apply

source venv/bin/activate
python src/scraper.py



chmod +x setup_credentials.sh
./setup_credentials.sh


