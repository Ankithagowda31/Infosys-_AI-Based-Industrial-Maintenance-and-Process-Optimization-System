import joblib

from flask import Flask
from flask_cors import CORS
from flasgger import Swagger

from routes.predict import predict_bp
from routes.robot import robot_bp
from routes.sensor import sensor_bp
from routes.telemetry import telemetry_bp
from routes.maintenance import maintenance_bp
from routes.notification import notification_bp
from routes.inventory import inventory_bp
from routes.incident import incident_bp


app = Flask(__name__)
CORS(app)

Swagger(app)


app.register_blueprint(predict_bp)
app.register_blueprint(robot_bp)
app.register_blueprint(sensor_bp)
app.register_blueprint(telemetry_bp)
app.register_blueprint(maintenance_bp)
app.register_blueprint(notification_bp)
app.register_blueprint(inventory_bp)
app.register_blueprint(incident_bp)


@app.route("/")
def home():
    return {
        "message": "Predictive Maintenance and Process Intelligence API",
        "status": "Running",
    }


if __name__ == "__main__":
    app.run(debug=True)
