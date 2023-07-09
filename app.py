from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import text
from sqlalchemy import create_engine

load_dotenv()

app = Flask(__name__)

app.secret_key = "cashynotes"
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

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(dbConnectionStr)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
  for row in result:
    jobs.append(({
      "id": row.id,
      "title": row.title,
      "location": row.location,
      "salary": row.salary,
      "currency": row.currency,
      "responsbilities": row.responsbilities,
      "requirements": row.requirements,
    }))
  print({
    "title": row.title,
    "location": row.location,
    "salary": row.salary,
    "currency": row.currency,
    "responsbilities": row.responsbilities,
    "requirements": row.requirements
  })
  return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"SELECT * FROM jobs WHERE id = {id}")).first()
    print(id)
    if result:
      return result
    else:
      return None

def 


@app.route("/")
def hello():
  jobs = load_jobs_from_db()
  return render_template("home.html", jobs=jobs, company_name="Cashynote")


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)

  if not job:
    return "No job with given id exists!", 404
  return render_template('jobpage.html', job=job)


@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form
  job = load_job_from_db(id)
  
  #send an email
  #display an acknowledgement
  return render_template('application_submitted.html',
                         application=data,
                         job=job)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
