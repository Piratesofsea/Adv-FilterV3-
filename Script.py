class script(object):
    START_TXT = """๐แดสสแด {},

 ๐ ส ๐กแดแดแด ษช๐ vadivelu

๐จ'๐ ๐บ ๐ฅ๐๐๐พ๐๐ฝ๐๐ ๐๐๐๐๐ ๐ฌ๐บ๐๐บ๐๐พ๐ Bot
โข Build Version : V2.1.0 (BETA)
โข Speciality : Movie Provider
๐ข๐๐๐ผ๐ Help or /help ๐๐ ๐๐ ๐ฅ๐๐๐ผ๐๐๐๐๐."""
    HELP_TXT = """๐ท๐ด๐ {}
๐ท๐ด๐๐ด ๐ธ๐ ๐ผ๐ ๐ท๐ด๐ป๐ฟ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐."""
    ABOUT_TXT = """<b>โฅ My name: {}
โฅ Creator: <a href='https://t.me/The_user_death'>แดฉสแด๊ฐแด๊ฑแดส</a>
โฅ Library: Pyrogram
โฅ Language: Python ๐น
โฅ Data Base: MongoDB
โฅ Bot Server: Heroku
โฅ Build Status: v2.0.1 [ Beta ]"""
    DONATION_TXT = """<b>๐๐จ๐ง๐๐ญ๐ข๐จ๐ง & ๐๐๐ข๐ ๐๐ซ๐จ๐ฆ๐จ๐ญ๐ข๐จ๐ง</b> 

โบโบ <b>๐๐จ๐ง๐๐ญ๐ข๐จ๐ง</b>

โชผ <b>๐๐จ๐ฎ ๐๐๐ง ๐๐จ๐ง๐๐ญ๐ ๐๐ง๐ฒ ๐๐ฆ๐จ๐ฎ๐ง๐ญ ๐๐จ๐ฎ ๐๐๐ฏ๐ ๐ณ. 
<b>โโโโโโโโโแ Payment Methods แโโโโโโโโโ
- ๐๐ผ๐ผ๐ด๐น๐ฒ๐ฃ๐ฎ๐
- ๐ฃ๐ต๐ผ๐ป๐ฒ๐ฃ๐ฒ
_๐๐จ๐ง๐ญ๐๐๐ญ ๐๐ ๐๐จ๐ซ ๐๐ง๐จ๐ฐ ๐๐๐จ๐ฎ๐ญ ๐๐ก๐ ๐๐๐ฒ๐ฆ๐๐ง๐ญ ๐๐ง๐๐จ_
โโโโโโโโโโโโแ <a href=https://t.me/The_user_death><b>แดฉสแด๊ฐแด๊ฑแดส</b></a> แโโโโโโโโโโโโ

โบโบ <b>๐๐๐ข๐ ๐๐ซ๐จ๐ฆ๐จ๐ญ๐ข๐จ๐ง</b>

โชผ <b>๐๐จ๐ง๐ญ๐๐๐ญ ๐๐ ๐๐ข๐ญ๐ก ๐๐จ๐ฎ ๐๐จ๐ง๐ญ๐๐ง๐ญ ๐๐ก๐ข๐๐ก ๐๐จ๐ฎ ๐๐๐ง๐ญ ๐๐จ ๐๐ซ๐จ๐ฆ๐จ๐ญ๐ . 
<b>โโโโโโโโโแ Payment Methods แโโโโโโโโโ
- ๐๐ผ๐ผ๐ด๐น๐ฒ๐ฃ๐ฎ๐
- ๐ฃ๐ต๐ผ๐ป๐ฒ๐ฃ๐ฒ
_๐๐จ๐ง๐ญ๐๐๐ญ ๐๐ ๐๐ข๐ญ๐ก ๐๐จ๐ฎ๐ซ ๐๐จ๐ง๐ญ๐๐ง๐ญ ๐๐ง๐ ๐๐ง๐จ๐ฐ ๐๐๐จ๐ฎ๐ญ ๐๐ก๐ ๐๐๐ฒ๐ฆ๐๐ง๐ญ ๐๐ง๐๐จ_
โโโโโโโโโโโโแ <a href=https://t.me/The_user_death><b>แดฉสแด๊ฐแด๊ฑแดส</b></a> แโโโโโโโโโโโโ"""
    PROMOTION_TXT = """<b>ใ ๐๐๐ข๐ ๐๐ซ๐จ๐ฆ๐จ๐ญ๐ข๐จ๐ง ใ</b>

โชผ <b>๐๐จ๐ง๐ญ๐๐๐ญ ๐๐ ๐๐ข๐ญ๐ก ๐๐จ๐ฎ ๐๐จ๐ง๐ญ๐๐ง๐ญ ๐๐ก๐ข๐๐ก ๐๐จ๐ฎ ๐๐๐ง๐ญ ๐๐จ ๐๐ซ๐จ๐ฆ๐จ๐ญ๐ . 
<b>โโโโโโโโโแ Payment Methods แโโโโโโโโโ
- ๐๐ผ๐ผ๐ด๐น๐ฒ๐ฃ๐ฎ๐
- ๐ฃ๐ต๐ผ๐ป๐ฒ๐ฃ๐ฒ
_๐๐จ๐ง๐ญ๐๐๐ญ ๐๐ ๐๐ข๐ญ๐ก ๐๐จ๐ฎ๐ซ ๐๐จ๐ง๐ญ๐๐ง๐ญ ๐๐ง๐ ๐๐ง๐จ๐ฐ ๐๐๐จ๐ฎ๐ญ ๐๐ก๐ ๐๐๐ฒ๐ฆ๐๐ง๐ญ ๐๐ง๐๐จ_
โโโโโโโโโโโโแ <a href=https://t.me/The_user_death><b>แดฉสแด๊ฐแด๊ฑแดส</b></a> แโโโโโโโโโโโโ""" 
    FILE_TXT = """The Batch Module../

<b>.By Using This MODUL you Can Store Files In My DataBase AND I Will Give You A Permanent Link To Access The Saved Files. ๐ธ๐ต ๐๐พ๐ ๐๐ฐ๐ฝ๐ ๐๐พ ๐ฐ๐ณ๐ณ ๐ต๐ธ๐ป๐ด๐ ๐ต๐๐พ๐ผ ๐ฐ ๐ฟ๐๐ฑ๐ป๐ธ๐ฒ ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป ๐๐ด๐ฝ๐ณ ๐๐ท๐ด ๐ต๐ธ๐ป๐ ๐ป๐ธ๐ฝ๐บ ๐พ๐ฝ๐ป๐  ๐พ๐ ๐๐พ๐ ๐๐ฐ๐ฝ๐ ๐๐พ ๐ฐ๐ณ๐ณ ๐ต๐ธ๐ป๐ด๐ ๐ต๐๐พ๐ผ ๐ฐ  ๐ฟ๐๐ธ๐๐ฐ๐๐ด ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป ๐๐พ๐ ๐ผ๐๐๐ ๐ผ๐ฐ๐บ๐ด ๐ผ๐ด ๐ฐ๐ณ๐ผ๐ธ๐ฝ ๐พ๐ฝ ๐๐ท๐ด ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป ๐๐พ ๐ฐ๐ฒ๐ฒ๐ด๐๐ ๐ต๐ธ๐ป๐ด๐.</b>
โชผ Commands

โช /plink โบโบ <b>Reply To Any Media To Get The Link .</b>
โช /pbatch โบโบ <b>Use Your Media Link With This Command .</b>
โช /batch โบโบ <b>๐๐พ ๐ฒ๐๐ด๐ฐ๐๐ด ๐ป๐ธ๐ฝ๐บ ๐ต๐พ๐ ๐ผ๐๐ป๐๐ธ๐ฟ๐ป๐ด ๐ต๐ธ๐ป๐ด๐.</b>

โชผ ๐๐ฑ๐๐ฆ๐ฉ๐ฅ๐ โบ

<code>/batch https://t.me/FPHDMOVE/3 https://t.me/FPHDMOVE/8</code>
"""
    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- Give a user details
