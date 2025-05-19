import os

DECAY_RATE = 0.001
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = 6379
REDIS_DB = 0
TRENDING_KEY = "articles:trending"
