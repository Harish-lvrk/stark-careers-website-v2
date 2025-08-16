from flask import Flask, render_template , jsonify
from database import get_jobs
app = Flask(__name__)



@app.route("/")
def hello_world():
  return render_template('home.html',jobs = get_jobs() ,company_name = "Stark")


@app.route('/api/jobs')
def list_jobs():
  jobs_from_db = get_jobs()

  # Convert the list of RowMapping objects into a list of dictionaries
  jobs_list = [dict(row) for row in jobs_from_db]

  return jsonify(jobs_list)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)