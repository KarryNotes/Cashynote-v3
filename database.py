from sqlalchemy import text
from sqlalchemy import engine



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


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO APPLICATIONS (job_id, first_name, last_name, email, linkedin_url, education, work_experience, resume_url) VALUES(:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_ur)")

  conn.execute(query,
               job_id=job_id, 
               first_name=data['first_name'],
               last_name = data['last_name'],
               email = data['email'],
               education = data['education'],
               work_experience = data['work_experience'],
               resume_url = data['resume_url'])
 
