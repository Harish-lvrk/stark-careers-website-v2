from flask import Flask, render_template , jsonify
from database import get_jobs , get_specific_job
app = Flask(__name__)



@app.route("/")
def hello_world():
  return render_template('home.html',jobs = get_jobs() ,company_name = "Stark")


@app.route('/api/jobs')
def list_jobs():
  jobs_from_db = get_jobs()
  return jsonify(jobs_from_db)
  
@app.route('/job/<id>')
def show_jobs(id):# this is what the rest api is with url getting the json object
  job = get_specific_job(id)
  if not job:
    return "Not Found", 404
  return render_template('jobpage.html',job = job)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)