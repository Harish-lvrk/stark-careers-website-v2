from sqlalchemy import create_engine, text
import os

# SQLAlchemy engine using PyMySQL + SSL
engine = create_engine(os.environ['DB_CONNECTION_STRING'],
                       connect_args={"ssl": {
                           "ca": "ca.pem"
                       }},
                       echo=True)


def get_jobs():
    # Fetch all jobs
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM jobs"))
        jobs = result.mappings().all()  # here jobs is a list of dictionaries

        # Convert the list of RowMapping objects into a list of dictionaries
        jobs_list = [dict(row) for row in jobs]
        return jobs_list


def get_specific_job(id):

    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM jobs WHERE id = :val"),
            {"val": id}  # Pass parameters as a dictionary
        )
        row = result.fetchone()  # Fetches the first matching row

        if row is None:
            return None  # Or handle as you see fit (e.g., raise an error)
        else:
            return dict(
                row._mapping)  # Converts the RowMapping to a dictionary


def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("""
            INSERT INTO applications 
            (job_id, full_name, email, linkdin_url, education, work_experiance, resume_url)
            VALUES (:job_id, :full_name, :email, :linkdin_url, :education, :work_experiance, :resume_url)
            """)
        conn.execute(
            query, {
                "job_id": job_id,
                "full_name": data["full_name"],
                "email": data["email"],
                "linkdin_url": data["linkdin_url"],
                "education": data["education"],
                "work_experiance": data["work_experiance"],
                "resume_url": data["resume_url"]
            })
        conn.commit()


def applicatns_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select *from applications"),
                              # Pass parameters as a dictionary
                              )
        applicants = result.mappings().all()  # here jobs is a list of dictionaries
        
        # Convert the list of RowMapping objects into a list of dictionaries
        applicants_list = [dict(row) for row in applicants]
        return applicants_list# Converts the RowMapping to a dictionary
        