# (c) @omega_projects

from configs import Config
from pyrogram import Client, filters, idle
from pyrogram.errors import QueryIdInvalid
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InlineQuery, InlineQueryResultArticle, \
    InputTextMessageContent
import asyncio

# Bot Client for Inline Search
Bot = Client(
    session_name=Config.BOT_SESSION_NAME,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

# User Client for Searching in Channel.
User = Client(
    session_name=Config.USER_SESSION_STRING,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    admin=Config.ADMIN
)

@Bot.on_message(filters.private & filters.command("start"))
async def start_handler(_, event: Message):
	await event.reply_photo("https://telegra.ph/file/d4e0b3b840b23dcd21fa4.jpg",
                                caption=Config.START_MSG.format(event.from_user.mention),
                                reply_markup=InlineKeyboardMarkup([
                                    [InlineKeyboardButton("➕ Add Me to Your Group ➕", url="http://t.me/MdiskDisneyStudiobot?startgroup=true")], 
                                    [InlineKeyboardButton("♻️ Backup", url="https://t.me/disney_hindi_movie"),
                                     InlineKeyboardButton("🍿 Group", url="https://t.me/+JSeBDW0bmgtiOGZl")],
                                    [InlineKeyboardButton("📢 Updates", url="https://t.me/tech_ai_bots"),
                                     InlineKeyboardButton("🔍 Files 📁", url="https://t.me/ai_filter_bot")],
                                    [InlineKeyboardButton("⭕ Help", callback_data="Help_msg"),
                                     InlineKeyboardButton("🧰 About", callback_data="About_msg")]]))

@Bot.on_message(filters.private & filters.command("help"))
async def help_handler(_, event: Message):

    await event.reply_text(Config.ABOUT_HELP_TEXT.format(event.from_user.mention),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🛡Support Group", url="https://t.me/omega_pro_support")], 
            [InlineKeyboardButton("💰 Mdisk bot", url="https://t.me/Mdisk_money_bot"), 
             InlineKeyboardButton("🧰 About", callback_data="About_msg")]
        ])
    )

@Bot.on_message(filters.incoming)
async def inline_handlers(_, event: Message):
    if event.text == '/start':
        return
    answers = f'<b>🏷 {event.text} \n\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬</b>\n✅ Check Your Spelling.✍️\n⭕️ Add Year For Better Result.🗓️\n<b>▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n\n</b>'
    async for message in User.search_messages(chat_id=Config.CHANNEL_ID, limit=50, query=event.text):
        if message.text:
            thumb = None
            f_text = message.text
            msg_text = message.text.html
            if "|||" in message.text:
                f_text = message.text.split("|||", 1)[0]
                msg_text = message.text.html.split("|||", 1)[0]
            answers += f'**🍿 Title ➠ **' + '' + f_text.split("\n", 1)[0] + '' + '**\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n\n**' + '' + f_text.split("\n", 2)[-1] + ' \n\nBackup : @disney_hindi_movie\n\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n<i>Link Auto Deletes in 60Sec...</i>\n▰▱▰▱▰▱▰▱▰▱▰▱▰▱\n\n'
    try:
        msg = await event.reply_text(answers)
        await asyncio.sleep(60)
        await event.delete()
        await msg.delete()
    except:
        print(f"[{Config.BOT_SESSION_NAME}] - Failed to Answer - {event.from_user.first_name}")


@Bot.on_callback_query()
async def button(bot, cmd: CallbackQuery):
        cb_data = cmd.data
        if "About_msg" in cb_data:
            await cmd.message.edit(
			text=Config.ABOUT_BOT_TEXT,
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("🛡Support Group", url="https://t.me/omega_pro_support"), 
					],
					[
						InlineKeyboardButton("⭕ Help", callback_data="Help_msg"),
						InlineKeyboardButton("⏪ Back", callback_data="gohome")
					]
				]
			),
			parse_mode="html"
		)
        elif "Help_msg" in cb_data:
            await cmd.message.edit(
			text=Config.ABOUT_HELP_TEXT,
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("🔳 DM 🎀", url="https://t.me/aidsbots"),
						InlineKeyboardButton("💰 Mdisk bot", url="https://t.me/Mdisk_money_bot")
					], 
                                        [
						InlineKeyboardButton("🧰 About", callback_data="About_msg"),
						InlineKeyboardButton("🔝 Home", callback_data="gohome")
					]
				]
			),
			parse_mode="html"
		)
        elif "gohome" in cb_data:
            await cmd.message.edit(
			text=Config.START_MSG.format(cmd.from_user.mention),
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				 [  
                                    [InlineKeyboardButton("➕ Add Me to Your Group ➕", url="http://t.me/MdiskDisneyStudiobot?startgroup=true")], 
                                    [InlineKeyboardButton("♻️ Backup", url="https://t.me/disney_hindi_movie"),
                                     InlineKeyboardButton("🍿 Group", url="https://t.me/+JSeBDW0bmgtiOGZl")],
                                    [InlineKeyboardButton("📢 Updates", url="https://t.me/tech_ai_bots"),
                                     InlineKeyboardButton("🔍 Files 📁", url="https://t.me/ai_filter_bot")],
                                    [InlineKeyboardButton("⭕ Help", callback_data="Help_msg"),
                                     InlineKeyboardButton("🧰 About", callback_data="About_msg")]
                                ]

			),
			parse_mode="html"
		)

# Start Clients
Bot.start()
User.start()
# Loop Clients till Disconnects
idle()
# After Disconnects,
# Stop Clients
Bot.stop()
User.stop()
