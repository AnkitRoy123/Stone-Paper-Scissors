import random
while True:
 x = ["Stone", "Paper", "Scissors"]
 x = random.choice(x)
 print("Choose any one :--")
 print("Stone, Paper and Scissors:")
 y = str(input(""))
 if x==y:
    print("Draw")
 else:
    if (x == "Stone" and y == "Paper"):
     print("Win")
    elif (x == "Paper" and y == "Stone"):
     print("Lose")
    elif (x == "Stone" and y == "Scissors"):
     print("Lose")
    elif (x == "Scissors" and y == "Paper"):
     print("Lose")
    elif (y == "Stone" and x == "Scissors"):
     print("Win")
    elif (x == "Scissors" and y == "Paper"):
     print("Win")
    elif y == "exit":
     break
    else:
     print("Choose any one into\nStone, Paper and Sci>
     print("If you want to quit please enter exit.")
