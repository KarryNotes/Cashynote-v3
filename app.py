from flask import Flask
from flask import render_template
from flask import jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Kanpur , India',
    'salary': '₹10 lpa' 
  }, 
   {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Bhopal , India',
    'salary': '₹15 lpa' 
  }, 
    {
    'id': 3,
    'title': 'Data Manager',
    'location': 'Lucknow , India',
    'salary': '₹12.5 lpa' 
  },
    {
    'id': 4,
    'title': 'Data Assistant',
    'location': 'Kanpur, India',
    'salary': '₹8.5 lpa' 
  }  
  ]
@app.route("/")
def hello():
  return render_template("home.html", jobs=JOBS, company_name="Cashynote")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(debug=True)
