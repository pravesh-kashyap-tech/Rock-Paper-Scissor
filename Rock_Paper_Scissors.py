import random
rock ="""
        __________
_______|    _______)
          (________)
          (________)
          (______)
-----.____(____)"""

paper = """
        ________
_______|     ____ )____
               ________)
               _________)
               _______)
-----._____________)"""

scissor = """
           _________
__________|    ______)_____
                  _________)
              ______________)
              (______)
------._______(____)"""

game_images = [ rock, paper, scissor]
user_choice = int(input("Enter your choice: \n0 for Rock. \n1 for Paper. \n2 for Scissor.\n"))
if user_choice>2 and user_choice<0:
    print("You entered a invalid number, you loose....")
else:
    print(game_images[user_choice])
    ai_choice = random.randint(0,2)
    print("Computer choice is:",ai_choice)
    print(game_images[ai_choice])
    if user_choice == ai_choice:
        print(" Tie.....")

    elif user_choice ==0 and ai_choice == 2:
        print("You Win.....")
    elif user_choice == 2 and ai_choice == 0:
        print(" You loose....")
    elif user_choice > ai_choice:
        print("You Win....")
    else : # user_choice < ai_choice:
        print("Yow Loose....")