โข/whois :-give a user full details"""
    FUN_TXT ="""<b>Gแดแดแดs</b> 
    
<b>Some dank for fun or whatever!</b>
 
๐ฃ. /dice - Role The Dice
๐ค. /Throw ๐๐ /Dart - To Make Dart
3. /Runs - Some Random Dialogues
4. /Goal or /Shoot - To Make A Goal Or Shoot
5. /luck or /cownd - Spin And Try Your Luck"""
    DEPLOY_TXT = """ ๐ Sorry bro """
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and แฉแแฉแญ  will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    SONG_TXT = """<b>๐๐พ๐ฝ๐ถ ๐ณ๐พ๐๐ฝ๐ป๐พ๐ฐ๐ณ ๐ผ๐พ๐ณ๐๐ป๐ด</b>

<b>๐๐พ๐ฝ๐ถ ๐ณ๐พ๐๐ฝ๐ป๐พ๐ฐ๐ณ ๐ผ๐พ๐ณ๐๐ป๐ด, ๐ต๐พ๐ ๐๐ท๐พ๐๐ด ๐๐ท๐พ ๐ป๐พ๐๐ด ๐ผ๐๐๐ธ๐ฒ. ๐๐พ๐ ๐ฒ๐ฐ๐ฝ ๐๐๐ด ๐๐ท๐ธ๐ ๐ต๐ด๐ฐ๐๐๐ด ๐ต๐พ๐ ๐ณ๐พ๐๐ฝ๐ป๐พ๐ฐ๐ณ ๐ฐ๐ฝ๐ ๐๐พ๐ฝ๐ถ ๐๐ธ๐๐ท ๐๐๐ฟ๐ด๐ ๐ต๐ฐ๐๐ ๐๐ฟ๐ด๐ด๐ณ.๐๐พ๐๐บ๐ ๐พ๐ฝ๐ป๐ ๐พ๐ฝ ๐ถ๐๐พ๐๐ฟ๐../</b>

