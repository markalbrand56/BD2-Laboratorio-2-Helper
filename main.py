import dotenv
import os

from mongo_conn import MongoConn
from random_user_generator import get_random_user

dotenv.load_dotenv()
URI = os.getenv("URI")

mongo_conn = MongoConn(URI, "lab02_atlas", "usuarios")
mongo_conn.connect()

current_size = mongo_conn.get_collection_size()
users_needed = 100000 - current_size

for i in range(5):
    user = get_random_user()
    print(user)
    # mongo_conn.collection.insert_one(user)