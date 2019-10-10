import redis


class RedisService:
    def __init__(self, config):
        self.redis_obj = redis.Redis(config["host"], config["port"])

    def hgetall(self, key: str) -> dict:
        """
        Calls redis hgetall with given key
        :param key: Key to search for
        :return: dict of key value pairs associated with given key
        """
        return self.redis_obj.hgetall(key)
