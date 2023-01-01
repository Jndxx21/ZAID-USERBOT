import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "23956534")) #optional
API_HASH = getenv("API_HASH", "00a8b56e240e16e95a322d42a122aa68") #optional

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
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAjteejgAvVmfRzbOYfKloWDkTjDNJBQik2MdHNdG_tCGOKIo0Iw9G1a9yIdPm2KYoQzLhP4LhBzROxuAAgcZNriGdzJ7Jwaco4u927nu6YB1vfFzmF1qSHZocDE6upvkQ0UzPHDVtKEaP-RwbkvjUxb21Ves-ukaCYWI8ex_EevHQZmoH0cZRtKKfZ8Ce1zYZt6Sp_0wk4MaJc3BaCDk_jl60gb6bpPfraey6BUbm6rQ4LQem_ICY7GSYi8sk55W8m2W6zU22TjfFW_fXHLX-oTwtRfZpUNi7YiffJfBARUF71UNmi4sNMvpfKypmEZgv1q5pYJpKiBqlRjV7GenNdQAAAAFaAWl8AA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
