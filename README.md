# AnythingDB

AnythingDB is a flexible, extensible database tool that allows you to use "anything" as a database. Whether it's Telegram, files, APIs, or even custom data sources, AnythingDB abstracts the complexity of managing different data sources and provides a simple interface for CRUD operations.

## Features

- **Simple API** for interacting with various types of databases.
- **Support for Telegram** and other social media as a data source.
- **Dynamic querying** with `where` filters for selecting specific data.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/anything_db.git
    cd anything_db
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the configuration:
    - Create a `config.py` file in the project root.
    - Add your Telegram API keys:

    ```python
    API_KEY = "your-telegram-api-key"
    API_HASH = "your-telegram-api-hash"
    ```

## Usage

Here’s an example showing how to interact with AnythingDB using Telegram as a database.

### Example

```python
from anything_db import get, set, where
from anything_db.social_media.telegram_db import Telegram
from config import API_KEY, API_HASH
from datetime import datetime

# Initialize the Telegram database
db = Telegram(API_KEY=API_KEY, API_HASH=API_HASH)
db.initialize()

# Track start time for performance monitoring
start = datetime.now()

# Fetch posts where the "case" field equals "dead"
posts = get(db, "posts/Jason", where("case", "==", "dead"))
for post in posts:
    print(post.text)
    print("---------------------------1")

# Fetch all posts from "posts/Jason"
posts = get(db, "posts/Jason")
for post in posts:
    print(post.text)
    print("---------------------------2")

# Fetch posts with a specific filter again
posts = get(db, "posts/Jason", where("case", "==", "dead"))
for post in posts:
    print(post.text)
    print("---------------------------3")

# Optionally, update a post
# set(db, "posts/Jason", {"title": "Montroe"})

# Output the time taken to execute the code
print(f"Time taken: {datetime.now() - start}")
