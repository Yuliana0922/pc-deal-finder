import requests

# Replace this with your actual OAuth token
oauth_token = 'v^1.1#i^1#r^0#I^3#f^0#p^3#t^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'

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
