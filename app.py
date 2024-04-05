from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
        "id" : 1,
        "title" : "Data Analyst",
        "locatiion" : "Lamia, Greece",
        "salary" : "EU. 1.000",
    }
    {
        "id" : 2,
        "title" : "Data Scientist",
        "locatiion" : "Athens, Greece",
        "salary" : "EU. 1.200",
    }
    {
        "id" : 3,
        "title" : "Frontend Engeneer",
        "locatiion" : "Remote",
        "salary" : "EU. 900",
    }
    {
        "id" : 4,
        "title" : "Backend Engeneer",
        "locatiion" : "Xania, Greece",
        "salary" : "EU. 1.300",
    }
]
    


@app.route("/")
def hello():
    return render_template("index.html", jobs = JOBS)

if __name__ == "__main__":
    app.run(debug=True)