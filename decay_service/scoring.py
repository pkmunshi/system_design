import math
import time
import redis
from constants import DECAY_RATE, REDIS_HOST, REDIS_PORT, REDIS_DB

# Redis connection
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

def decayed_score(weight: float, timestamp: int, now: int, decay_rate: float = DECAY_RATE) -> float:
    elapsed = now - timestamp
    return weight * math.exp(-decay_rate * elapsed)

def add_event(key: str, item_id: str, event_time: int, weight: float = 1.0):
    now = int(time.time())
    score = decayed_score(weight, event_time, now)
    r.zadd(key, {item_id: score})

def get_trending(key: str, count: int = 10):
    return r.zrevrange(key, 0, count - 1, withscores=True)
