import json

from slack_sdk import WebClient
from slack_sdk.rtm_v2 import RTMClient

import requests

import config

web_client = WebClient(token=config.User_OAuth_Token)
rtm_client = RTMClient(token=config.User_OAuth_Token)


def send_message(message_text):
    message = web_client.chat_postMessage(
        channel='#general',
        text=message_text
    )
    print(message)


def update_slack_status(status_text, status_emoji):
    status = web_client.users_profile_get()
    print(status)
    response = web_client.users_profile_set(
        profile={
            'status_text': status_text,
            'status_emoji': status_emoji,
        }
    )
    print(response)


def update_slack_status_web_api(status_text, status_emoji):
    base_url = 'https://slack.com/api/users.profile.set'
    headers = {
        'Content-type': 'application/json; charset=utf-8',
        'Authorization': f'Bearer {config.User_OAuth_Token}'
    }
    response = requests.post(
        base_url,
        headers=headers,
        data=json.dumps({
            'profile': {
                'status_text': status_text,
                'status_emoji': status_emoji
            }
        })
    )
    print(response.text)


def slack_bot_webhook(text: str = ''):
    url = config.Bot_Webhook_URL
    data = json.dumps({
        'text': text
    })
    response = requests.post(url, data=data)
    return print(response.status_code)


@rtm_client.on('message')
def handle(client: RTMClient, event: dict):
    if 'Hello' in event['text']:
        channel_id = event['channel']
        thread_ts = event['ts']
        user = event['user']  # This is not username but user ID (the format is either U*** or W***)

        client.web_client.chat_postMessage(
            channel=channel_id,
            text=f"Hi <@{user}>!",
            thread_ts=thread_ts
        )


if __name__ == '__main__':
    # send_message('Hello, world!')  # To certain channel
    # update_slack_status('Hello, world!', ':rocket:')
    update_slack_status_web_api('Hello, Slack Web API!', ':rocket:')
    # slack_bot_webhook('Hello, world!')  # To certain user or channel
    # rtm_client.start()
