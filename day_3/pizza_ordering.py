print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: \n").strip().upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").strip().upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").strip().upper()
bill = 0


if size in ("S", "M", "L"):
    if size == "S":
        bill = 5
    elif size == "M":
        bill = 8
    elif size == "L":
        bill = 10



    if pepperoni == "Y":
            bill += 3
    else:
        bill += 0

    if extra_cheese == "Y":
        bill += 1



    total_bill = bill
    print(f"Your total bill is {total_bill}")

else:
    print("cant order")
