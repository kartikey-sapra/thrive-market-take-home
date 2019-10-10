from flask import request, jsonify
from flask_restful import Resource

from app import db


class RecommendationResource(Resource):
    PREFIX = "prod_id_"

    def __get_key(self, k):
        return self.PREFIX + str(k)

    def get(self):
        """
           Get recommendation for the given product id
           :return: dict: status, message, data -> list of recommended products
        """
        product_id = request.args.get('productid')
        if product_id is None or product_id == "":
            response_d = {"status": 500, "message": "Error", "data": []}
            return jsonify(response_d)

        try:
            key = self.__get_key(product_id)
            recommendation_dict = db.hgetall(key)

            if recommendation_dict is None or len(recommendation_dict) == 0:
                response_d = {"status": 404, "message": "Error", "data": []}
            else:
                recommended_ids = [int(k) for k in recommendation_dict.keys()]
                message = "recommendations for PID : %s" % product_id
                response_d = {"status": 200, "message": message, "data": recommended_ids}
        except Exception as e:
            print(e)
            response_d = {"status": 500, "message": "Error", "data": []}

        return response_d
