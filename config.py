#(©)CodeXBotz

import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv()

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7469198869:AAGL83C8Xz8kboHUiUSKAE5Dta4y9JipWRo")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "22418774"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "d8c8dab274f9a811814a6a96d044028e")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001750485720"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "2129936439"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://botmaker9675208:botmaker9675208@cluster0.sc9mq8b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", ""))
JOIN_REQUEST_ENABLE = os.environ.get("JOIN_REQUEST_ENABLED", "")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_PIC = os.environ.get("START_PIC","")
START_MSG = os.environ.get("START_MESSAGE", "🎚Cʜᴀɴɴᴇʟ Lɪɴᴋ ⟹ https://t.me/+pT2esZ-4jucyZDc1

✅ (BluRay + Original Audios) - [1080p - 720p - 480p - 360p - 280p]

✅ 240p - https://t.me/+pT2esZ-4jucyZDc1

✅ 360p - https://t.me/+pT2esZ-4jucyZDc1

✅ 720P - https://t.me/+pT2esZ-4jucyZDc1

✅ 1080P - https://t.me/+pT2esZ-4jucyZDc1

✅ Join & Download Now ⬇️

Search Any Movie/Series Here And Get It In 1 Seconds👇👇👇👇👇
https://t.me/+tqHsm2_-lts3NTk1
https://t.me/+tqHsm2_-lts3NTk1 
https://t.me/+tqHsm2_-lts3NTk1")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Auto delete time in seconds.
AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", "0"))
AUTO_DELETE_MSG = os.environ.get("AUTO_DELETE_MSG", "This file will be automatically deleted in {time} seconds. Please ensure you have saved any necessary content before this time.")
AUTO_DEL_SUCCESS_MSG = os.environ.get("AUTO_DEL_SUCCESS_MSG", "Your file has been successfully deleted. Thank you for using our service. ✅")

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
