from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def teardown_db(exception):
    """Close storage session"""
    storage.close()


if __name__ == "__main__":
    host1 = getenv("HBNB_API_HOST")
    port1 = int(getenv("HBNB_API_PORT"))
    app.run(host=host1, port=port1, threaded=True)
