# Don't Remove Credit @AshutoshGoswami24
import pyrogram
import os
import asyncio

# Don't Remove Credit @AshutoshGoswami24
try:
    app_id = int(os.environ.get("app_id", "22287041"))
except Exception as app_id:
    print(f"⚠️ App ID Invalid {app_id}")
try:
    api_hash = os.environ.get("api_hash", "c149386dcd58a40fa9fe60e632e161d4")
except Exception as api_id:
    print(f"⚠️ Api Hash Invalid {api_hash}")
try:
    bot_token = os.environ.get("bot_token", "7088270463:AAHUyHPQWB6pUDgLBt8pXpDatZAjVpmWRRk")
except Exception as bot_token:
    print(f"⚠️ Bot Token Invalid {bot_token}")
try:
    custom_caption = os.environ.get("custom_caption", "📽️𝗡𝗮𝗺𝗲 - 

👍𝗦𝘁𝗮𝘁𝘂𝘀 - 𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗱✅

✅𝗦𝗲𝗮𝗿𝗰𝗵 𝗡𝗼𝘄 𝗜𝗻 - @MovieSearchPanda

😁𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗬𝗼𝘂𝗿 𝗠𝗼𝘃𝗶𝗲𝘀 𝗛𝗲𝗿𝗲 - @PandaRequestMovies")
except Exception as custom_caption:
    print(f"⚠️ Custom Caption Invalid {custom_caption}")

# Don't Remove Credit @AshutoshGoswami24
Ashu = pyrogram.Client(
    name="Ashu", api_id=app_id, api_hash=api_hash, bot_token=bot_token)

# Don't Remove Credit @AshutoshGoswami24
start_message = """
<b>👋Hello {}</b>
<b>I am an AutoCaption bot</b>
<b>All you have to do is add me to your channel and I will show you my power</b>
<b>@PandaWep</b>"""

# Don't Remove Credit @AshutoshGoswami24
about_message = """
<b>• Name : <a href=https://t.me/PandaWep>PandaWep</a></b>
<b>• Developer : <a href=https://github.com/AshutoshGoswami24>[Ashu]</a></b>
<b>• Language : Python3</b>
<b>• Library : Pyrogram v{version}</b>
<b>• Updates : <a href=https://t.me/PandaWep>Click Here</a></b>
<b>• Source Code : <a href=https://github.com/AshutoshGoswami24/AutoCaptionBot-By-Ashu>Click Here</a></b>"""

# Don't Remove Credit @AshutoshGoswami24
@Ashu.on_message(pyrogram.filters.private & pyrogram.filters.command(["start"]))
def start_command(bot, update):
    update.reply(start_message.format(update.from_user.mention), reply_markup=start_buttons(bot, update),
                  parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

# Don't Remove Credit @AshutoshGoswami24
@Ashu.on_callback_query(pyrogram.filters.regex("start"))
def strat_callback(bot, update):
    update.message.edit(start_message.format(update.from_user.mention), reply_markup=start_buttons(bot, update.message),
                        parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

# Don't Remove Credit @AshutoshGoswami24
@Ashu.on_callback_query(pyrogram.filters.regex("about"))
def about_callback(bot, update):
    bot = bot.get_me()
    update.message.edit(about_message.format(version=pyrogram.__version__, username=bot.mention),
                        reply_markup=about_buttons(bot, update.message), parse_mode=pyrogram.enums.ParseMode.HTML,
                        disable_web_page_preview=True)

# Don't Remove Credit @AshutoshGoswami24
@Ashu.on_message(pyrogram.filters.photo)
def edit_caption(bot, update: pyrogram.types.Message):
    motech, file_name = get_file_details(update)
    try:
        try:
            update.edit(custom_caption.format(file_name=file_name))
        except pyrogram.errors.FloodWait as FloodWait:
            asyncio.sleep(FloodWait.value)
            update.edit(custom_caption.format(file_name=file_name))
    except pyrogram.errors.MessageNotModified:
        pass

# Don't Remove Credit @AshutoshGoswami24
def get_file_details(update: pyrogram.types.Message):
    if update.photo:
        obj = update.photo
        # Generate unique file name for photo
        file_name = f"photo_{obj.file_id}.jpg"
        return obj, file_name

# Don't Remove Credit @AshutoshGoswami24
def start_buttons(bot, update):
    bot = bot.get_me()
    buttons = [[
        pyrogram.types.InlineKeyboardButton("Updates", url="t.me/PandaWep"),
        pyrogram.types.InlineKeyboardButton("About 🤠", callback_data="about")
    ], [
        pyrogram.types.InlineKeyboardButton("➕️ Add To Your Channel ➕️",
                                            url=f"http://t.me/{bot.username}?startchannel=true")
    ]]
    return pyrogram.types.InlineKeyboardMarkup(buttons)

# Don't Remove Credit @AshutoshGoswami24
def about_buttons(bot, update):
    buttons = [[
        pyrogram.types.InlineKeyboardButton("🏠 Back To Home 🏠", callback_data="start")
    ]]
    return pyrogram.types.InlineKeyboardMarkup(buttons)

# Don't Remove Credit @AshutoshGoswami24
print("Bot Working ")
print("Bot Created By https://t.me/PandaWep")
# Don't Remove Credit @AshutoshGoswami24
Ashu.run()
# Don't Remove Credit @AshutoshGoswami24
# Don't Remove Credit @AshutoshGoswami24
