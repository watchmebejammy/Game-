from collections import UserString
from urllib.parse import urldefrag
from time import sleep

power = False
weapon = False


def introscene():
    directions = ["left", "right", "forward", "back"]
    print("You have been teleported to a dungeon! There are doors in both directions, which do you take? ")
    userInput = ""
    while userInput not in directions:
        userInput = input("Options: left, right, forward or back? ")
        if userInput == "left":
            room2()
        elif userInput == "right":
            room3()
        else:
            print("please enter a valid input")

def room2():
    directions = ["left", "forward", "back"]
    print("you have entered a room with another two doors, which do you take? ")
    userInput = ""
    while userInput not in directions:
        userInput = input("Options: left, forward or back? ")
        if userInput == "left":
            room4()
        elif userInput == "forward":
            roomKnife()
        elif userInput == "back":
            introscene()
        else:
            print("Please enter a valid input ")
            break

def room3():
    directions = ["back"]
    print("you have reached a dead end, the wall in front of you has the numbers '9412' scraped into it with what looks like another rock ")
    userInput = ""
    while userInput not in directions:
        userInput = input("Options: back ")
        if userInput == "back":
            introscene()
        else:
            print("Please enter a valid input")
            
def room4():
  actions = ["fight","flee","run","Run"]
  global weapon
  print("A strange goul-like creature has appeared. You can either run or fight it. What would you like to do? ")
  userInput = "" 
  while userInput not in actions:
    userInput = input("Options: run or fight ")
    if userInput == "fight" and weapon == True:
      print("You kill the ghoul with the knife you found earlier. After moving forward, you find one of the exits. ")
      exitRoom()
    elif userInput == "fight" and weapon == False:
      print("You realise you are not strong enough to face it without a weapon and head back through to the last room")
      room2()
    elif userInput == "run" or "Run":
      print("You quickly step back into the previous room and shut the iron door. ")
      room2()
    else:
      print("Please enter a valid input (run, fight)")

def roomKnife():
  actions = ["pull lever", "grab knife", "go"]
  global weapon
  global power
  print("There is a knife sitting on the floor next to some sort of lever, what do you do? ")
  userInput = ""
  while userInput not in actions:
    userInput = input("Options: pull lever, grab knife, go back ")
    if userInput == "pull lever":
      power = True
      print("You hear a loud buzz in the distance, you head back through the door and notice the power has turned on.")
      room2()
    elif userInput == "grab knife":
      weapon = True
      print("You carefully pick up the knife from the floor and stare into the reflection of the blade. You feel more prepared. You head back to the last room.")
      room2()
    elif userInput == "go back":
      room2()
    else:
      print("Please enter a valid input (pull lever, grab knife, go back)")

def exitRoom():
  actions = ["9412", "exit"]
  global power
  print("There is a keypad connected to the door  ")
  userInput = ""
  while userInput not in actions:
    userInput = input("Enter a code or exit to the last room: ")
    if userInput == "9412" and power == True:
      print("Congratulations! You have escaped the dungeon!")
    elif userInput == "9412" and power == False:
      print("You need to turn the power on! It must be that lever you found. ")
      exitRoom()
    elif userInput == "exit":
      room4()
    else:
      print("please enter a valid input")


introscene()