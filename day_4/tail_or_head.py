import random



print("Welcome to heads o trail")

user_want_to_play = input("You wanna to play? Y or N \n").upper().strip()

if user_want_to_play == "Y":
    print("Ok, lets play")

    number_random = random.randint(1,2)

    if number_random == 1:
        print("Tail")

    else:
        print("Head")

else:
    print("Ok, bye")
