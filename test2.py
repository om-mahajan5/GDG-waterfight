import json
import matplotlib.pyplot as plt
data = '''{
   "_links":{
      "self":{
         "href":"https://python-bot-jxkeswruca-em.a.run.app/"
      }
   },
   "arena":{
      "dims":[
         10,
         7
      ],
      "state":{
         "https://python-bot-jinxto7chq-em.a.run.app":{
            "x":2,
            "y":6,
            "direction":"E",
            "wasHit":false,
            "score":0
         },
         "https://java-springboot-bot-vt7gk6uhyq-em.a.run.app":{
            "x":9,
            "y":0,
            "direction":"W",
            "wasHit":false,
            "score":0
         },
         "https://nodejs-bot-zx4wpxe3oq-em.a.run.app":{
            "x":7,
            "y":2,
            "direction":"E",
            "wasHit":false,
            "score":0
         },
         "https://python-bot-3h4xit75ca-uc.a.run.app":{
            "x":6,
            "y":5,
            "direction":"N",
            "wasHit":false,
            "score":0
         },
         "https://nodejs-bot-tmozo7xwqa-as.a.run.app":{
            "x":3,
            "y":5,
            "direction":"E",
            "wasHit":false,
            "score":0
         },
         "https://java-springboot-bot-oaiu5q5ata-de.a.run.app":{
            "x":4,
            "y":4,
            "direction":"S",
            "wasHit":false,
            "score":0
         },
         "https://java-quarkus-bot-nallqtvrbq-de.a.run.app":{
            "x":4,
            "y":3,
            "direction":"N",
            "wasHit":false,
            "score":0
         },
         "https://python-bot-ucfpygglmq-an.a.run.app/":{
            "x":4,
            "y":1,
            "direction":"N",
            "wasHit":false,
            "score":0
         },
         "https://nodejs-bot-q7wdicztsa-uc.a.run.app/":{
            "x":0,
            "y":3,
            "direction":"E",
            "wasHit":false,
            "score":0
         },
         "https://python-bot-lt7kzp4ajq-an.a.run.app/":{
            "x":7,
            "y":5,
            "direction":"W",
            "wasHit":false,
            "score":0
         },
         "https://python-bot-jxkeswruca-em.a.run.app/":{
            "x":5,
            "y":4,
            "direction":"S",
            "wasHit":false,
            "score":0
         },
         "https://java-springboot-bot-aoj52cfs3a-em.a.run.app/":{
            "x":3,
            "y":6,
            "direction":"W",
            "wasHit":false,
            "score":0
         }
      }
   }
}'''

mydata = json.loads(data)
def dataFormat(mydata):
    X= [mydata['arena']['state'][key]['x'] for key in mydata['arena']['state'].keys()]
    Y= [mydata['arena']['state'][key]['y'] for key in mydata['arena']['state'].keys()]
    D= [mydata['arena']['state'][key]['direction'] for key in mydata['arena']['state'].keys()]
    wasHit= [mydata['arena']['state'][key]['wasHit'] for key in mydata['arena']['state'].keys()]
    score = [mydata['arena']['state'][key]['score'] for key in mydata['arena']['state'].keys()]
    info = list(zip(X,Y,D,wasHit,score))
myinfo = info[7] #6 7 9 11
print(info)

def checkForward(myinfo):
    if myinfo[2]=="N":
        toNorth = []
        for x in info:
            if x[0]==myinfo[0] and x[1]>myinfo[1]:
                if x[1]-myinfo[1]<=3:
                    toNorth.append(x)
                    return "T"
    elif myinfo[2]=="S":
        toSouth = []
        for x in info:
            if x[0]==myinfo[0] and x[1]<myinfo[1]:
                if myinfo[1]-x[1]<=3:
                    toSouth.append(x)
                    return "T"
    elif myinfo[2]=="E":
        toEast = []
        for x in info:
            if x[0]>myinfo[0] and x[1]==myinfo[1]:
                if x[0]-myinfo[1]<=3:
                    toEast.append(x)
                    return "T"
    elif myinfo[2]=="W":
        toWest = []
        for x in info:
            if x[0]<myinfo[0] and x[1]==myinfo[1]:
                if myinfo[1]-x[1]<=3:
                    toWest.append(x)
                    return "T"

plt.scatter(X,Y)
plt.show()