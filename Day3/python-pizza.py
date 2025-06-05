#This will be a pizza app where it calculates the price of the bill for the pizza
# and possible toppings

#Creating intro and needed variables
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L\n")
pepperoni = input("Do you want pepperoni on your pizza? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")
bill = 0


if size == "S":
  bill += 15
elif size == "M":
  bill += 20
elif size == "L":
  bill += 25
else:
  print("Please enter a valid size choice: S, M, L")
  

if pepperoni == "Y" and size == "S":
  bill += 2
elif pepperoni == "Y" and size == "M" or "L":
  bill += 3
else:
  print("Please select Y or N")
  

if extra_cheese == "Y":
  bill += 1
  
print(f"Your final bill is: ${bill}.")
