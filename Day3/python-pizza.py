#This will be a pizza app where it calculates the price of the bill for the pizza
# and possible toppings

#Creating intro and needed variables
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L\n")
pepperoni = input("Do you want pepperoni on your pizza? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")
bill = 0

#creating responses for a small pizza and asking if they want topping finally calculating bill
if size == "S":
  bill += 15
  if pepperoni == "Y":
    bill += 2
  if extra_cheese == "Y":
    bill += 1
  print(f"Your final bill is: ${bill}")

#creating responses for a medium pizza and asking if they want topping finally calculating bill
elif size == "M":
  bill += 20
  if pepperoni == "Y":
    bill += 2
  if extra_cheese == "Y":
    bill += 1
  print(f"Your final bill is: ${bill}")
  
#creating responses for a large pizza and asking if they want topping finally calculating bill
elif size == "L":
  bill += 25
  if pepperoni == "Y":
    bill += 2
  if extra_cheese == "Y":
    bill += 1
  print(f"Your final bill is: ${bill}")
  
#responding to invalid responses
else:
  print("Please enter a valid size choice: S, M, L")
  
