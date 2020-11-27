from flask import Flask
from flask import request
from twilio.rest import Client
from services import get_usd_price
import os
import dialogflow
from google.api_core.exceptions import InvalidArgument
import requests
import json

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'gcp_private_key.json'

DIALOGFLOW_PROJECT_ID = 'currencywhatsappbot-my9w'
DIALOGFLOW_LANGUAGE_CODE = 'es'
SESSION_ID = 'test'

app = Flask(__name__)

#Initialize Twilio Client
ACCOUNT_ID = os.environ.get('TWILIO_ACCOUNT')
TWILIO_TOKEN = os.environ.get('TWILIO_TOKEN')
client = Client(ACCOUNT_ID, TWILIO_TOKEN)
TWILIO_NUMBER = 'whatsapp:+14155238886'

@app.route("/start", methods=["POST"])
def start():
  f = request.form
  message = f['Body']
  sender = f['From']
  print(sender)
  session_client = dialogflow.SessionsClient()
  session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
  text_input = dialogflow.types.TextInput(text=message, language_code=DIALOGFLOW_LANGUAGE_CODE)
  query_input = dialogflow.types.QueryInput(text=text_input)
  try:
    response = session_client.detect_intent(session=session, query_input=query_input)
  except InvalidArgument:
    raise
    
  sendMessage(sender, response.query_result.fulfillment_text)
  return response.query_result.fulfillment_text

def sendMessage(recipient, message):
  client.messages.create(
    from_=TWILIO_NUMBER,
    body=message,
    to=recipient
  )