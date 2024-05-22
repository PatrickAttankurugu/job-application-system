from flask import Blueprint, request, jsonify
from models import db, User, JobApplication  # Make sure JobApplication is imported

bp = Blueprint('user_routes', __name__)

@bp.route('/api/preferences', methods=['POST'])
def set_preferences():
    preferences = request.json
    # Save preferences to the database (mocked for now)
    return jsonify({"message": "Preferences saved successfully"})

@bp.route('/api/upload', methods=['POST'])
def upload_resume():
    resume = request.files['file']
    # Save resume to the database (mocked for now)
    return jsonify({"message": "Resume uploaded successfully"})

@bp.route('/api/applications', methods=['GET'])
def get_applications():
    user_id = request.args.get('user_id')
    applications = JobApplication.query.filter_by(user_id=user_id).all()
    applications_list = [{"job_title": app.job_title, "company": app.company, "location": app.location, "status": app.status} for app in applications]
    return jsonify(applications_list)
