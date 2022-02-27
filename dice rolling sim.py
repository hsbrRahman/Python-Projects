import random

play = input("Do you want to roll some dice?: ").upper()
while play == "Y":

    # Gnenerates a random number
    # between 1 and 6 (including
    # both 1 and 6)
    num = random.randint(1, 6)
    if num == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    if num == 2:
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
    if num == 3:
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
    if num == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    if num == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    if num == 6:
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")
    play = input("type y to play again or n to exit: ").upper()
    print("\n")
print("Thanks\n")
