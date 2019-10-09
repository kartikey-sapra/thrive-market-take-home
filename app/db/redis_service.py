import redis


class RedisService:
    def __init__(self, config):
        self.redis_obj = redis.Redis(config["host"], config["port"])

    def hgetall(self, key):
        return self.redis_obj.hgetall(key)
