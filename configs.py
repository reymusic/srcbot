# (c) @omega_projects

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 1))
    API_HASH = os.environ.get("API_HASH", "")
    ADMIN = int(os.environ.get('ADMIN', 1))
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Sharediskrobot")
    UPDATES_CHANNEL = int(os.environ.get("UPDATES_CHANNEL", ))
    DB_NAME = os.environ.get("DB_NAME", "srcbot")
    DB_URL = os.environ.get("DB_URL", "")
    BROADCAST_AS_COPY = os.environ.get("BROADCAST_AS_COPY", True)
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))
    
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


