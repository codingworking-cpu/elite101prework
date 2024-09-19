def startUp_sequence():
    print("hello user")
    print("\n before we let you get started")
    print("we are going to need user information")
    username = input("please enter your name:")
    userage= int(input("please enter your age:"))
    print(f"hello {username} what would you like to do?")

def Mainmenu():
  print("IMPORTANT DISCLAMINER: THIS IS A VERY EARLY BUILD OPTION 5 IS THE ONLY WORKING ONE CURRENTLY")
  print("1. Do math")
  print("2. user information")
  print("3.awnser a question")
  print("4.play a game")
  print("5. exit")
  print("6.help")
  user_choice = int(input("please type your option(numbers only)"))
  if user_choice == 5:
   print("goodbye")
   exit
startUp_sequence()
Mainmenu()
