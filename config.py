from os import environ 

class Config:
    API_ID = environ.get("API_ID", "24253579")
    API_HASH = environ.get("API_HASH", "55773656b8e938d38ea528f26a29a2b3")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7098087706:AAGonnIfgOXiGvKTd9YuRswFJu7WV0cVATI") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://forward48:aaaa11@forward48.uyixyw1.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5311861748').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
