import requests
import json

def get_usd_price():
  endpoint = 'https://api.bitso.com/v3/ticker/?book=dai_mxn'
  api_response = requests.get(endpoint)
  json_response = json.loads(api_response.text)
  return {
    "last_price": json_response["payload"]["last"]
  }