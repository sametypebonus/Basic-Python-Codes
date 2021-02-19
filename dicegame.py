import random

def rolldice():
    dicetotal = random.randint(1,6) + random.randint(1,6)
    return dicetotal


player1 = input("Input player one's name\n")
player2 = input("Input player two's name\n")

roll1 = rolldice()
roll2 = rolldice()

print("The rolls are ", roll1, "and", roll2)

if roll1 > roll2 :
    print(player1,"wins")
elif roll2 > roll1:
    print(player2,"wins")
else:
    print("Its a draw")