

#Day_3 of 100 days of code

# Displaying the welcome message and mission
print("Welcome to Treasure Island. Your mission is to find the treasure!")

# Step 1: Choose a direction
direction = input("Do you want to go left or right? Type 'left' or 'right': ").lower()

if direction == "right": 
    # If the user chooses "right," the game ends
    print("Game Over. You fell into a pit!")
elif direction == "left":
    # If the user chooses "left," proceed to the next step
    swim_or_wait = input("Do you want to swim or wait? Type 'swim' or 'wait': ").lower()
    
    if swim_or_wait == "swim":
        # If the user chooses "swim," the game ends
        print("Game Over. You were attacked by a crocodile!")
    elif swim_or_wait == "wait":
        # If the user chooses "wait," proceed to the final step
        door = input("Which door do you choose? Type 'B' for Blue, 'Y' for Yellow, or 'R' for Red: ").lower()
        
        if door == "b":
            # If the user chooses the blue door, the game ends
            print("Game Over. You entered a room full of beasts!")
        elif door == "r":
            # If the user chooses the red door, the game ends
            print("Game Over. You were burned by fire!")
        elif door == "y":
            # If the user chooses the yellow door, they win
            print("You win! Congratulations, you found the treasure!")
        else:
            # If the user inputs an invalid door, display an error message
            print("Invalid response. Please restart the game and choose a valid door.")
    else:
        # If the user inputs an invalid choice in the swim or wait step
        print("Invalid response. Please restart the game and choose 'swim' or 'wait.'")
else:
    # If the user inputs an invalid choice in the direction step
    print("Invalid input. Please restart the game and choose 'left' or 'right.'")
