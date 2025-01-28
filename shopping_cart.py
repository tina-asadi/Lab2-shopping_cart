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

