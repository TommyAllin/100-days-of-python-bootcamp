# tip Calculator

print("Welcome to tip calculator, Tomas!\n")
## total de la cuenta
total_bill = float(input("What was the total bill?\n"))
## calculos de tip_give

tip_give = float(input("How much tip would you like to give? in percentage\n"))
tip_give_percent = tip_give / 100
tip_give_is = 1 + tip_give_percent
## cantidad de personas
People_number = int (input("How many people would pay the bill\n"))
## haciendo calculos
result = total_bill * tip_give_is / People_number
result_final = round(result, 2)
print(f"Each person should pay : {result_final} $")
