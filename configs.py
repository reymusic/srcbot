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

π€ My Name: <a href='https://t.me/MdiskDisneyStudiobot'>Disney Studio bot</a>
π Language : <a href='https://www.python.org'> Python V3</a>
π Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>
π‘ Server: <a href='https://heroku.com'>Heroku</a>
π¨βπ» Created By: <a href='https://t.me/tech_ai_bots'>Tech Ai Bots</a></b>
"""

    ABOUT_HELP_TEXT = """<b>π¨βπ» Developer : <a href='https://t.me/Tech_ai_bots'>Click Me</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer or π³ DM π .</b>
"""

    HOME_TEXT = """
<b>Hey! {}π,

I'm Mdisk Search Robot.π€

I Can Search π What You Wantβ

πMade for @Disney_hindi_movie</b>
"""


    START_MSG = """
<b>Hey! {}π,

I'm Mdisk Search Robot.π€

I Can Search π What You Wantβ

πMade for @Disney_hindi_movie</b>
"""


