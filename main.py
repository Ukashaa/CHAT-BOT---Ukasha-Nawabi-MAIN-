from ukasha import ukashaChat
from mccurdy import mccurdyChat
from austin import austinChat

def chat(text):

  response = mccurdyChat(text)

  if response:
    return response

  response = austinChat(text)

  if response:
    return response

  response = ukashaChat(text)

  if response:
    return response
    
  return "I'm still learning.  Try saying hello."

while(True):
  userInput = input("You: ")
  print(chat(userInput)))