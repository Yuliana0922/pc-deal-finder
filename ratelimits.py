import requests
from dotenv import load_dotenv
import os
import json

# Loading OAuth token from config.json
with open("config.json", "r") as file:
    config= json.load(file)

oauth_token = config['OAUTH_TOKEN']
print(oauth_token)

if not oauth_token:
    raise ValueError("OAuth token is missing! Please ensure it's present in your .env file.")

def check_rate_limits():
    # Analytics API endpoint to check rate limits
    url = "https://api.ebay.com/developer/analytics/v1_beta/rate_limit"

    # Set up the headers with the OAuth token
    headers = {
        "Authorization": f"Bearer {oauth_token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    # Make the API call to get rate limit data
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print("Rate limit data retrieved successfully.")
        return data
    else:
        print(f"Failed to retrieve rate limits: {response.status_code}")
        return None

# Run the function to check rate limits
rate_limit_data = check_rate_limits()

if rate_limit_data:
    print(rate_limit_data)

