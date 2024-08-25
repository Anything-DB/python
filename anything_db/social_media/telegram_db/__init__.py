from pyrogram import Client
from datetime import datetime
from typing import List
import string, random

class Chat:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.id = None
    
    def __str__(self):
        return f"{self.title} - {self.description}"

class Telegram:
    def __init__(self, API_KEY, API_HASH):
        self.API_KEY = API_KEY
        self.API_HASH = API_HASH

    def initialize(self):
        try:
            self.app = Client("social_database", api_id=self.API_KEY, api_hash=self.API_HASH)

            self.tables = {}
            self.last_update = None
            
            self.app.start()  # Start the client
            self.channels = self.show_tables()

            print("Connected!")
            return True
        except Exception as e:
            print(f"Failed to initialize Telegram client: {e}")
            return False
        
    def show_tables(self) -> List[str]:
        # Returns created channels list that end with _db
        if self.last_update and (datetime.now() - self.last_update).total_seconds() < 60:
            return self.tables  # Return the cached channels list

        # Fetch new channels list from Telegram and update self.tables
        try:
            dialogs = self.app.get_dialogs()
            db_channels = [chat for chat in dialogs if chat.chat.title and chat.chat.title.endswith('_db')]

            for channel in db_channels:
                title = channel.chat.title[:-3]  # Assuming `_db` suffix exists
                new_chat = Chat(channel.chat.title, channel.chat.description)
                new_chat.id = channel.chat.id
                self.tables[title] = new_chat  # Add new channel to the list of channels

            # Set self.last_update timestamp
            self.last_update = datetime.now()
        except Exception as e:
            print(f"Failed to fetch channels: {e}")

        return self.tables
        
    def create_table(self, table_name, table_description=""):
        if table_name not in self.channels:
            try:
                self.app.create_channel(f"{table_name}_db", table_description)
                # After creating, update the channels list
                self.show_tables()
            except Exception as e:
                print(f"Failed to create channel: {e}")

    def get(self, path, *args, **kwargs):
        chat, data_id = path.split("/", 1)

        if chat not in self.tables:
            return None
        
        search = f"{data_id}; {''.join(args)}"

        try:
            results = self.app.search_messages(self.tables[chat].id, search)
            for row in results:
                yield row
        except Exception as e:
            print(f"Error while searching messages: {e}")

    def set(self, path, data_json, **kwargs):
        chat, data_id = path.split("/", 1)

        if chat not in self.tables:
            print("Chat not found")
            return

        if not data_id:
            data_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

        message = data_id + "\n"
        message += "\n".join([f"{key}: {value}" for key, value in data_json.items()])

        try:
            self.app.send_message(self.tables[chat].id, message)
        except Exception as e:
            print(f"Failed to send message: {e}")