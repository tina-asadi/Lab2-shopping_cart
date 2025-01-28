"""
Author: Tina Asadi
Date: 2025-01-26
This program simulates a simple shopping cart.
Users can add items, specify quantities, and see the total cost.
The program uses exception handling to manage invalid inputs.
"""
print("Welcome to the Shopping Cart Program!")

# Step 1: Ask the user for the number of items
try:
    num_of_items=int(input("Please Enter the number Of items you want to buy: "))
except:
    print("Invalid input Please enter an integer number!")
else:
    print("Thank you! Number of items were successfully added.")

# step 2: Creating Lists to add items, prices and quantities
name_of_item=[]
price_of_item=[]
quantity_of_item=[]

# Creating variable to keep the total value
total_price=0

# step 3: Creating a loop to ask the user for the name, price, and quantity of each item.
for i in range(num_of_items):
    #Using Exception handeling
    try:
        #Asking the uset to enter the name
        name=input(f"Please enter the name of item {i+1}: ")
        #Adding name to the list
        name_of_item.append(name)
        #Asking the uset to enter the price
        price=float(input(f"Please enter the price of {name}: "))
         #Adding price to the list
        price_of_item.append(price)
        #Asking the uset to enter the quantity
        quantity=int(input(f"Please enter the quantity of {name}: "))
        #Adding quantity to the list
        quantity_of_item.append(quantity)
        #Calculating the total price
        total_price+=price*quantity
    except:
        print("Invalid Input! Please Enter a valid input for each part")
    #printing the total value of each item if successful
    else:
        print(f"{quantity} {name} Added to your cart at {total_price}")

#step 4: printing the total price
print(f"The total price will be {total_price} dollars! ")

    




