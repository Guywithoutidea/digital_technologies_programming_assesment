'''
testing plant_species function
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
            print(f"The plants we currently have in stock are: {str(plants_in_stock).strip('[]')}")
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

get_plant_species()
