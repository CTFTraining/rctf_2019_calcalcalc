from flask import Flask, request
import bson
import json
import datetime

app = Flask(__name__)


@app.route("/", methods=["POST"])
def calculate():
    data = request.get_data()
    expr = bson.BSON(data).decode()
    if 'exec' in dir(__builtins__):
        del __builtins__.exec
    return bson.BSON.encode({
        "ret": str(eval(str(expr['expression'])))
    })


if __name__ == "__main__":
    app.run("0.0.0.0", 80)