<b>๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐</b>

โบโบ  /song ๐๐พ๐ฝ๐ถ ๐ฝ๐ฐ๐ผ๐ด 

๐๐พ๐๐บ๐ ๐พ๐ฝ๐ป๐ ๐พ๐ฝ ๐ถ๐๐พ๐๐ฟ

๐ฒ๐๐ด๐ณ๐ธ๐๐ :- <a href=https://t.me/The_user_death>แดฉสแด๊ฐแด๊ฑแดส</a>"""
    PIN_TXT ="""<b>PIN MODULE</b>
<b>๐ฟ๐ธ๐ฝ ๐ฐ ๐ผ๐ด๐๐๐ฐ๐ถ๐ด../</b>

<b>๐ฐ๐ป๐ป ๐๐ท๐ด ๐ฟ๐ธ๐ฝ ๐๐ด๐ป๐ฐ๐๐ด๐ณ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐ ๐ฒ๐ฐ๐ฝ ๐ฑ๐ด ๐ต๐พ๐๐ฝ๐ณ ๐ท๐ด๐๐ด::</b>

<b>๐๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐ ๐ฐ๐ฝ๐ณ ๐๐๐ฐ๐ถ๐ด๐</b>

โ /pin :- ๐๐พ ๐ฟ๐ธ๐ฝ ๐๐ท๐ด ๐ผ๐ด๐๐๐ฐ๐ถ๐ด ๐พ๐ฝ ๐๐พ๐๐ ๐ฒ๐ท๐ฐ๐๐
โ /unpin :- ๐๐พ ๐๐ฝ๐ฟ๐ธ๐ฝ ๐๐ท๐ด ๐ฒ๐๐๐๐ด๐ด๐ฝ๐ ๐ฟ๐ธ๐ฝ๐ฝ๐ด๐ณ ๐ผ๐ด๐๐ฐ๐ฐ๐ถ๐ด"""
    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>

โข /paste [text] - paste the given text on Pasty

<b>NOTE:</b>

โข These commands works on both pm and group.
โข These commands can be used by any group member."""
    TTS_TXT = """Help: <b> TTS ๐ค module:</b>

Translate text to speech

<b>Commands and Usage:</b>

โข /tts <text> : convert text to speech

<b>NOTE:</b>

โข IMDb should have admin privillage.
โข These commands works on both pm and group.
โข IMDb can translate texts to 200+ languages."""
    PINGS_TXT ="""<b>๐ Ping:</b>

- /pings - To know your pings

โข This commands can be used in pms and groups
โข This commands can be used buy everyone in the groups and bots pm
โข Share us for more features"""
    TELE_TXT = """<b>โซ๏ธHELP: Telegraphโช๏ธ</b>

Do as you wish with telegra.ph module!

</b>USAGE:</b>

๐คง /telegraph - Send me Picture or Vide Under (5MB)

<b>NOTE:</b>

โข This Command Is Available in goups and pms
โข This Command Can be used by everyone"""

    PRIVATEBOT_TXT = """<b>๐ฟ๐๐ธ๐๐ฐ๐๐ด ๐ฑ๐พ๐ ๐ต๐พ๐ ๐๐พ๐</b>
