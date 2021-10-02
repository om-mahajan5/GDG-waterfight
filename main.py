
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
  if
    if myinfo[2] == "S":
        toNorth = []
        for x in info[1:]:
            if x[0] == myinfo[0] and x[1] > myinfo[1]:
                if x[1]-myinfo[1] <= 3:
                    toNorth.append(x)
                    return "T"
        return ["L", "R", "F"][random.randrange(3)]
    elif myinfo[2] == "N":
        toSouth = []
        for x in info[1:]:
            if x[0] == myinfo[0] and x[1] < myinfo[1]:
                if myinfo[1]-x[1] <= 3:
                    toSouth.append(x)
                    return "T"
        return ["L", "R", "F"][random.randrange(3)]
    elif myinfo[2] == "E":
        toEast = []
        for x in info[1:]:
            if x[0] > myinfo[0] and x[1] == myinfo[1]:
                if x[0]-myinfo[0] <= 3:
                    toEast.append(x)
                    return "T"
        return ["L", "R", "F"][random.randrange(3)]
    elif myinfo[2] == "W":
        toWest = []
        for x in info[1:]:
            if x[0] < myinfo[0] and x[1] == myinfo[1]:
                if myinfo[0]-x[0] <= 3:
                    toWest.append(x)
                    return "T"
            else:
                return ["L", "R"][random.randrange(2)]


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
