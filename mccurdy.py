import random


greetingOptions = ["hello", "yo", "hola", "namaste"]


def mccurdyChat(text):
  text = text.replace(",", "")
  text = text.replace(".", "")
  text = text.replace("!", "")

  words = text.split(" ")
  for word in words:
    if word.lower() in greetingOptions:
      return random.choice(greetingOptions).capitalize()
    
    if word.lower() == "bye":
      return "see ya"
  
  return None
