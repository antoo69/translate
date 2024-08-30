from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "7303980025:AAFj14nUqM_Lke--96RZyDPU7FlTIvsYJhg")

API_ID = int(os.environ.get("API_ID","29305295"))

API_HASH = os.environ.get("API_HASH", "6838cc67172f18fe5f302c158ce2fbfa")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "GTBot",
        bot_token=TOKEN,
        api_hash=API_HASH,
        api_id=API_ID,
        plugins=plugins
    )
    app.run()
