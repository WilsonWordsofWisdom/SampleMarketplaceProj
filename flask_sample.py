import secrets
from threading import Thread

import pandas as pd
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from icecream import ic
from loguru import logger
from orchestrator import Orchestrator
from wordcloud_generation import WordcloudGenerator

# import pysnooper

ic.configureOutput(outputFunction=lambda s: logger.debug(s))
ic.configureOutput(includeContext=True)
ic.configureOutput(prefix="")

model = Orchestrator()
wordcloud_model = WordcloudGenerator()
####################

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


# @pysnooper.snoop()
@app.route("/ping", methods=["GET"])
def ping():
    """Determine if the container is working and healthy. In this
    sample container, we declare it healthy if we can load the model
    successfully."""

    # always return 200, in case model did not load in time
    # after all, model should be in place and model loading can be
    # activated and checked by query
    return jsonify({"ping": "success"}), 200
    # Response(
    #     response="\n", status=status, mimetype="application/json"
    # )


##########################
# todo: change as needed
# can also write in train class and import to here
# invocations functions, as this function subject to highly frequent changes, just keep it here
@app.route("/invocations", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    content = data["content"]
    model_choice = data["model"]
    model_choice = str(model_choice).strip().lower()
    # todo: add GCP model
    if model_choice in ["voc", "pcnn"]:
        use_gcp_sentiments = data["use_gcp_sentiments"]
        gcp_sentiments = (
            True
            if str(use_gcp_sentiments).strip().lower() == "true"
            else False
        )
        ic(content, use_gcp_sentiments)
        response = model.get_response(content, model_choice, gcp_sentiments)
        return jsonify(response), 200
    elif model_choice == "wordcloud":
        # todo: S3 path check in next iteration, something like path starts with s3://de-mlauto-de-wordcloud-nonprod/incoming
        data["token"] = secrets.token_urlsafe(32)
        output_path = (
            f'{content.rsplit(".", maxsplit=1)[0]}_{data["token"]}_output'
        )
        data["output_path"] = f"{output_path}.csv"
        # todo: consider to add a parameter to control image generate or not
        data["image_output_path"] = f"{output_path}.png"
        # data['log_output_path'] = f'{output_path}.log'
        thread = Thread(
            target=wordcloud_model.get_response, kwargs={"data": data}
        )
        thread.start()
        return jsonify(data), 200
    elif model_choice == "wordcloud_result":
        try:
            return (
                jsonify(pd.read_csv(content, header=None).to_dict("index")),
                200,
            )
        except Exception as e:
            return jsonify(e)
    else:
        return jsonify({"Error": "model_choice not valid"}), 400