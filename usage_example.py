from anything_db import get, set, where
from anything_db.social_media.telegram_db import Telegram

from config import *
from datetime import datetime

db = Telegram(
    API_KEY = API_KEY, API_HASH = API_HASH,
)
db.initialize()


start = datetime.now()
posts = get(db, "posts/Jason", where("case", "==", "dead"))
for post in posts:
    print(post.text)

    print("---------------------------1")
posts = get(db, "posts/Jason")
for post in posts:
    print(post.text)
    print("---------------------------2")

posts = get(db, "posts/Jason", where("case", "==", "dead"))
for post in posts:
    print(post.text)
    print("---------------------------3")

# set(db, "posts/Jason", {"title": "Montroe"})


print(f"Time taken: {datetime.now() - start}")