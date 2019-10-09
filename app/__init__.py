from flask import Flask
from flask_restful import Api

from app.config import Configdb
from app.db.redis_service import RedisService
from app.server import run

app = Flask(__name__)

app.config.from_object(Configdb)
api = Api(app)
db = RedisService(app.config["REDIS"])
run()
