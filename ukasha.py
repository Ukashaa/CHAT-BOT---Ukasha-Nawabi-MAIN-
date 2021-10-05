import random 
import re


closingOptions = ["finally.", "you're leaving? thank god.", "*sighs in relief*", "bye bye stinky", "Leave mortal"]

helloOptions = ["hello", "hi", "hey", "yo", "hola", "namaste", "sup"]

sarGreetings = ["It's SoOoOo good to see you...", "Oh it's you...", "iM sO GlAd tO sEe yOU!", "*turns head the other way*"]

newGreeting = "What(('s)|(+is))+(your|ur)+name(.+)"

#A secret is hidden within this name, can you figure it out? ;D
newResponce = "Banshi Ukanawa" 

myFavorites = {"movie": "nacho lebre",
              "animal": "cats",
              "food": "shawarma",
              "color": "blue"}

def ukashaChat(text):

  text = text.replace(",", "")
  text = text.replace(".", "")
  text = text.replace("!", "")
  text = text.replace("?", "")

  textLower = text.lower()


  myMatchObject = re.match("what(('s)|([\s]+is))[\s]+your[\s]+favorite[\s]+(.+)", textLower)
  if myMatchObject:
    favoriteIndex = myMatchObject.group(4)
    if favoriteIndex in myFavorites:
      return "My favorite {} is {}".format(favoriteIndex, myFavorites[favoriteIndex])

  words = text.split(" ")
  for word in words: 
    if word.lower() in helloOptions:
      return random.choice(sarGreetings)
    if word.lower() in newGreeting:
      return newResponce 
    if word.lower() == "cya":
      return random.choice(closingOptions)
  
  else:
    return None