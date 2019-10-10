import os


class Config(object):
    DEBUG = False


class Configdb(Config):
    REDIS = {"host": os.environ.get('REDIS_HOST') or "redis",
             "port": os.environ.get('REDIS_PORT') or 6379
             }
