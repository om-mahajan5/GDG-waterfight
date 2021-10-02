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


def dataFormat(data):
    global info, myinfo
    X = [data['arena']['state'][key]['x']
         for key in data['arena']['state'].keys()]
    Y = [data['arena']['state'][key]['y']
         for key in data['arena']['state'].keys()]
    D = [data['arena']['state'][key]['direction']
         for key in data['arena']['state'].keys()]
    wasHit = [data['arena']['state'][key]['wasHit']
              for key in data['arena']['state'].keys()]
    score = [data['arena']['state'][key]['score']
             for key in data['arena']['state'].keys()]
    info = list(zip(X, Y, D, wasHit, score))
    myinfo = info[0]


def checkForward(info, myinfo):
    aheadMe = []
    if myinfo[2] == "S":
        for x in info[1:]:
            if x[0] == myinfo[0] and x[1] > myinfo[1]:
                aheadMe.append(x)
                if x[1]-myinfo[1] <= 3:
                    return "T"
    elif myinfo[2] == "N":
        for x in info[1:]:
            if x[0] == myinfo[0] and x[1] < myinfo[1]:
                aheadMe.append(x)
                if myinfo[1]-x[1] <= 3:
                    return "T"
    elif myinfo[2] == "E":
        for x in info[1:]:
            if x[0] > myinfo[0] and x[1] == myinfo[1]:
                aheadMe.append(x)
                if x[0]-myinfo[0] <= 3:
                    return "T"
    elif myinfo[2] == "W":
        for x in info[1:]:
            if x[0] < myinfo[0] and x[1] == myinfo[1]:
                aheadMe.append(x)
                if myinfo[0]-x[0] <= 3:
                    return "T"
    if len(aheadMe)>0:
        return "F"
    return ["L", "R"][random.randrange(3)]


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
