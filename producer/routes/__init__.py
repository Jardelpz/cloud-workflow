from flask_restful import Api

from resources.health_check import HealthCheckandler
from resources.sns_topic import SnsTopic


def init_routes(app):
    api = Api()

    api.add_resource(HealthCheckandler, '/health-check')
    api.add_resource(SnsTopic, '/user/publish')

    api.init_app(app)

