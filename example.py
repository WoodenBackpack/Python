import csvReader
from math import floor

input = csvReader.readFromFile("./players.csv")

def inchToCm(inches):
  return inches * 2.54

def lbsToKgs(lbs):
  return lbs * 0.45

def isNone(el):
  if type(el) == str:
    el = el.strip()
  if el == "" or el == " ":
    return "-1"
  return el

output = []
identifier = 0
for iterator in input.records:
  playerDict = {}
  playerDict["Id"] = isNone(identifier)
  playerDict["Name"] = isNone(iterator[0])
  playerDict["Team"] = isNone(iterator[1])
  playerDict["Position"] = isNone(iterator[2])
  playerDict["Height"] = inchToCm(float(isNone(iterator[3].replace(',', ''))))
  playerDict["Weight"] = lbsToKgs(float(isNone(iterator[4].replace(',', ''))))
  playerDict["Age"] = floor(float((isNone(iterator[5]))))
  identifier += 1
  output.append(playerDict)

def printPlayerWithId(ident):
  for x in output:
    if x["Id"] == ident:
      print(x)
      return

printPlayerWithId(20)

