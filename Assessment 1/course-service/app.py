from flask import Flask, jsonify

app = Flask(__name__)


# Sample course data
courses = {
    "CC301": {
        "courseId": "CC301",
        "courseName": "Cloud Computing",
        "credits": 4,
        "department": "CSE"
    },
    "DAA301": {
        "courseId": "DAA301",
        "courseName": "Design and Analysis of Algorithms",
        "credits": 4,
        "department": "CSE"
    },
    "DBMS301": {
        "courseId": "DBMS301",
        "courseName": "Database Management Systems",
        "credits": 4,
        "department": "CSE"
    }
}


# Get course details
@app.route("/courses/<course_id>", methods=["GET"])
def get_course(course_id):

    course = courses.get(course_id)

    if course:
        return jsonify(course)

    return jsonify({
        "error": "Course not found"
    }), 404


# Health check
@app.route("/health", methods=["GET"])
def health():

    return jsonify({
        "service": "course-service",
        "status": "running"
    })


# Start Flask server
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5002,
        debug=True
    )