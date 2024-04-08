from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        "id" : 1,
        "title" : "Data Analyst",
        "location" : "Lamia, Greece",
        "salary" : "EU. 1.000",
    },
    {
        "id" : 2,
        "title" : "Data Scientist",
        "location" : "Athens, Greece",
        "salary" : "EU. 1.200",
    },
    {
        "id" : 3,
        "title" : "Frontend Engeneer",
        "location" : "Remote",
        "salary" : "EU. 900",
    },
    {
        "id" : 4,
        "title" : "Backend Engeneer",
        "location" : "Xania, Greece",
        "salary" : "EU. 1.300",
    }
]

    

@app.route("/")
def hello():
    return render_template("index.html", jobs = JOBS, company_name = 'Jovian')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True)