<b>โบโบ ๐ณ๐พ ๐๐พ๐ ๐๐ฐ๐ฝ๐ ๐ฐ ๐ฑ๐พ๐ ๐๐ฐ๐ผ๐ด ๐ป๐ธ๐บ๐ด ๐๐ท๐ธ๐</b>
<b>โบโบ ๐๐ธ๐๐ท ๐ฐ๐ป๐ป ๐๐พ๐๐ ๐ฒ๐๐ด๐ณ๐ธ๐๐</b>
<b>โบโบ ๐๐ธ๐๐ท ๐๐พ๐๐ ๐พ๐๐ฝ๐ด๐๐๐ท๐ธ๐ฟ</b>
<b>โบโบ ๐ฒ๐พ๐ฝ๐๐ฐ๐ฒ๐ ๐ผ๐ด <a href=https://t.me/The_user_death>แดฉสแด๊ฐแด๊ฑแดส</a></b>"""

    JSON_TXT ="""<b>JSON:</b>

Bot returns json for all replied messages with /json

<b>Features:</b>

Message Editting JSON
Pm Support
Group Support

<b>Note:</b>

Everyone can use this command , if spaming happens bot will automatically ban you from the group."""
    PURGE_TXT = """<b>Purge</b>
    
Delete A Lot Of Messages From Groups! 
    
 <b>ADMIN</b> 

โ /purge :- Delete All Messages From The Replied To Message, To The Current Message"""
    BUTTON_TXT = """Help: <b>Buttons</b>

-this bot  Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. This bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/MWUpdatez)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """<b>๐ฐ๐๐๐พ ๐ต๐ธ๐ป๐๐ด๐ ๐พ๐ฝ/๐พ๐ต๐ต ๐ผ๐พ๐ณ๐๐ป๐ด..</b>

<b>๐ฐ๐๐๐พ ๐ต๐ธ๐ป๐๐ด๐ ๐ธ๐ ๐๐ท๐ด ๐ต๐ด๐ฐ๐๐๐๐ด ๐๐พ ๐ต๐ธ๐ป๐๐ด๐ ๐ฐ๐ฝ๐ณ ๐๐ฐ๐๐ด  ๐๐ท๐ด ๐ต๐ธ๐ป๐ด๐ ๐ฐ๐๐๐พ๐ผ๐ฐ๐๐ธ๐ฒ๐ฐ๐ป๐ป๐ ๐ต๐๐พ๐ผ ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป ๐๐พ ๐ถ๐๐พ๐๐ฟ. ๐๐พ๐ ๐ฒ๐ฐ๐ฝ ๐๐๐ด ๐๐ท๐ด ๐ต๐พ๐ป๐ป๐พ๐๐ธ๐ฝ๐ถ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐ ๐๐พ ๐พ๐ฝ ๐ฐ๐ฝ๐ณ ๐พ๐ต๐ต ๐๐ท๐ด ๐ฐ๐๐๐พ๐ต๐ธ๐ป๐๐ด๐ ๐ธ๐ฝ ๐๐พ๐๐ ๐ถ๐๐พ๐๐ฟ.../</b>

<b>๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐ :-
<b>โบโบ /autofilter on - ๐ด๐ฝ๐ฐ๐ฑ๐ป๐ด ๐ฐ๐๐๐พ ๐ต๐ธ๐ป๐๐ด๐ ๐ธ๐ฝ ๐๐ท๐ด ๐ถ๐๐พ๐๐ฟ๐.</b>
<b>โบโบ /autofilter off - ๐ณ๐ธ๐๐ฐ๐ฑ๐ป๐ด๐ณ ๐ฐ๐๐๐พ ๐ต๐ธ๐ป๐๐ด๐ ๐ธ๐ฝ ๐๐ท๐ด ๐ถ๐๐พ๐๐ฟ๐.</b>
<b>โบโบ /set_template - ๐๐ด๐ ๐ฒ๐๐๐๐พ๐ผ ๐ธ๐ผ๐ณ๐ฑ ๐๐ด๐ผ๐ฟ๐ป๐ฐ๐๐ด ๐ต๐พ๐ ๐ฐ๐๐๐พ ๐ต๐ธ๐ป๐๐ด๐.</b>
<b>โบโบ /get_template - ๐ถ๐ด๐ ๐ฒ๐๐๐๐ด๐ฝ๐ ๐ธ๐ผ๐ณ๐ฑ ๐๐ด๐ผ๐ฟ๐ป๐ฐ๐๐ด ๐พ๐ต ๐ฐ๐๐๐พ ๐ต๐ธ๐ป๐๐ด๐.</b>

