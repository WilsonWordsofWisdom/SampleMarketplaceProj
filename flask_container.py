import secrets
from threading import Thread

import pandas as pd
from flask import Flask

from flask import jsonify
from flask import request
from flask_cors import CORS
from icecream import ic
from loguru import logger

from items import Items
# import pysnooper

ic.configureOutput(outputFunction=lambda s: logger.debug(s))
ic.configureOutput(includeContext=True)
ic.configureOutput(prefix="")


####################

app = Flask(__name__)
#cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
items = Items()
##########################
# todo: change as needed
# can also write in train class and import to here
# invocations functions, as this function subject to highly frequent changes, just keep it here
@app.route('/')
def predict():
    data = request.get_json(force=True)
    return Items.get_items().to_json()
    #return jsonify(response), 200
if __name__ == "__main__":
    app.run(host='0.0.0.0')