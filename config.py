import os

import dotenv

dotenv.load_dotenv()

User_OAuth_Token = os.environ.get("User_OAuth_Token")
Bot_User_OAuth_Token = os.environ.get("Bot_User_OAuth_Token")
Calendar_ICS_URL = os.environ.get("Calendar_ICS_URL")
Bot_Webhook_URL = os.environ.get("Bot_Webhook_URL")
