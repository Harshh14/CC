from flask import Flask, jsonify, render_template
import requests
import os

app = Flask(__name__)


# URLs of other microservices
# These will later be changed to Docker service names
STUDENT_SERVICE_URL = os.getenv(
    "STUDENT_SERVICE_URL",
    "http://localhost:5001"
)

COURSE_SERVICE_URL = os.getenv(
    "COURSE_SERVICE_URL",
    "http://localhost:5002"
)


# Sample enrollment data
enrollments = {
    101: ["CC301"],
    102: ["DAA301"],
    103: ["DBMS301"]
}
@app.route("/")
def home():
    return render_template("index.html")

# Get enrollment details for a student
@app.route("/enrollment/<int:student_id>", methods=["GET"])
def get_enrollment(student_id):

    try:

        # Request student information
        student_response = requests.get(
            f"{STUDENT_SERVICE_URL}/students/{student_id}",
            timeout=5
        )

        if student_response.status_code != 200:
            return jsonify({
                "error": "Student not found"
            }), 404

        student = student_response.json()

        # Get the courses in which the student is enrolled
        course_ids = enrollments.get(student_id, [])

        courses = []

        for course_id in course_ids:

            course_response = requests.get(
                f"{COURSE_SERVICE_URL}/courses/{course_id}",
                timeout=5
            )

            if course_response.status_code == 200:
                courses.append(course_response.json())

        # Return combined response
        return jsonify({
            "student": student,
            "courses": courses,
            "enrollmentStatus": "Enrolled"
        })

    except requests.exceptions.RequestException as error:

        return jsonify({
            "error": "Unable to communicate with other services",
            "details": str(error)
        }), 500


# Health check endpoint
@app.route("/health", methods=["GET"])
def health():

    return jsonify({
        "service": "enrollment-service",
        "status": "running"
    })


# Start the Flask server
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5003,
        debug=True
    )