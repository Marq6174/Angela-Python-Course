print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
first_direction = input('Type "left" or "right"\n').lower()

if first_direction == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    wait_or_swim = input('Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    
    if wait_or_swim == "wait":
        print("You've discovered three different doors! which once will you choose?")
        door_choice = input('Please type "Red", "yellow", or "blue"\n').lower()
        
        if door_choice == "yellow":
            print("Great job! you've found the hidden treasure")
            print("You win!")
        
        elif door_choice == "red":
            print("You've been burned alive by fire!")
            print("Game Over!")
            
        elif door_choice == "blue":
            print("You've been devoured by beasts!")
            print("Game Over!")
            
        else:
            print("Game Over!")
        
    else:
        print("You've been attacked and killed by a trout!")
        print("Game Over!")
        
else:
    print("Oh no! you've fallen into a hole.")
    print("Game Over!")