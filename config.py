import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "12936189")

API_HASH = os.environ.get("API_HASH", "7e24008e8ec33a397155b6a9d618497b")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6350447720:AAGotXZpcpTDbkPZv4n82THHgytcMizmR2E") 

FORCE_SUB = os.environ.get("FORCE_SUB", "") 

DB_NAME = os.environ.get("DB_NAME","Rename_test_bot")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://SoloLevling7seven:solo7@cluster0.4nolwkk.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1166670205').split()]

Bot_Username = "@Rename_robotbot"

PORT = os.environ.get('PORT', '8080')

String_Session  = "None"

Permanent_4gb = "-100XXX"
