print("Welcome to Treasure Island")
direction = input("Left or Right? ")
if(direction == "Right"):
    print("Game over")
else:
    decision = input("swim or wait")
    if(decision == "swim"):
        print("game over")
    else:
        color = input("Which door? Red, Blue, or Yellow")
        if(color == "Yellow"):
            print("You win")
        else:
            print("Game over")
