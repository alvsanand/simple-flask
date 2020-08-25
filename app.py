from flask import Flask
import os
import time
from random import uniform

version = os.environ.get("VERSION", "1.0")
delay = os.environ.get("DELAY", "")
failure = os.environ.get("FAILURE", "")
port = os.environ.get("PORT", 6000)

app = Flask(__name__)


@app.route("/")
def hello():
    if failure and float(failure) > uniform(0, 1):
        return "RANDOM ERROR", 500

    if delay:
        time.sleep(float(delay))

    return "Helloworld from Flask[{0}]!!".format(version), 200


if __name__ == "__main__":
    port = int(port)
    app.run(debug=True, host='0.0.0.0', port=port)