<b>๐ฒ๐๐ด๐ณ๐ธ๐๐ :- <a href=https://t.me/The_user_death>แดฉสแด๊ฐแด๊ฑแดส</a></b>"""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    SEARCH_TXT = """Help: <b>IMDb</b>
Search many things without leaving telegram!
<b>Commands and Usage:</b>
โข /imdb  - get the film information from IMDb source.
โข /search  - get the film information from various sources.
<b>NOTE:</b>
โข BOT should have admin privillage.
โข More search tools can be found on inline.
โข Those commands works on both pm and group."""
    INFO_TXT = """Help: <b>Information</b>
Get information about something!
<b>Commands and Usage:</b>
โข /id - get id of a specified user.
โข /info  - get information about a user.
โข /json - get the json details of a message.
<b>NOTE:</b>
โข Bot should have admin privillage.
โข These commands works on both pm and group.
โข These commands can be used by any group member."""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /delete - <code>to delete a specific file from db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban_user  - <code>to ban a user.</code>
โข /unban_user  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>แโบ ๐๐พ๐๐ฐ๐ป ๐ต๐ธ๐ป๐ด๐: <code>{}</code></b>
<b>แโบ ๐๐พ๐๐ฐ๐ป ๐๐๐ด๐๐: <code>{}</code></b>
<b>แโบ ๐๐พ๐๐ฐ๐ป ๐ฒ๐ท๐ฐ๐๐: <code>{}</code></b>
<b>แโบ ๐๐๐ด๐ณ ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> </b>
<b>แโบ ๐ต๐๐ด๐ด ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> </b>"""
    LOG_TEXT_G = """#๐๐๐ฐ๐๐ซ๐จ๐ฎ๐ฉ
    
<b>แโบ ๐๐ซ๐จ๐ฎ๐ฉ โชผ {}(<code>{}</code>)</b>
<b>แโบ ๐๐จ๐ญ๐๐ฅ ๐๐๐ฆ๐๐๐ซ๐ฌ โชผ <code>{}</code></b>
<b>แโบ ๐๐๐๐๐ ๐๐ฒ โชผ {}</b>
"""
    LOG_TEXT_P = """#๐๐๐ฐ๐๐ฌ๐๐ซ
    
<b>แโบ ๐๐ - <code>{}</code></b>
<b>แโบ ๐๐๐ฆ๐ - {}</b>
"""
    REPORT_TXT = """โค ๐๐๐ฅ๐ฉ: Rแดแดแดสแด โ ๏ธ

๐๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐๐ ๐ข๐๐ ๐๐ ๐๐๐๐๐๐ ๐ ๐๐๐๐๐๐๐ ๐๐ ๐ ๐๐๐๐ ๐๐ ๐๐๐ ๐๐๐๐๐๐ ๐๐ ๐๐๐ ๐๐๐๐๐๐๐๐๐๐ ๐๐๐๐๐. ๐ณ๐๐'๐ ๐๐๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐๐๐.

โค ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐:

โช/report ๐๐ @admins - ๐ณ๐ ๐๐พ๐๐๐๐ ๐บ ๐๐๐พ๐ ๐๐ ๐๐๐พ ๐บ๐ฝ๐๐๐๐ (๐๐พ๐๐๐ ๐๐ ๐บ ๐๐พ๐๐๐บ๐๐พ)."""

    CORONA_TXT = """โค ๐๐๐ฅ๐ฉ: ๐ข๐๐๐๐ฝ

๐๐๐๐ ๐ฒ๐๐๐๐๐๐ ๐๐๐๐๐ ๐ข๐๐ ๐๐ ๐๐๐๐  ๐๐๐๐๐ข ๐๐๐๐๐๐๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐ 

โค ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐:

โช /covid - ๐๐๐พ ๐๐๐๐ ๐ผ๐๐๐๐บ๐๐ฝ ๐๐๐๐ ๐๐๐๐ ๐ผ๐๐๐๐๐๐ ๐๐บ๐๐พ ๐๐ ๐๐พ๐ ๐ผ๐๐๐๐ฝ๐พ ๐๐๐ฟ๐๐๐๐บ๐๐๐๐

โ๐ค๐๐บ๐๐๐๐พ:
<code>/covid ๐จ๐๐ฝ๐๐บ</code>"""

    URLSHORT_TXT = """โค ๐๐๐ฅ๐ฉ: ๐ด๐๐ ๐๐๐๐๐๐๐พ๐

๐๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐๐ ๐ข๐๐ ๐๐ ๐๐๐๐๐ ๐ ๐๐๐ 

โค ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐:

โช /short: ๐๐๐พ ๐๐๐๐ ๐ผ๐๐๐๐บ๐๐ฝ ๐๐๐๐ ๐๐๐๐ ๐๐๐๐ ๐๐ ๐๐พ๐ ๐๐๐๐๐๐พ๐ฝ ๐๐๐๐๐

โ๐ค๐๐บ๐๐๐๐พ:
<code>/short https://youtu.be/AB9CdEfG8ch0</code>"""

    VIDEO_TXT ="""๐ท๐ด๐ป๐ฟ ๐๐พ๐ ๐๐พ ๐ณ๐พ๐๐ฝ๐ป๐พ๐ฐ๐ณ ๐๐ธ๐ณ๐ด๐พ ๐ต๐๐พ๐ผ ๐๐พ๐๐๐๐ฑ๐ด.

โข ๐๐ด๐ข๐จ๐ฆ
๐ ๐ฐ๐ถ ๐๐ข๐ฏ ๐๐ฐ๐ธ๐ฏ๐ญ๐ฐ๐ข๐ฅ ๐๐ฏ๐บ ๐๐ช๐ฅ๐ฆ๐ฐ ๐๐ณ๐ฐ๐ฎ ๐ ๐ฐ๐ถ๐ต๐ถ๐ฃ๐ฆ

๐๐ค๐ฌ ๐๐ค ๐๐จ๐
โข ๐๐บ๐ฑ๐ฆ /video or /mp4 ๐๐ฏ๐ฅ (https://youtu.be/AB9CdEfG8ch0)
โข ๐๐น๐ข๐ฎ๐ฑ๐ญ๐ฆ:
<code>/mp4 https://youtu.be/AB9CdEfG8ch0</code>
<code>/video https://youtu.be/AB9CdEfG8ch0</code>"""

    ZOMBIES_TXT = """๐ท๐ด๐ป๐ฟ ๐๐พ๐ ๐๐พ ๐บ๐ธ๐ฒ๐บ ๐๐๐ด๐๐

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
โข /inkick - command with required arguments and i will kick members from group.
โข /instatus - to check current status of chat member from group.
โข /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
โข /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
โข /dkick - to kick deleted accounts."""

    IMAGE_TXT = """โค ๐๐๐ฅ๐ฉ: Iแดแดษขแด

๐๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐๐ ๐ข๐๐ ๐๐ ๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐ข ๐๐๐๐๐๐ข 

โค ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐:

โช ๐ฉ๐๐๐ ๐๐พ๐๐ฝ ๐๐พ ๐บ ๐๐๐บ๐๐พ ๐๐ ๐พ๐ฝ๐๐ โจ

๐ฌ๐บ๐ฝ๐พ ๐ป๐ <a href=https://t.me/The_user_death>แดฉสแด๊ฐแด๊ฑแดส</a>"""

    STICKER_TXT = """๐๐พ๐ ๐ฒ๐ฐ๐ฝ ๐๐๐ด ๐๐ท๐ธ๐ ๐ผ๐พ๐ณ๐๐ป๐ด ๐๐พ ๐ต๐ธ๐ฝ๐ณ ๐ฐ๐ฝ๐ ๐๐๐ธ๐ฒ๐บ๐ด๐๐ ๐ธ๐ณ.
โข ๐๐๐๐๐
To Get Sticker ID
 
๐๐ค๐ฌ ๐๐ค ๐๐จ๐
 
โ Reply To Any Sticker [/stickerid]"""

    YTTHUMB_TXT = """๐ท๐ด๐ป๐ฟ๐ ๐๐พ ๐ณ๐พ๐๐ฝ๐ป๐พ๐ฐ๐ณ ๐ฐ๐ฝ๐ ๐๐พ๐๐๐๐ฑ๐ด ๐๐ธ๐ณ๐ด๐พ ๐๐ท๐๐ผ๐ฑ๐ฝ๐ฐ๐ธ๐ป
    
๐๐ค๐ฌ ๐๐ค ๐๐จ๐
๐๐บ๐ฑ๐ฆ /ytthumb ๐๐ฏ๐ฅ ๐๐ช๐ฅ๐ฆ๐ฐ ๐๐ช๐ฏ๐ฌ

โข ๐๐น๐ข๐ฎ๐ฑ๐ญ๐ฆ
<code>/ytthumb https://youtu.be/AB9CdEfG8ch0</code>"""

    ABOOK_TXT = """โค ๐๐๐ฅ๐ฉ: ๐ ๐๐ฝ๐๐๐ป๐๐๐

๐๐๐ ๐๐๐ ๐๐๐๐๐๐๐ ๐ ๐ฟ๐ณ๐ต ๐๐๐๐ ๐๐ ๐ ๐๐๐๐๐ ๐๐๐๐ ๐ ๐๐๐ ๐๐๐๐ ๐๐๐๐๐๐๐ โฏ

โค ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐:

โช /audiobook: ๐ฑ๐พ๐๐๐ ๐๐๐๐ ๐ผ๐๐๐๐บ๐๐ฝ ๐๐ ๐บ๐๐ ๐ฏ๐ฃ๐ฅ ๐๐ ๐๐พ๐๐พ๐๐บ๐๐พ ๐๐๐พ ๐บ๐๐ฝ๐๐"""

    GTRANS_TXT = """โค ๐๐๐ฅ๐ฉ: ๐ฆ๐๐๐๐๐พ ๐ณ๐๐บ๐๐๐๐บ๐๐พ๐

๐๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐๐ ๐ข๐๐ ๐๐ ๐๐๐๐๐๐๐๐๐ ๐ ๐๐๐ก๐ ๐๐ ๐บ๐๐ ๐๐๐๐๐๐๐๐๐ ๐ข๐๐ ๐ ๐๐๐. ๐๐๐๐ ๐๐๐๐๐๐๐ ๐ ๐๐๐๐ ๐๐ ๐๐๐๐ ๐๐ ๐๐๐ ๐๐๐๐๐ โฏ

โค ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐:

โช/tr - ๐ณ๐ ๐๐๐บ๐๐๐๐บ๐๐พ๐ ๐๐พ๐๐๐ ๐๐ ๐บ ๐๐๐พ๐ผ๐๐ฟ๐ผ ๐๐บ๐๐๐๐บ๐๐พ

โค ๐ญ๐๐๐พ:
๐ถ๐๐๐๐พ ๐๐๐๐๐ /tr ๐๐๐ ๐๐๐๐๐๐ฝ ๐๐๐พ๐ผ๐๐ฟ๐ ๐๐๐พ ๐๐บ๐๐๐๐บ๐๐พ ๐ผ๐๐ฝ๐พ

โ๐ค๐๐บ๐๐๐๐พ: /๐๐ ๐๐
โข ๐พ๐ = ๐ค๐๐๐๐๐๐
โข ๐๐ = ๐ฌ๐บ๐๐บ๐๐บ๐๐บ๐
โข ๐๐ = ๐ง๐๐๐ฝ๐"""

    ALIVE_TXT = """ALIVE MOD
โข /alive - check me alive or dead๐คง
Just for a rasam๐"""

    GROUP_TXT = """๐ง๐พ๐๐พ ๐๐ ๐๐๐พ ๐ด๐๐๐บ๐ ๐ผ๐๐๐๐บ๐๐ฝ๐:"""

    CHANNEL_TXT = """๐ง๐พ๐๐พ ๐๐ ๐๐๐พ ๐ด๐๐๐บ๐ ๐ผ๐๐๐๐บ๐๐ฝ๐:"""

    MAIN_TXT = """๐ง๐พ๐๐พ ๐๐ ๐๐๐พ ๐ด๐๐๐บ๐ ๐ผ๐๐๐๐บ๐๐ฝ๐:"""

    FILTER_TXT = """๐ง๐พ๐๐พ ๐๐ ๐๐๐พ ๐ด๐๐๐บ๐ ๐ผ๐๐๐๐บ๐๐ฝ๐:"""

    NE_TXT = """๐ง๐พ๐๐พ ๐๐ ๐๐๐พ ๐ด๐๐๐บ๐ ๐ผ๐๐๐๐บ๐๐ฝ๐:"""

    NEX_TXT = """๐ง๐พ๐๐พ ๐๐ ๐๐๐พ ๐ด๐๐๐บ๐ ๐ผ๐๐๐๐บ๐๐ฝ๐:"""

    EXTRA_TXT = """Extra Modulbot
NOTE:
these are the extra features of this bot
"""

    MOD_TXT = """
๐ง๐พ๐๐พ ๐๐ ๐๐๐พ ๐ด๐๐๐บ๐ ๐ผ๐๐๐๐บ๐๐ฝ๐:
"""

    NXE_TXT = """
๐ง๐พ๐๐พ ๐๐ ๐๐๐พ ๐ด๐๐๐บ๐ ๐ผ๐๐๐๐บ๐๐ฝ๐:
"""

    COR_TXT = """Creators โค
- Thanks To Dan For His Awesome Library
- Thanks To Mahesh For His Awesome Media-Search-bot
- Thanks To <a href='https://github.com/trojanzhex'>Trojanz</a> for Their Awesome Unlimited Filter Bot And AutoFilterBoT
- Thanks To <a href='https://t.me/TeamEvamaria'>Eva Mari Team</a> A amazing combination of this repo
- Thanks To <a href='https://t.me/Aadhi011'>Aadhi</a> For Creating Extra featurs 
- Thanks To <a href='https://t.me/sangeeth006'>Sangeeth</a> To create me 
- Thanks To All Everyone In This Journey"""

    RESTRIC_TXT = """โค ๐๐๐ฅ๐ฉ: Mแดแดแด ๐ซ

๐๐๐๐๐ ๐๐๐ ๐๐๐ ๐๐๐๐๐๐๐๐ ๐ ๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐ ๐๐๐ ๐๐ ๐๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐๐๐๐๐๐๐ข.

โช/ban: ๐ณ๐ ๐ป๐บ๐ ๐บ ๐๐๐พ๐ ๐ฟ๐๐๐ ๐๐๐พ ๐๐๐๐๐.
โช/unban: ๐ณ๐ ๐๐๐ป๐บ๐ ๐บ ๐๐๐พ๐ ๐๐ ๐๐๐พ ๐๐๐๐๐.
โช/tban: ๐ณ๐ ๐๐พ๐๐๐๐๐บ๐๐๐๐ ๐ป๐บ๐ ๐บ ๐๐๐พ๐.
โช/mute: ๐ณ๐ ๐๐๐๐พ ๐บ ๐๐๐พ๐ ๐๐ ๐๐๐พ ๐๐๐๐๐.
โช/unmute: ๐ณ๐ ๐๐๐๐๐๐พ ๐บ ๐๐๐พ๐ ๐๐ ๐๐๐พ ๐๐๐๐๐.
โช/tmute: ๐ณ๐ ๐๐พ๐๐๐๐๐บ๐๐๐๐ ๐๐๐๐พ ๐บ ๐๐๐พ๐.

โค ๐ญ๐๐๐พ:
๐ถ๐๐๐๐พ ๐๐๐๐๐ /tmute ๐๐ /tban ๐๐๐ ๐๐๐๐๐๐ฝ ๐๐๐พ๐ผ๐๐ฟ๐ ๐๐๐พ ๐๐๐๐พ ๐๐๐๐๐.

โ๐ค๐๐บ๐๐๐๐พ: /๐๐ป๐บ๐ 2๐ฝ ๐๐ /๐๐๐๐๐พ 2๐ฝ.
๐ธ๐๐ ๐ผ๐บ๐ ๐๐๐พ ๐๐บ๐๐๐พ๐: ๐/๐/๐ฝ. 
 โข ๐ = ๐๐๐๐๐๐พ๐
 โข ๐ = ๐๐๐๐๐
 โข ๐ฝ = ๐ฝ๐บ๐๐"""
    CREATOR_REQUIRED = """โ<b>You have To Be The Group Creator To Do That.</b>"""
      
    INPUT_REQUIRED = "โ **Arguments Required**"
      
    KICKED = """โ๏ธ Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """๐ฎ Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """โ<b>เดเดจเตเดจเต Admin เดเดเตเดเดคเตเดค เดธเตเดฅเดฒเดคเตเดคเต เดเดพเตป เดจเดฟเดเตเดเดฟเดฒเตเดฒ เดชเตเดเตเดตเดพ Bii..Add Me Again with all admin rights.</b>"""
      
    DKICK = """โ๏ธ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>เดเดชเตเดชเต เดเดฒเตเดฒเดพเด เดเดเดฟเดเตเดเตเดฎเดพเดฑเตเดฑเดฟ เดคเดฐเดพเด...</b>"""
      
    STATUS = """{}\n<b>Chat Member Status</b>**\n\n```<i>Recently``` - {}\n```Within Week``` - {}\n```Within Month``` - {}\n```Long Time Ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}</i>
"""
