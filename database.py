
from sqlalchemy import create_engine, text 
import os

# SQLAlchemy engine using PyMySQL + SSL
engine = create_engine(
    os.environ['DB_CONNECTION_STRING'],
    connect_args={
        "ssl": {
            "ca": "ca.pem"
        }
    },
    echo=True
)

def get_jobs():
    # Fetch all jobs
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM jobs"))
        jobs = result.mappings().all()   # here jobs is a list of dictionaries
        
         # Convert the list of RowMapping objects into a list of dictionaries
        jobs_list = [dict(row) for row in jobs]
        return jobs_list

def get_specific_job(id):
   
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM jobs WHERE id = :val"),
            {"val": id}  # Pass parameters as a dictionary
        )
        row = result.fetchone() # Fetches the first matching row

        if row is None:
            return None # Or handle as you see fit (e.g., raise an error)
        else:
            return dict(row._mapping) # Converts the RowMapping to a dictionary

        
   