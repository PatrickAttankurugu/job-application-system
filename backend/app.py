from flask import Flask
from config import Config
from models import db
from routes import job_routes, user_routes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Register blueprints
app.register_blueprint(job_routes.bp)
app.register_blueprint(user_routes.bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
