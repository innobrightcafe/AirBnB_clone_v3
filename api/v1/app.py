from flask import Flask
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def teardown_db(exception):
    """Close storage session"""
    storage.close()


if __name__ == "__main__":
    host1 = os.environ.get("HBNB_API_HOST", '0.0.0.0')
    port1 = int(os.environ.get("HBNB_API_PORT", 5000))
    app.run(host=host1, port=port1, threaded=True)
