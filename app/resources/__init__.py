from app import api
from app.resources.ping import PingResource
from app.resources.recommendation import RecommendationResource

# Add Resources to API
api.add_resource(RecommendationResource, '/recs')
api.add_resource(PingResource, '/ping')