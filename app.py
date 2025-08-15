from flask import Flask, render_template , jsonify

app = Flask(__name__)

JOBS = [
  {
    "id": 1,
    'title': "Data Analyst",
    'location': "Bengulur, India",
    'salary': 'Rs. 10,00,000'
  },
  {
    "id": 2,
    'title': "Agent Work",
    'location': "Vishakapatnam, India",
    'salary': 'Rs. 12,00,000'
  },
  {
    "id": 3,
    'title': "ML Engineer",
    'location': "Remote",
    'salary': 'Rs. 15,00,000'
  },
  {
    "id": 4,
    'title': "Full Stakc Developer",
    'location': "Hyderabad, India",
    'salary': '$. 8,00,000'
  },
  {
    "id": 5,
    'title': "Backend Engineer",
    'location': "San Fransisco",
    
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs = JOBS ,company_name = "Stark")

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)