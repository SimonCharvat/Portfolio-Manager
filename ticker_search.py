

import json
import requests
import pandas as pd

def query_yahoo_finance_for_ticker(query: str):

    url = "https://query2.finance.yahoo.com/v1/finance/search"
    params = {
        "q": query,
        "lang": "en-US",
        "region": "US",
        "quotesCount": "10",
        "quotesQueryId": "tss_match_phrase_query",
        "multiQuoteQueryId": "multi_quote_single_token_query",
        "enableCb": "false",
        "enableNavLinks": "true",
        "enableCulturalAssets": "true",
        "enableNews": "false",
        "enableResearchReports": "false",
        "listsCount": "1",
        "recommendCount": "10"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }

    response = requests.get(url, params=params, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        print(f"Request successful")
        return response.text
    else:
        print(f"Request failed, code: {response.status_code}, reason: {response.reason}")
        return False
    


def parse_query_response(json_text: str):
    data = json.loads(json_text)
    stocks = []
    
    for item in data.get("quotes", []):
        # Extract required fields with defaults if they are missing
        stock = {
            "name_short": item.get("shortname", ""),
            "exchange_tag": item.get("exchange", ""),
            "instrument_type": item.get("quoteType", ""),
            "ticker": item.get("symbol", ""),
            "industry": item.get("industry", "")
        }
        stocks.append(stock)
        
        df_stocks = pd.DataFrame(stocks)
    
    return df_stocks


# use query functions

# get raw data from yahoo finance
query_response_raw = query_yahoo_finance_for_ticker("Vanguard world")

# format the raw data into panda
df_query_stocks = parse_query_response(query_response_raw)

print(df_query_stocks)


print()
