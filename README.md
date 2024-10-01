# PC Part Deal Notifier

This project is a Python-based tool that tracks and notifies users of good deals on specific PC parts listed on eBay. 
The tool uses eBay's Browse API to search for items based on keywords, filters results to exclude products being sold broken, incomplete, just the boxes or for parts, and calculates the average and median prices for comparison. 
If a deal is priced below the average, it sends a notification to a Slack channel with the deal details and link.


The initial scope wanted to use Ebay's Finding API to calculate the average price based on sold listings, but that option is currently unavailable to me.



## Features
  - Searches for specific PC parts on eBay using the Browse API.
  - Filters out items with user-specified exclusion keywords like "Broken", "For Parts", "AS IS", etc.
  - Calculates average and median prices from active listings.
  - Sends a Slack notification if a new deal is below the calculated average price.
  - User input for product keywords, condition, timeframe, and exclusion keywords.

## Installation
1. Clone this repository:
   ```git clone https://github.com/YOUR_GITHUB_USERNAME/pc-part-deal-notifier.git
   cd pc-part-deal-notifier```
   
2. Install the necessary dependencies:
     ```pip install -r requirements.txt```

3. Create a .env file in the root directory and add your Slack token:
   ```SLACK_TOKEN=your_slack_token```

4. You will also need a config.json file in the root directory to store eBay OAuth token. You'll need to sign up for Ebay's developer program and wait a day. This is a config.json because .env file limitations:
  ```{  "OAUTH_TOKEN": "your_oauth_token}```

# How to use

The script is a Jupyter Notebook for ease of use. Just change the user inputs and run the entire script. Here are the inputs you have to give the script.
- product_keywords: Keywords describing the PC part (e.g., "GPU RTX 3060 12GB").
- condition: The condition of the items to search for (e.g., "New", "Used").
- timeframe_days: The maximum number of days since the item was listed.
- exclusion_keywords: Keywords to exclude from the results (e.g., "Broken", "AS IS").

Technologies

    Python
    Slack SDK: For sending notifications to Slack.
    eBay Browse API: For fetching eBay listings.
    dotenv: For handling environment variables.
    nunpy: to calculate median prices.

Contributors
Yuliana Gonzalez (Yuliana0922)

