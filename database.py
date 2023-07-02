import sqlalchemy
from sqlalchemy import text
from sqlalchemy import create_engine
import ssl
import os
from os import environ

db_connection_string =  "mysql+pymysql://w760pvrule6vd6p9gqpz:pscale_pw_rUoEg4yD8GSNoLV9SjjdXp9BOOIkKrmuEflpIqKtWgz@aws.connect.psdb.cloud/cashynote?charset=utf8mb4" 

engine = create_engine(
    db_connection_string,
    connect_args={"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}}
)
def load_jobs_from_db():
   with engine.connect() as conn:
      result = conn.execute(text("select * from jobs")).all()
      jobs = []
      
      for row in result:
        jobs.append(({'title':row.title, 'location':row.location, 'salary':row.salary}))
        print({'title':row.title, 'location':row.location, 'salary':row.salary})
        return jobs
