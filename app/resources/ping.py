from flask_restful import Resource


class PingResource(Resource):
    def get(self):
        """
        Health check ping function
        :return: dict
        """
        return {"ping": "pong"}
