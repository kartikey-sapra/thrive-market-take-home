from app import api
from app.resources.ping import PingResource
from app.resources.recommendation import RecommendationResource

api.add_resource(RecommendationResource, '/recs')
api.add_resource(PingResource, '/ping')