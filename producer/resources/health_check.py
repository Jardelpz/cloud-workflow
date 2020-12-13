from flask_restful import Resource


class HealthCheckandler(Resource):

    def get(self):
        return "alive and kicking", 200