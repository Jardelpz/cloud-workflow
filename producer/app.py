from flask import Flask
from flask_cors import CORS

from routes import init_routes

app = Flask(__name__)
CORS(app)

init_routes(app)


if __name__ == "__main__":
    app.run()
