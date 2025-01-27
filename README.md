# **Day 3 of 100 Days of Code**  
## **Treasure Island Game**

### **Project Description**
The **Treasure Island Game** is a simple text-based adventure game written in Python. The player navigates through a series of choices to find the treasure. Each decision either brings the player closer to the treasure or ends the game. This project helps reinforce basic Python concepts like conditional statements and user input handling.

---

### **How the Game Works**
1. The player is welcomed to the game and informed of their mission: **Find the treasure!**
2. The player is presented with a series of choices:
   - **Step 1**: Choose a direction (`left` or `right`).
   - **Step 2**: Decide to either swim or wait (`swim` or `wait`).
   - **Step 3**: Pick a door to enter (`Blue`, `Yellow`, or `Red`).
3. Based on the player's choices, the game either ends in success (treasure found) or failure (game over).

---

### **Code**
```python
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
```

---

### **How to Play**
1. Run the script in Python:
   ```bash
   python treasure_island.py
   ```
2. Follow the instructions and make your choices by typing the provided options (e.g., `left`, `swim`, or `Y`).
3. Your choices will determine whether you find the treasure or face an untimely end.

---

### **Example Gameplay**
**Input:**
```
Do you want to go left or right? Type 'left' or 'right': left  
Do you want to swim or wait? Type 'swim' or 'wait': wait  
Which door do you choose? Type 'B' for Blue, 'Y' for Yellow, or 'R' for Red: y
```

**Output:**
```
Welcome to Treasure Island. Your mission is to find the treasure!  
You win! Congratulations, you found the treasure!
```

---

### **Skills Practiced**
- Using **conditional statements** (`if`, `elif`, `else`) to create decision-making logic.
- Handling **user input** with the `input()` function.
- Working with **string methods** like `.lower()` to handle case-insensitive inputs.
- Structuring code into logical steps to create an interactive program.

---

### **Potential Improvements**
- Add more choices and storylines to make the game longer and more engaging.
- Implement input validation to handle unexpected inputs more gracefully.
- Add ASCII art or animations for better visuals.
- Store the player's choices and results in a log file for review.
- Create a graphical version using a GUI library like **Tkinter** or **PyGame**.

---

Have fun adventuring on Treasure Island and finding the treasure! 🏴‍☠️
