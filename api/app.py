from flask import Flask, jsonify
import os
app = Flask(__name__)


@app.route("/")
def index():
    # get env variable
    name = os.environ.get('MESSAGE')
    # return json
    return jsonify({'message': name})


if __name__ == "__main__":
    app.run(host="0.0.0.0")
