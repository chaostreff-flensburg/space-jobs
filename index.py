import os
import schedule
import time
from datetime import datetime
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

load_dotenv()

SLACK_TOKEN = os.getenv('SLACK_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')
MESSAGE = os.getenv('MESSAGE')

def send_poll_message():
    client = WebClient(token=SLACK_TOKEN)

    try:
        response = client.chat_postMessage(
            channel=CHANNEL_ID,
            text=MESSAGE
        )
        print("Message sent successfully:", response['ts'])
        # Add a reaction to the message
        client.reactions_add(
            channel=CHANNEL_ID,
            name='white_check_mark',
            timestamp=response['ts']
        )
    except SlackApiError as e:
        print(f"Error sending message: {e.response['error']}")

print("Poll bot is running...")

schedule.every().tuesday.at("14:00").do(send_poll_message)

while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute if it's time to send the message
