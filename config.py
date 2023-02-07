# Thanks For: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/ramadhani892/RamPyro-Bot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/ramsupportt


from distutils.util import strtobool
from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


ALIVE_EMOJI = getenv("ALIVE_EMOJI", "👑")
ALIVE_LOGO = getenv("ALIVE_LOGO", "https://telegra.ph/file/970cc2e71824203876a00.jpg")
ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "Hey bro, I am Luffy.")
API_HASH = getenv("API_HASH", "8d7db642ff9200d0ad118fd0e3303045")
API_ID = getenv("API_ID", "27993115")
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001528080636]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "-1001528080636").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID", "-1001477499506")
BOT_TOKEN = getenv("BOT_TOKEN", "5379182487:AAEhLHQuBmzpkPRAUs3Dk0VFg41Dr44nz58")
BOT_VER = "1.0.3@master"
BRANCH = getenv("BRANCH", "main")
CH_SFS = getenv("CH_SFS", "b4c0d")
IG_ALIVE = getenv("IG_ALIVE", "panggil_m")
CHANNEL = getenv("CHANNEL", "nakama_asl")
CMD_HANDLER = getenv("CMD_HANDLER", "~")
DB_URL = getenv("DATABASE_URL", "postgres://dnlyohdv:xJYyTD2QjfgVh_fju7ViQoeVIeDPyP3U@rosie.db.elephantsql.com/dnlyohdv")
GIT_TOKEN = getenv("GIT_TOKEN", "")
GROUP = getenv("GROUP", "nakamaop")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
OPENAI_API_KEY = getenv("OPENAI_API_KEY", "")
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
REPO_URL = getenv("REPO_URL", "https://github.com/virtualunionsex/Ram-Pyro")
STRING_SESSION1 = getenv("STRING_SESSION1", "BQAhIHQAtM5ZyVmy0k6_vW1bIgJDRbYuzjCJkUzsKf6A2gkOfhLWDfdS87EKJ1PZHaRPYzDRh5fKIAuT1Q457zxCKAna7FO_tAr0DFDSu9WH6V_y4w64rZGKieXg1byztBJO-xA0fTiG22kRliOxc8uoaMuTzzLfGlaTGBmCJFQlD9M9TsCNeRyklJqu-PWe0eAEr6bjDZpbjhmLcI77peDuV6_mv7KeHniPo0llhVQ_vBxT0HI5ACariypYI1ILkLR0qjzvVdegJWVEjS2GFSdfEADDShCKFGjObQOr5WkgiJP15QnVA8jaRfykI2SHwodSUbkC4r5POGykixRIpaR_zXaBAgAAAABszMKvAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
