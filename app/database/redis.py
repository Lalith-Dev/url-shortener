"""
before the docker redis setup, we can use this code to connect to a local redis instance.
# import redis

# redis_client = redis.Redis(
#     host="localhost",
#     port=6379,
#     db=0,
#     decode_responses=True
# )

"""


import redis
import os

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=6379,
    db=0,
    decode_responses=True
)