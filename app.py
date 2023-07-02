from flask import Flask
from flask import render_template
from flask import jsonify
from database import load_jobs_from_db


app = Flask(__name__)


@app.route("/")
def hello():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs, company_name="Cashynote")


@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(debug=True)
