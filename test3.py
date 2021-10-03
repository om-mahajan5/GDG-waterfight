import json, random
from os import stat
import matplotlib.pyplot as plt
data = '''{
   "_links":{
      "self":{
         "href":"https://python-bot-jxkeswruca-em.a.run.app/"
      }
   },
   "arena":{
      "dims":[
         13,
         9
      ],
      "state":{
         "https://nodejskrs-bot-7juvvzwy4q-uc.a.run.app":{
            "x":0,
            "y":0,
            "direction":"S",
            "wasHit":false,
            "score":-3
         },
         "https://python-bot-ksvj7q4wga-em.a.run.app":{
            "x":7,
            "y":0,
            "direction":"W",
            "wasHit":false,
            "score":-59
         },
         "https://python-bot-dnuf5dybaq-em.a.run.app/":{
            "x":5,
            "y":7,
            "direction":"E",
            "wasHit":false,
            "score":-14
         },
         "https://python-bot-wzf2k7csnq-wl.a.run.app":{
            "x":7,
            "y":2,
            "direction":"S",
            "wasHit":false,
            "score":16
         },
         "https://94e9-172-105-34-203.ngrok.io":{
            "x":12,
            "y":1,
            "direction":"W",
            "wasHit":false,
            "score":-25
         },
         "https://python-bot-xpu2myq57q-uc.a.run.app":{
            "x":12,
            "y":0,
            "direction":"E",
            "wasHit":false,
            "score":-4
         },
         "https://python-bot-jxkeswruca-em.a.run.app/":{
            "x":6,
            "y":6,
            "direction":"E",
            "wasHit":false,
            "score":-49
         },
         "https://jay-bot-4rmtwapiia-uc.a.run.app":{
            "x":11,
            "y":3,
            "direction":"S",
            "wasHit":false,
            "score":146
         },
         "https://nodejs-bot-n33wt2kama-as.a.run.app":{
            "x":10,
            "y":0,
            "direction":"W",
            "wasHit":false,
            "score":-25
         },
         "https://python-bot-j4bgsvwz3a-uc.a.run.app":{
            "x":0,
            "y":6,
            "direction":"N",
            "wasHit":true,
            "score":-72
         },
         "https://nodejs-bot-44oaeskbqa-as.a.run.app":{
            "x":4,
            "y":3,
            "direction":"S",
            "wasHit":false,
            "score":-19
         },
         "https://python-bot-adlhc57fcq-de.a.run.app":{
            "x":0,
            "y":8,
            "direction":"N",
            "wasHit":false,
            "score":116
         },
         "https://java-springboot-bot-t34nqg3eqq-as.a.run.app":{
            "x":6,
            "y":2,
            "direction":"W",
            "wasHit":false,
            "score":-21
         },
         "https://java-springboot-bot-r5lsmc2n3q-an.a.run.app":{
            "x":10,
            "y":7,
            "direction":"W",
            "wasHit":false,
            "score":-15
         },
         "https://java-springboot-bot-gwlv4a5zxa-as.a.run.app":{
            "x":2,
            "y":7,
            "direction":"N",
            "wasHit":true,
            "score":-16
         },
         "https://python-bot-oskyweulvq-as.a.run.app/":{
            "x":9,
            "y":8,
            "direction":"S",
            "wasHit":false,
            "score":4
         },
         "https://python-bot-iiqpxb2opq-uc.a.run.app":{
            "x":7,
            "y":3,
            "direction":"N",
            "wasHit":false,
            "score":-22
         },
         "https://python-bot-36ufadraiq-as.a.run.app":{
            "x":0,
            "y":4,
            "direction":"E",
            "wasHit":false,
            "score":-62
         },
         "https://nodejs-bot-gqugfjrxja-uc.a.run.app":{
            "x":2,
            "y":5,
            "direction":"S",
            "wasHit":false,
            "score":124
         }
      }
   }
}'''

state = []
mystate = []
mydata = json.loads(data)
def formatData():
    global state, mystate
    myURL = mydata['_links']['self']['href']
    for key in mydata['arena']['state'].keys():
        if key==myURL:
            mystate = [mydata['arena']['state'][key]['x'],mydata['arena']['state'][key]['y'],mydata['arena']['state'][key]['direction'],mydata['arena']['state'][key]['wasHit'],mydata['arena']['state'][key]['score']]
        else:
            state.append([mydata['arena']['state'][key]['x'],mydata['arena']['state'][key]['y'],mydata['arena']['state'][key]['direction'],mydata['arena']['state'][key]['wasHit'],mydata['arena']['state'][key]['score']])

formatData()
print("My coordinates are :" + str(mystate))
for player in state:
    player - 
'''
X = [x-X[myPosition] for x in X]
Y = [y-Y[myPosition] for y in Y]
state = list(zip(X,Y,D,wasHit,score))

print(state)
plt.gca().invert_yaxis()
plt.scatter(X,Y)
plt.scatter(mystate[0],mystate[1],marker="s")
plt.show()
'''