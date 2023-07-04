import sqlalchemy
from sqlalchemy import text
from sqlalchemy import create_engine, engine
import ssl


def load_job_from_db():
    with engine.connect() as conn:
        result = conn.execute(
            text("select * from jobs where id = :val"),
            val=id
        )
    rows= result.all()
    if len(rows) == 0:
        return None
    else:
        return dict(rows[0])