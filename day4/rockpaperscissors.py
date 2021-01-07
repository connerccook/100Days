import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

moves = (rock, paper, scissors)
yourMove = input("Enter either rock, paper, or scissors: ")
computerMove = moves[random.randint(0, 2)]
print(computerMove)
if yourMove == "scissors":
    print(moves[2])
    if(computerMove == yourMove):
        print("Draw")
    elif(computerMove == rock):
        print("You Lost")
    else:
        print("You won")
elif yourMove == "rock":
    print(moves[0])
    if(computerMove == yourMove):
        print("Draw")
    elif(computerMove == "paper"):
        print("You Lost")
    else:
        print("You won")
elif yourMove == "paper":
    print(moves[1])
    if(computerMove == yourMove):
        print("Draw")
    elif(computerMove == "scissors"):
        print("You Lost")
    else:
        print("You won")
