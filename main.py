from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')

@app.route("/check/health", methods=['GET'])
def checkHealth():
    return jsonify({"Code": 200, "Status": "System is Up ..."})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=False)