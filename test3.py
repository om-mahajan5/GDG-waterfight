import os
import logging
import random
from flask import Flask, request

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)
app = Flask(__name__)

state = []
mystate = None

def dataFormat(data):
    global state, mystate
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
    state = list(zip(X, Y, D, wasHit, score))
    mystate = state[0]

def checkAround():
    
    pass


def checkForward(state, mystate):
    aheadMe = []
    if mystate[2] == "S":
        for x in state[1:]:
            if x[0] == mystate[0] and x[1] > mystate[1]:
                if x[1]-mystate[1] <= 3:
                    aheadMe.append(x)
                    return "T"
    elif mystate[2] == "N":
        for x in state[1:]:
            if x[0] == mystate[0] and x[1] < mystate[1]:
                if mystate[1]-x[1] <= 3:
                    aheadMe.append(x)
                    return "T"
    elif mystate[2] == "E":
        for x in state[1:]:
            if x[0] > mystate[0] and x[1] == mystate[1]:
                if x[0]-mystate[0] <= 3:
                    aheadMe.append(x)
                    return "T"
    elif mystate[2] == "W":
        for x in state[1:]:
            if x[0] < mystate[0] and x[1] == mystate[1]:
                if mystate[0]-x[0] <= 3:
                    aheadMe.append(x)
                    return "T"
    if len(aheadMe)>0:
        return "F"
    return ["L", "R"][random.randrange(3)]


@app.route("/", methods=['POST'])
def move():
    request.get_data()
    dataFormat(request.json)
    decision = checkForward(state, mystate)
    logger.info(str(request.json) + " DECISION " + decision)
    return checkForward(state, mystate)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0',
            port=int(os.environ.get('PORT', 8080)))