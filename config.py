import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5805009276").split()))
OWNER_ID = int(getenv("OWNER_ID", "5805009276"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://JjjZaid: nakiba123456789@cluster0.ryzajxj.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5833041829:AAEa79DipgpNaHGOYZN9j_CG6QXtAIFrkPQ")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAQHmaBTutz3ZFjMMK92CvlQDSSGOAOr85APEZW8vV1hAuWo75fBFuGBL7Ki-mydF4U8cHmB2fz0fifmQyt4jOF9dxxgm44nRt_MLAceckVrakryxTClYSWdApIuGpQmWK8XZZyBjagdfKcQc90c7lVHwfmHdTr68ICn9zHDO5a7j9SBOJC_xbTABYXoEjq8cB__D2mELi2REN9rX6_9e8AAshMlu_w71qPqnjfj5sBQnmhrOGO6CivU5xt0e7nbwQrLIuuS0pKn58VODdh6YS1OIKeycY3B5oo_wCNQRrY7RZ3ix5xjHmADOJ6oe7Yy-FMTxV2_rguGIu2dDRPI9B1QAAAAFaAWl8AA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
