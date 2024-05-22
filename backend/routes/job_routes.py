from flask import Blueprint, request, jsonify
from config import Config
from models import db, JobApplication
import requests
import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)

bp = Blueprint('job_routes', __name__)

@bp.route('/api/search_jobs', methods=['POST'])
def search_jobs():
    try:
        data = request.json
        query = data.get("query")
        location = data.get("location")
        if not query or not location:
            return jsonify({"error": "Query and location are required"}), 400

        jobs = fetch_jobs_from_serper(query, location)
        return jsonify(jobs)
    except Exception as e:
        logging.error(f"Error in search_jobs: {str(e)}")
        return jsonify({"error": "An error occurred while searching for jobs"}), 500

def fetch_jobs_from_serper(query, location):
    try:
        serper_api_key = Config.SERPER_API_KEY
        url = f"https://serper.dev/api/search?query={query}+jobs+in+{location}&type=job"
        headers = {"Authorization": f"Bearer {serper_api_key}"}
        response = requests.get(url, headers=headers)
        logging.debug(f"URL: {url}")
        logging.debug(f"Response status code: {response.status_code}")
        logging.debug(f"Response text: {response.text}")

        response.raise_for_status()
        jobs = response.json().get("jobs", [])
        return jobs
    except requests.exceptions.RequestException as e:
        logging.error(f"HTTP request failed: {str(e)}")
        return []
    except ValueError:
        logging.error("Invalid JSON response")
        return []

@bp.route('/api/apply_for_jobs', methods=['POST'])
def apply_for_jobs():
    try:
        logging.debug("Request data: %s", request.data)
        data = request.json
        logging.debug("Parsed JSON data: %s", data)

        user_id = data.get("user_id")
        jobs = data.get("jobs")

        if not user_id or not jobs:
            return jsonify({"error": "User ID and jobs are required"}), 400

        for job in jobs:
            if not all([job.get("title"), job.get("company"), job.get("location")]):
                return jsonify({"error": "Job title, company, and location are required"}), 400

            new_application = JobApplication(
                user_id=user_id,
                job_title=job.get("title"),
                company=job.get("company"),
                location=job.get("location"),
                status="Applied"
            )
            db.session.add(new_application)
            db.session.commit()
        return jsonify({"message": "Job applications submitted successfully"})
    except Exception as e:
        logging.error(f"Error in apply_for_jobs: {str(e)}")
        return jsonify({"error": f"An error occurred while applying for jobs: {str(e)}"}), 500

@bp.route('/api/track', methods=['GET'])
def track_applications():
    try:
        user_id = request.args.get('user_id')
        if not user_id:
            return jsonify({"error": "User ID is required"}), 400

        applications = JobApplication.query.filter_by(user_id=user_id).all()
        applications_list = [{"id": app.id, "job_title": app.job_title, "company": app.company, "location": app.location, "status": app.status} for app in applications]
        return jsonify(applications_list)
    except Exception as e:
        logging.error(f"Error in track_applications: {str(e)}")
        return jsonify({"error": "An error occurred while tracking applications"}), 500

@bp.route('/api/update_status', methods=['POST'])
def update_status():
    try:
        data = request.json
        application_id = data.get("application_id")
        status = data.get("status")
        interview_date_str = data.get("interview_date")
        offer_details = data.get("offer_details")

        logging.debug(f"Received data for update_status: {data}")

        if not application_id or not status:
            logging.debug("Missing application_id or status")
            return jsonify({"error": "Application ID and status are required"}), 400

        application = JobApplication.query.get(application_id)
        logging.debug(f"Application fetched for ID {application_id}: {application}")

        if application:
            application.status = status
            if interview_date_str:
                try:
                    interview_date = datetime.strptime(interview_date_str, "%Y-%m-%dT%H:%M:%S")
                    application.interview_date = interview_date
                except ValueError as e:
                    logging.error(f"Invalid date format for interview_date: {str(e)}")
                    return jsonify({"error": "Invalid date format for interview_date"}), 400
            if offer_details:
                application.offer_details = offer_details
            db.session.commit()
            logging.debug("Application status updated successfully")
            return jsonify({"message": "Status updated successfully"})
        else:
            logging.debug("Application not found")
            return jsonify({"error": "Application not found"}), 404
    except Exception as e:
        logging.error(f"Error in update_status: {str(e)}")
        return jsonify({"error": "An error occurred while updating the application status"}), 500

@bp.route('/api/delete_application', methods=['DELETE'])
def delete_application():
    try:
        data = request.json
        application_id = data.get("application_id")

        if not application_id:
            return jsonify({"error": "Application ID is required"}), 400

        application = JobApplication.query.get(application_id)
        if application:
            db.session.delete(application)
            db.session.commit()
            return jsonify({"message": "Application deleted successfully"})
        else:
            return jsonify({"error": "Application not found"}), 404
    except Exception as e:
        logging.error(f"Error in delete_application: {str(e)}")
        return jsonify({"error": "An error occurred while deleting the application"}), 500

@bp.route('/api/application_details', methods=['GET'])
def application_details():
    try:
        application_id = request.args.get('application_id')

        if not application_id:
            return jsonify({"error": "Application ID is required"}), 400

        application = JobApplication.query.get(application_id)
        if application:
            application_details = {
                "job_title": application.job_title,
                "company": application.company,
                "location": application.location,
                "status": application.status,
                "interview_date": application.interview_date,
                "offer_details": application.offer_details
            }
            return jsonify(application_details)
        else:
            return jsonify({"error": "Application not found"}), 404
    except Exception as e:
        logging.error(f"Error in application_details: {str(e)}")
        return jsonify({"error": "An error occurred while retrieving the application details"}), 500
