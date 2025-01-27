#Pizza Delivery Service

pizza_cost = 0
print("Welcome to Our  Restaurants !")

# Taking user Order
size = input("What size pizza do you want? S, M, or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

# Calculating the pizza cost based on size
if size == "s":
    pizza_cost = 15
    print("Small pizza (S): $15")
elif size == "m":
    pizza_cost = 20
    print("Medium pizza (M): $20")
elif size == "l":
    pizza_cost = 25
    print("Large pizza (L): $25")
else:
    print("Invalid size selected!")
    pizza_cost = 0

# Adding cost for pepperoni
if pepperoni == "y":
    if size == "s":
        pizza_cost += 2  # Small pizzas get $2 pepperoni cost
    else:
        pizza_cost += 3  # Medium and large pizzas get $3 pepperoni cost
    print(f"Added pepperoni: ${pizza_cost}")

# Adding cost for extra cheese
if extra_cheese == "y":
    pizza_cost += 1  # Extra cheese is $1 for all sizes
    print(f"Added extra cheese: ${pizza_cost}")

# Displaying the final bill
if pizza_cost > 0:
    print(f"Your total bill is ${pizza_cost}")

print("Thanks for your patronage")