import random

dictUsers = {
  224784486619938817: "Tsubasa",
  173266225202200576: "Josh"

}

responseWin = {}

with open("responseWins.txt") as f:
  for line in f:
    (key, val) = line.split(" ", 1)
    responseWin.setdefault(key,[]).append(val)

responseLoss = {}
with open("responseLoss.txt") as f:
  for line in f:
    (key, val) = line.split(" ", 1)
    responseLoss.setdefault(key,[]).append(val)


def identifyUser(userID):
  return dictUsers.get(userID, "NewUser")

def respondWin(userID):
  print(responseWin)
  listOfResponses = responseWin.get(str(userID), "Have fun playing")
  if type(listOfResponses) is list:
    return random.choice(listOfResponses)
  return listOfResponses

def respondLoss(userID):
  print(responseLoss)
  listOfResponses = responseLoss.get(str(userID), "You may go")
  if type(listOfResponses) is list:
    return random.choice(listOfResponses)
  return listOfResponses

def addResponseWin(key, val):
  responseWin.setdefault(key,[]).append(val)

def addResponseLoss(key, val):
  responseLoss.setdefault(key,[]).append(val)
