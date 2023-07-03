from flask import Flask
from flask import render_template
from flask import jsonify
from os import environ
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy import text
import sqlalchemy
import os
load_dotenv()

app = Flask(__name__)

app.secret_key="cashynotes"
# app.permanent_session_lifetime = timedelta(minutes=30)

# DATABASE CONNECTION
# Set & Get Env Variables
dbUser = os.environ['DBUSERNAME'].strip()
dbPwd = os.environ['PASSWORD'].strip()
dbHost = os.environ['HOST'].strip()
dbName = os.environ['DATABASE'].strip()

dbConnectionStr = f"mysql+pymysql://{dbUser}:{dbPwd}@{dbHost}/{dbName}?ssl_ca=cacert.pem"

app.config['SQLALCHEMY_DATABASE_URI'] = dbConnectionStr
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def load_jobs_from_db():
  result = db.session.execute(text(f"select * from jobs")).all()
  jobs = []

  for row in result:
      jobs.append(
          ({"title": row.title, "location": row.location, "salary": row.salary})
      )
      print({"title": row.title, "location": row.location, "salary": row.salary})
      return jobs

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
