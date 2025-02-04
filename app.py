from flask import Flask, render_template

app = Flask(__name__)

# Simulated IoT data
alerts = [
    {"animal": "Deer", "time": "10:15 AM", "location": "Point A"},
    {"animal": "Elephant", "time": "11:30 AM", "location": "Point B"},
    {"animal": "Fox", "time": "1:45 PM", "location": "Point C"},
]

@app.route("/")
def home():
    return render_template("home.html", alerts=alerts)

if __name__ == "__main__":
    app.run(debug=True)
