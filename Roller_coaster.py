#Roller Coaster Cmpany

bill=0
print("Welcome to roller!")
height=int(input("What is your height in cm? 🛴 "))
if height>=120:
    print("You can ride the roller coaster ✈🌴 ")
    age=int(input("What is your age? "))
    if age <= 12:
        bill=5
        print("child ticket is $5")
    elif age <= 18:
        bill=7
        print("Youth ticket is $7")
    elif age >=45 and age <=55:
    #Or elif 45 <=age <=55
        bill=0
        print("Everything is okay. Have a free ride on us ! ")
    else:
        bill=12
        print("Adult ticket is $12 ")
    wants_snack=input("Do you want a snack ? Type Y for Yes, Type N for no : ").lower()
    if wants_snack == "y":
        #Add $3 to the bill
        bill +=3

    print(f"final bill is ${bill}")

else:
    print("Sorry you have to grow taller before you can ride")