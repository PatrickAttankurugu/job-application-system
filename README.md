# Job Application System

## Overview
This project is a job application management system that helps users search for jobs, apply for them, and track their application status. The system is built with a Flask backend and a React frontend.

## Features
- Job search using the Serper API
- Apply for jobs with uploaded resumes
- Track job applications
- Update application status
- Delete job applications

## Project Structure
job-application-system/
├── backend/
│ ├── app.py
│ ├── config.py
│ ├── models.py
│ ├── routes/
│ │ ├── init.py
│ │ ├── job_routes.py
│ │ ├── user_routes.py
│ ├── uploads/
│ ├── .env
│ ├── requirements.txt
├── frontend/
│ ├── public/
│ ├── src/
│ │ ├── components/
│ │ │ ├── JobList.js
│ │ │ ├── JobDetails.js
│ │ │ ├── ApplicationForm.js
│ │ ├── App.js
│ │ ├── index.js
│ ├── package.json
├── .gitignore
├── README.md
└── LICENSE


## Installation

### Backend
1. Navigate to the backend directory:
    ```bash
    cd backend
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the backend directory and add your API keys:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    SERPER_API_KEY=your_serper_api_key
    ```

5. Run the backend server:
    ```bash
    python app.py
    ```

### Frontend
1. Navigate to the frontend directory:
    ```bash
    cd frontend
    ```

2. Install the required packages:
    ```bash
    npm install
    ```

3. Start the frontend development server:
    ```bash
    npm start
    ```

## API Endpoints

### User Routes

#### Set Preferences
- **URL:** `/api/preferences`
- **Method:** `POST`
- **Description:** Save user preferences.
- **Request Body:**
    ```json
    {
      "preference": "example"
    }
    ```
- **Response:**
    ```json
    {
      "message": "Preferences saved successfully"
    }
    ```

#### Upload Resume
- **URL:** `/api/upload`
- **Method:** `POST`
- **Description:** Upload a user resume.
- **Request Body:** Form data with the key `file` containing the file.
- **Response:**
    ```json
    {
      "message": "Resume uploaded successfully"
    }
    ```

#### Get Applications
- **URL:** `/api/applications`
- **Method:** `GET`
- **Description:** Get all applications for a user.
- **Query Parameters:**
    - `user_id` (integer): The ID of the user.
- **Response:**
    ```json
    [
      {
        "job_title": "AI Developer",
        "company": "TechCorp",
        "location": "Accra",
        "status": "Applied"
      }
    ]
    ```

### Job Routes

#### Search Jobs
- **URL:** `/api/search_jobs`
- **Method:** `POST`
- **Description:** Search for jobs using the Serper API.
- **Request Body:**
    ```json
    {
      "query": "AI Developer",
      "location": "Accra"
    }
    ```
- **Response:**
    ```json
    [
      {
        "title": "AI Developer",
        "company": "TechCorp",
        "location": "Accra",
        "description": "Job description here..."
      }
    ]
    ```

#### Apply for Jobs
- **URL:** `/api/apply_for_jobs`
- **Method:** `POST`
- **Description:** Apply for jobs.
- **Request Body:**
    ```json
    {
      "user_id": 1,
      "jobs": [
        {
          "title": "AI Developer",
          "company": "TechCorp",
          "location": "Accra"
        }
      ]
    }
    ```
- **Response:**
    ```json
    {
      "message": "Job applications submitted successfully"
    }
    ```

#### Update Application Status
- **URL:** `/api/update_status`
- **Method:** `POST`
- **Description:** Update the status of a job application.
- **Request Body:**
    ```json
    {
      "application_id": 1,
      "status": "Interview Scheduled",
      "interview_date": "2023-05-25T10:00:00",
      "offer_details": "N/A"
    }
    ```
- **Response:**
    ```json
    {
      "message": "Application status updated successfully"
    }
    ```

#### Delete Application
- **URL:** `/api/delete_application`
- **Method:** `DELETE`
- **Description:** Delete a job application.
- **Request Body:**
    ```json
    {
      "application_id": 1
    }
    ```
- **Response:**
    ```json
    {
      "message": "Application deleted successfully"
    }
    ```

#### Application Details
- **URL:** `/api/application_details`
- **Method:** `GET`
- **Description:** Retrieves detailed information about a specific job application.
- **Query Parameters:**
  - `application_id`: The ID of the application.
- **Response:**
    ```json
    {
      "job_title": "AI Developer",
      "company": "TechCorp",
      "location": "Accra",
      "status": "Interview Scheduled",
      "interview_date": "2023-05-25T10:00:00",
      "offer_details": "N/A"
    }
    ```

## Environment Variables

Ensure that the following environment variables are set in a `.env` file:

```plaintext
OPENAI_API_KEY="your_openai_api_key"
SERPER_API_KEY="your_serper_api_key"

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](LICENSE)
