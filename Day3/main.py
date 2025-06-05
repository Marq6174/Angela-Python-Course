print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm\n"))

if height >= 120:
  print("You can enter!")
  age = int(input("What is your age?\n"))
  if age > 18:
    print("Your ticket price will be $12")
  elif age < 12:
    print("Your ticket price will be $5")
  else:
    print("Your ticket price will be $7")
else:
  print("You can't enter the ride sorry :( you're too short")

