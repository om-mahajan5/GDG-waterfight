import os
import logging
import random
from flask import Flask, request

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'T', 'L', 'R']
state = []
mystate = []

def formatData(mydata):
    global state, mystate
    myURL = mydata['_links']['self']['href']
    for key in mydata['arena']['state'].keys():
        if key==myURL:
            mystate = [mydata['arena']['state'][key]['x'],mydata['arena']['state'][key]['y'],mydata['arena']['state'][key]['direction'],mydata['arena']['state'][key]['wasHit'],mydata['arena']['state'][key]['score']]
        else:
            state.append([mydata['arena']['state'][key]['x'],mydata['arena']['state'][key]['y'],mydata['arena']['state'][key]['direction'],mydata['arena']['state'][key]['wasHit'],mydata['arena']['state'][key]['score']])


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
    if mystate[2] == "S":
        for player in state:
            if player[0] == mystate[0] and player[1] > mystate[1]:
                aheadMe.append(player)
                if player[1]-mystate[1] <= 3:
                    return "T"
    elif mystate[2] == "N":
        for player in state:
            if player[0] == mystate[0] and player[1] < mystate[1]:
                aheadMe.append(player)
                if mystate[1]-player[1] <= 3:
                    return "T"
    elif mystate[2] == "E":
        for player in state:
            if player[0] > mystate[0] and player[1] == mystate[1]:
                aheadMe.append(player)
                if player[0]-mystate[0] <= 3:
                    return "T"
    elif mystate[2] == "W":
        for player in state:
            if player[0] < mystate[0] and player[1] == mystate[1]:
                aheadMe.append(player)
                if mystate[0]-player[0] <= 3:
                    return "T"
    if len(aheadMe)>0:
        return "F"
    return ["L", "R"][random.randrange(3)]


@app.route("/", methods=['POST'])
def move():
    request.get_data()
    formatData(request.json)
    decision = checkForward(state, mystate)
    logger.info(str(request.json) + " DECISION " + decision)
    return checkForward(decision)
    # return moves[random.randrange(len(moves))]


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0',
            port=int(os.environ.get('PORT', 8080)))
