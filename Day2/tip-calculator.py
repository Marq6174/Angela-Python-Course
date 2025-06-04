print("Welcome to the tip calculator!")
bill_amount = float(input("What was the total bill?\n$"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
num_of_people = int(input("How many people to split the bill?\n"))

tip_amount = tip_percent / 100 * bill_amount
total_bill = bill_amount + tip_amount

print(f"Each person should pay: ${round(total_bill / num_of_people, 2)}")