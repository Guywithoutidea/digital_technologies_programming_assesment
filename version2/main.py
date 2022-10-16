'''
Native Planting Cost Calculator.
> Gets multiple plant species that the user wants to plant.
    > The user can request to see a list of available plants.
    > Rejects the user's input if it is not a string, the plant.
      is not in stock, or they have already selected the plant.

> Gets the density the user wants to plant at.
    > Rejects the user's input if it is not an integer, negative, or zero.

> Gets the area the user wants to plant.
    > Rejects the user's input if it is not an integer, negative, or zero.

> Gets the user's address.
    > Rejects the user's input if it is not a string.

> Calculates the quote cost.
    > Adds $100 delivery fee if the address is not in wanaka.

> Returns the user's quote cost and the information they entered.
'''

import time
import os

def get_plant_species():
    '''
    Ask the user what species of plants they want
    '''
    # List of the plants currently in stock (all lower case)
    plants_in_stock = [
        "flax", "lancewood", "kanuka", "koromiko",
        "mikimiki", "kowhai", "cabbage tree", "mountain beech"]

    print("Welcome to Kakano Nursury Wanaka's quote calculation program.")
    print("First, tell us what species you will be planting. You can plant multiple species.")

    # Get the plant species the user wants.
    # Initialise the list of plants the user wants
    user_plants = []
    while True:
        # Ask the user for another plant
        new_plant = ( # Parenthesis to avoid the line length limit
            input("Please enter the plant species, or to see what's in stock enter '?' ").lower())
        if new_plant == "?":
            os.system('cls') # Clear the terminal
            # Tell the user what plants we have in stock
            print(f"The plants we currently have in stock are: {plants_in_stock}")
            continue
        if not isinstance(new_plant, str): # If the user's input is not a string:
            os.system('cls') # Clear the terminal
            print(f"{new_plant} is not a valid string.")
            continue
        if not new_plant in plants_in_stock: # If the user enters something we don't sell
            os.system('cls') # Clear the terminal
            # Tell them what we do have in stock
            print(f"We do not have {new_plant} in stock. However, we do have: {plants_in_stock}")
            continue
        if new_plant in user_plants:
            os.system('cls') # Clear the terminal
            print(f"You have already selected the {new_plant} plant type- select a different one.")
            continue

        user_plants.append(new_plant) # Add the new plant to the user_plants string.
        print(f"Added {new_plant}") # Tell the user what plant they have added.
        time.sleep(1) # Wait for 1 seconds
        os.system('cls') # Clear the terminal
        if input("Select another plant? [y/n]").lower() == "y":
            continue
        return user_plants

def get_plant_density():
    '''
    Ask the user what density of plants they want
    '''
    print("Now, tell us the density (number of plants per square metre) you want to plant at.")
    user_plant_density = input("Please enter the plant density as an integer. ")
    # If the user's input is not an integer (just text or negative)
    while not user_plant_density.isdigit():
        os.system('cls') # Clear the terminal
        print(f"{user_plant_density} was not a valid integer.")
        # The user must re-enter the density
        user_plant_density = input("Please enter the plant density as an integer. ")
    # If the user enters a number greater than or equal to 0:
    while int(user_plant_density) <= 0:
        os.system('cls') # Clear the terminal
        print("Cannot plant 0 or less plants per square meter.")
        # The user must re-enter the density
        user_plant_density = input("Please enter the plant density as an integer. ")

    # Tell the user their plant density.
    print(f"The plant density is {user_plant_density} plants per square metre.")
    time.sleep(1) # Wait for 1 seconds
    os.system('cls') # Clear the terminal
    return int(user_plant_density)

def get_planting_area():
    '''
    Ask the user how large an area they want to plant
    '''
    print("Next, tell us the area of land you want to plant in.")
    user_planting_area = input("Please enter the area you want to plant. ")
    # If the user's input is not an integer:
    while not user_planting_area.isdigit():
        os.system('cls') # Clear the terminal
        print("That was not an integer.")
        # The user must re-enter the area
        user_planting_area = input("Please enter the area you want to plant. ")
    # If the user enters a number greater than or equal to 0:
    while int(user_planting_area) <= 0:
        os.system('cls') # Clear the terminal
        print("Cannot plant 0 or less square meters.")
        # The user must re-enter the density
        user_planting_area = input("Please enter the area you want to plant. ")

    # Tell the user their planting area
    print(f"Planting {user_planting_area} square metres.")
    time.sleep(1) # Wait for 1 seconds
    os.system('cls') # Clear the terminal
    return int(user_planting_area)

def get_address():
    '''
    Ask the user what their address is
    '''
    user_delivery_address = input("Lastly, what is your delivery address?")
    while not isinstance(user_delivery_address, str): # If the user's input is not a string:
        os.system('cls') # Clear the terminal
        print("That was not a valid string.")
        # The user must re-enter the address

    print("Delivery address is ", user_delivery_address)
    time.sleep(2) # Wait for 2 seconds
    os.system('cls') # Clear the terminal
    return user_delivery_address

# Get the details of the quote from the user using the above functions
plants = get_plant_species()
density = get_plant_density()
area =  get_planting_area()
address = get_address()

# Calculate the cost using our cost formula with the user's details
cost = (area * density * 6.5) + 200
# If the user is not in Wanaka:
if not "wanaka" in address.lower():
    cost += 100 # add the 100 delivery fee

# Tell the user their quote
print(f"Your quote is: ${cost} to plant {area}m^2 of:")
# Bullet point list of plants
for species in plants:
    print(f"> {species}")
print(f"At a density of {density} plants per square metre.")
print(f"Delivering to {address}")
time.sleep(8)
