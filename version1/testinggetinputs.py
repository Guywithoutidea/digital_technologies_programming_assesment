import time
import os

def get_inputs():
    '''
    Asks the user what types of plants they want, how large an area they are planting,
    what density of plants they want and what their address is.
    '''
    # List of the plants currently in stock (all lower case)
    plants_in_stock = [
        "flax", "lancewood", "kanuka", "koromiko",
        "mikimiki", "kowhai", "cabbage tree", "mountain beech"]

    print("Welcome to Kakano Nursury Wanaka's quote calculation program.")
    print("First, tell us what species you will be planting. You can plant multiple species.")

    # Get the plant species the user wants.
    # later- handle multiple plant types.
    user_plants = input("Please enter the plant species, or to see what's in stock enter '?' ")
    while not isinstance(user_plants, str): # If the user's input is not a string:
        os.system('cls') # Clear the terminal
        print("That was not a valid string.")
        # The user must re-enter the species
        user_plants = input("Please enter the plant species. ")
    while not user_plants.lower() in plants_in_stock: # If the user enters something we don't sell
        os.system('cls') # Clear the terminal
        # Tell them what we do have in stock
        print("We do not have that in stock. However, we do have these plants: ", plants_in_stock)
        # The user must re-enter the species
        user_plants = input("Please enter the plant species. ")

    print("The plant species is ", user_plants) # Tell the user what plant they have selected.
    time.sleep(2) # Wait for 2 seconds
    os.system('cls') # Clear the terminal

    print("Now, tell us the density (number of plants per square metre) you want to plant at.")
    user_plant_density = input("Please enter the plant density as an integer. ")
    # If the user's input is not an integer (just text or negative)
    while not user_plant_density.isdigit():
        os.system('cls') # Clear the terminal
        print("That was not a valid integer.")
        # The user must re-enter the density
        user_plant_density = input("Please enter the plant density as an integer. ")
    # If the user enters a number greater than or equal to 0:
    while int(user_plant_density) <= 0:
        os.system('cls') # Clear the terminal
        print("Cannot plant 0 or less plants per square meter.")
        # The user must re-enter the density
        user_plant_density = input("Please enter the plant density as an integer. ")

    # Tell the user their plant density.
    print("The plant density is ", user_plant_density, " plants per square metre.")
    time.sleep(2) # Wait for 2 seconds
    os.system('cls') # Clear the terminal

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
    print("Planting ", user_planting_area, " square metres.")
    time.sleep(2) # Wait for 2 seconds
    os.system('cls') # Clear the terminal

    user_delivery_address = input("Lastly, what is your delivery address?")
    while not isinstance(user_delivery_address, str): # If the user's input is not a string:
        os.system('cls') # Clear the terminal
        print("That was not a valid string.")
        # The user must re-enter the address
    if "wanaka" in user_delivery_address.lower(): # If the user is in wanaka:
        user_in_wanaka = True # Set the user_in_wanaka bool to True

    # Tell the user their delivery address
    print("Delivery address is ", user_delivery_address)
    time.sleep(2) # Wait for 2 seconds
    os.system('cls') # Clear the terminal

    # Return the user's inputs in the form of a dictionary.
    return {"plants":user_plants, "density":int(user_plant_density),
        "area":int(user_planting_area), "in_wanaka":user_in_wanaka}

get_inputs()