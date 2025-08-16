
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
        return jobs

            
        
   