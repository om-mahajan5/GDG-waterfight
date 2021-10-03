import os
import logging
import random
from flask import Flask, request

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'T', 'L', 'R']
info = []
myinfo = []
@app.route("/", methods=['POST'])
def move():
    request.get_data()
    dataFormat(request.json)
    decision = checkForward(info, myinfo)
    logger.info(str(request.json) + " DECISION " + decision)
    return checkForward(info, myinfo)
    # return moves[random.randrange(len(moves))]


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0',
            port=int(os.environ.get('PORT', 8080)))
