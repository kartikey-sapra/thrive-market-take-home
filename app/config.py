import os


class Config(object):
    DEBUG = False


class Configdb(Config):
    REDIS = {"host": os.environ.get('DATABASE_USER') or "redis",
                  "port": os.environ.get('DATABASE_USER') or 6379
                  }
