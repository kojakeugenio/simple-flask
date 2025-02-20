from flask import Flask, render_template

app = Flask(__name__)

@app.route("/ping")
def ping():
    return "pong", 200

@app.route("/")
def home():
    return render_template("index.html", title="Simple Flask App")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
