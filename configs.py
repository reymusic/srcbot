# (c) @omega_projects

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 19977122))
    API_HASH = os.environ.get("API_HASH", "168c8159234070c260a85df74feae727")
    BOT_TOKEN = [os.environ.get("BOT_TOKEN", "5649770570:AAHush_bJFtDSsPNnrdVf3cELQD0x96CR7c" "5260749200:AAGAn7-UDsaUsf1P6a5m9FSflkZBJ9GTOBE").split()]
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQCwrMD45DyZE1aS4pwlPnQTSdJ98R1IHHMRZP6A_X9ThFMyqkgeGhaQ268XaVytEGWUT6K21Yz3IK6kWdDYD0i-lRDw006fg6vopnYy9xSK4WeUCLVtD1x6ldkXpYNcHJhLuCevgRhl0m6e9OreXvTLNdTrBB2jfWB7-R7B92GXkkplRYxk5kEuklQ3jdtV2UhexzuZWJnlFD1ld5Bg9zIjq-O-nMP1HE4yi1h8nOoGOtao2nHTf_2S0kUeRUcA0WEYbCBSoUvAWHpVSCPbON-EYXj5ai_wfLxI9ozjRoOo80BnHObfgVLaWZ9tsTns7HSXH_311ExZ-5FK_CVxIG99cXlxawA")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1001873244035))
    BOT_USERNAME = [os.environ.get("BOT_USERNAME", "MdiskDisneyStudiobot" "MdiskDownloaderultronBot").split()]
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1903784299))
    UPDATES_CHANNEL = int(os.environ.get("UPDATES_CHANNEL", -1001739538472))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://sample123:sample123@cluster0.ridbnpt.mongodb.net/?retryWrites=true&w=majority")
    BROADCAST_AS_COPY = os.environ.get("BROADCAST_AS_COPY", True)
    DATABASE_URL = int(os.environ.get("LOG_CHANNEL", -1001579883875))
    
            ## variables for bot
    
    ABOUT_BOT_TEXT = """<i>This is Mdisk Search Bot & Very Soon it's have a filters Capabilities & much more. </i>

🤖 My Name: <a href='https://t.me/MdiskDisneyStudiobot'>Disney Studio bot</a>
📝 Language : <a href='https://www.python.org'> Python V3</a>
📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>
📡 Server: <a href='https://heroku.com'>Heroku</a>
👨‍💻 Created By: <a href='https://t.me/tech_ai_bots'>Tech Ai Bots</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer : <a href='https://t.me/Tech_ai_bots'>Click Me</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer or 🔳 DM 🎀 .</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Mdisk Search Robot.🤖

I Can Search 🔍 What You Want❗

🎀Made for @Disney_hindi_movie</b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Mdisk Search Robot.🤖

I Can Search 🔍 What You Want❗

🎀Made for @Disney_hindi_movie</b>
"""


