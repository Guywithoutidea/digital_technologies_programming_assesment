'''
Native Planting Cost Calculator for Kakano Nursery WITH AN INTERFACE!
> Gets multiple plant species that the user wants to plant through check boxes.
    > No need to validate the input as it is multiple choice.
> Gets the density the user wants to plant at from a text field.
    > Rejects the user's input if it is not an integer, negative, or zero.
    > Tells the user how to fix their error.
    > Now accepts floats!.
> Gets the area the user wants to plant  from a text field..
    > Rejects the user's input if it is not an integer, negative, or zero.
    > Tells the user how to fix their error.
    > Now accepts floats!
> Gets the user's address from a text field..
    > Rejects the user's input if it is not a string.
    > Tells the user how to fix their error.
> Calculates the quote cost when the user presses a button.
    > Adds $100 delivery fee if the address is not in wanaka.
> Returns the user's quote cost and the information they entered in a label.
> The user can do this as many times as they want.
> The user can review information about this quote in a .txt receipt if they choose to print it
    > The date of the quote
    > The plants they selected
    > The plant density
    > The planting area
    > The number of plants they would recive
    > The delivery address
    > The total cost of the quote
Please note:
Prefixes for widget names like ent, btn, and lbl are conventions for tkinter programs.
Yes, I am naming my variables appropriately
'''
import tkinter as tk
from tkinter.filedialog import asksaveasfile
from datetime import date

# Initialise the list of plants in stock
plants_in_stock = [
    "flax", "lancewood", "kanuka", "koromiko",
    "mikimiki", "kowhai", "cabbage tree", "mountain beech"]

# Maximum number of plants we will sell to the user
MAX_PLANTS = 3000

# Initialise user_plants
user_plants = []

def plant_species_handler(plant_species, value):
    '''
    Event handler for the plant species checkboxes
    '''
    # If the user has deselected the checkbox and the plant is currently in user_plants
    if value.get() == 0 and plant_species in user_plants:
        user_plants.remove(plant_species) # Remove the plant from the list user_plants
    # If the user has selected the checkbox
    if value.get() == 1:
        user_plants.append(plant_species) # Add that plant to the list user_plants

def get_quote():
    '''
    Command called when user presses the calculate button
    '''
    # Get our user's values from the entry boxes
    area_string = ent_area.get()
    density_string = ent_density.get()
    address = ent_address.get()

    # Intialise our two floating point values for area and density

    area_float = 0
    density_float = 0
    inputs_invalid = False # Keeps track of whether there are any invalid inputs

    # Area validation code. If it all checks out, area_float is valid and a float.
    # First, we reset the lbl_area to it's normal value.
    lbl_area.config(fg="white", text="Enter the area you wish to plant in m^2.")
    try:
        # Try to convert it to a floating point number
        area_float = float(area_string)
        # If that suceeds, check if the float is greater than zero.
        if area_float <= 0:
            inputs_invalid = True # Set inputs invalid to true
            # Tell the user their mistake
            lbl_area.config(fg="red",
                text="""Enter the area you wish to plant in m^2.
                    \nYou cannot plant 0 or less m^2 of trees.""")
    # If the area cannot be converted into a float (throws one of the below errors)
    except (TypeError, ValueError):
        inputs_invalid = True # Set inputs invalid to true
        # Tell the user their mistake
        lbl_area.config(fg="red", text="""Enter the area you wish to plant in m^2.
            \nPlease enter a valid number, like 2, or 0.6.""")

    # Density validation code. If it all checks out, density_float is a valid float.
    # First, we reset the lbl_area to it's normal value.
    lbl_density.config(fg="white", text="Enter the density of plants you want per m^2.")
    try:
        # Try to convert it to a floating point number
        density_float = float(density_string)
        # If that suceeds, check if the float is greater than zero.
        if density_float <= 0:
            inputs_invalid = True # Set inputs invalid to true
            # Tell the user their mistake
            lbl_density.config(fg="red",
                text="""Enter the density of plants you want per m^2.
                    \nYou cannot plant 0 or less trees per m^2.""")
    # If the area cannot be converted into a float (throws one of the below errors)
    except (TypeError, ValueError):
        inputs_invalid = True # Set inputs invalid to true
        # Tell the user their mistake
        lbl_density.config(fg="red", text="""Enter the density of plants you want per m^2.
            \nPlease enter a valid number, like 2, or 0.6.""")

    # Address validation code.
    # First, we reset the lbl_address to it's normal value.
    lbl_address.config(fg="white", text="Enter the delivery address.")
    # If the user has not entered an address:
    if not address:
        inputs_invalid = True # Set inputs invalid to true
        # Emphasise the delivery address field
        lbl_address.config(fg="red", text="Enter the delivery address.")

    # Plant species validation code.
    # First, we reset the lbl_plant_types to it's normal value.
    lbl_plant_types.config(fg="white", text="Please select the species\nyou wish to purchase.")
    # If the user has not entered any plant species:
    if not user_plants:
        inputs_invalid = True # Set inputs invalid to true
        # Emphasise the plant species field
        lbl_plant_types.config(fg="red", text="Please select the species\nyou wish to purchase.")

    # Calculate the number of plants the user is buying.
    # You cannot buy half a plant, so convert the float to int
    number_of_plants = int(area_float * density_float)
    # If the user is trying to buy more plants than this:
    if number_of_plants > MAX_PLANTS:
        inputs_invalid = True # Set inputs invalid to true
        lbl_number_of_trees.config(fg = "red",
            text=f"We can't sell you {number_of_plants} plants! Maximum 3000.")

    # If none of the inputs are invalid:
    if not inputs_invalid:
        lbl_number_of_trees.config(fg = "white",
            text=f"You're buying {number_of_plants} plants.")
        # Calculate the user's quote
        cost = calculate_quote(number_of_plants, address)
        # Update the cost label
        lbl_quote.config(text=f"${cost}")
        # Allow the user to save a receipt with this valid information
        btn_receipt.config(text="Save a receipt!",
            command=lambda:
            save_receipt(area_string, density_string, number_of_plants, address, cost),
            relief=tk.RAISED)
    # If one or more input is invalid:
    else:
        # Prevent the user from saving a receipt with this information
        btn_receipt.config(text="Cannot save a receipt.",
        command=None,
        relief=tk.FLAT)

def calculate_quote(number_of_plants, address):
    '''
    Calculate the cost using our cost formula with the user's details
    '''
    cost = (number_of_plants * 6.5) + 200
    # If the user is not in Wanaka:
    if not "wanaka" in address.lower():
        cost += 100 # add the 100 delivery fee

    return cost

def save_receipt(area, density, number_of_plants, address, cost):
    '''
    Allows the user to save a text file receipt with the information about their quote
    '''
    # Get the current date to use in the file
    current_date = date.today().strftime("%d-%m-%Y")
    # Open a file dialog asking the user where they want to save the receipt.
    receipt_file = asksaveasfile(mode="a", # The file object is opened in append mode
        initialfile=f"kakano_nursery_quote_receipt_{current_date}.txt",
        defaultextension=".txt",
        filetypes=[("Text Document", "*.txt"),])

    # If they are saving over an existing file, delete the text already there
    receipt_file.truncate(0)
    # Write the receipt to the file
    receipt_file.write(f"""Kakano Nursery Quoting Software.
        \nDate: {current_date}
        \nPlants selected:\n""")
    # Bullet point list of all the plants the user is buying
    for each in user_plants:
        receipt_file.write(f" > {each}\n")
    # Rest of the receipt info
    receipt_file.write(f"""
        \nSize of the area being planted: {area} m^2.
        \nDensity of plants: {density} plants per m^2.
        \nThis order is for: {number_of_plants} plants.
        \nDelivery Address: {address}.
        \nTotal Cost: ${cost}""")
    # Close the write stream
    receipt_file.close()

# Tkinter code!

# Initialise the root window
rootwindow =  tk.Tk()
# Give it a name
rootwindow.title("Kakano Nursery Quoting Software")
# Prevent it from being resized horizontally or vertically
rootwindow.resizable(False, False)

# Initialising the widgets:

# Initialise the main frame. #222 is a very dark gray
frm_mainframe = tk.Frame(master=rootwindow,
    bg="#222")
frm_mainframe.grid(sticky="nsew") # Make it stretch across the screen

# The title
lbl_title = tk.Label(master=frm_mainframe,
    text="Kakano Nursery",
    font=("Cascadia Code Light", 35),
    fg="white",
    bg="#222",
    height=2)
lbl_title.grid(row=1, column=1)

# The blurb below the title
lbl_blurb = tk.Label(master=frm_mainframe,
    text="""Welcome to Kakano Nursery Wanaka's quote calculation program.
        \nTo recieve your quote, please fill out the following fields.""",
    font=("Cascadia Code Light", 12),
    fg="white",
    bg="#222",
    height=4,
    padx=15)
lbl_blurb.grid(row=2, column=1)

# The frame for the plant checkboxes
frm_checkbuttons = tk.Frame(master=rootwindow,
    bg="#222",
    borderwidth=5,
    relief=tk.SUNKEN)
frm_checkbuttons.grid(sticky="ew", row=3)

# The instructions for the plant types checkboxes
lbl_plant_types = tk.Label(master=frm_checkbuttons,
    text="""Please select the species\nyou wish to purchase.""",
    font=("Cascadia Code Light", 10),
    fg="white",
    bg="#222",
    height=4,
    padx=15)
lbl_plant_types.grid(row=0, column=0, sticky="w")

# A loop adding each of the plants in stock to the list of checkboxes
for plant in plants_in_stock:
    i = tk.IntVar() # Initialise an on/off variable
    tk.Checkbutton(master=frm_checkbuttons,
        text=plant,
        bg="#222",
        fg="white",
        activebackground="#222",
        activeforeground="white",
        selectcolor="#222",
        variable=i,
        padx=15,
        pady=1,
        font=("Cascadia Code Light", 10),
        # The command executed whenever the checkbox is clicked. Lambda used to pass arguments on
        command=lambda arg1 = plant, arg2 = i: plant_species_handler(arg1, arg2)).grid(sticky="w")

# The frame for the plant density, planting area, and address fields
frm_fields = tk.Frame(master=rootwindow,
    bg="#222",
    borderwidth=5,
    relief=tk.SUNKEN,
    padx=15,
    pady=30)
frm_fields.grid(sticky="ew", row=4, column=0)

# Label on top of the planting area field
lbl_area = tk.Label(master=frm_fields,
    text="""Enter the area you wish to plant in m^2.""",
    font=("Cascadia Code Light", 10),
    fg="white",
    bg="#222",
    height=4)
lbl_area.grid(sticky="sw")

# The planting area field
ent_area = tk.Entry(master=frm_fields,
    width=15,
    font=("Cascadia Code Light", 10))
ent_area.grid(sticky="w")

# Label on top of the planting density field
lbl_density = tk.Label(master=frm_fields,
    text="""Enter the density of plants you want per m^2.""",
    font=("Cascadia Code Light", 10),
    fg="white",
    bg="#222",
    height=4)
lbl_density.grid(sticky="sw")

# The planting density field
ent_density = tk.Entry(master=frm_fields,
    width=15,
    font=("Cascadia Code Light", 10))
ent_density.grid(sticky="w")

# Label on top of the address field
lbl_address = tk.Label(master=frm_fields,
    text="""Enter the delivery address.""",
    font=("Cascadia Code Light", 10),
    fg="white",
    bg="#222",
    height=4)
lbl_address.grid(sticky="sw")

# The address field
ent_address = tk.Entry(master=frm_fields,
    width=60,
    font=("Cascadia Code Light", 10))
ent_address.grid(sticky="w")

# The frame for the button and quote return field
frm_calculate = tk.Frame(master=rootwindow,
    bg="#222",
    borderwidth=5,
    padx=15,
    pady=30,
    relief=tk.SUNKEN)
frm_calculate.grid(sticky="ew", row=5)

# The big button saying calculate my quote!
btn_calculate = tk.Button(master=frm_calculate,
    text="Calculate my quote!",
    font=("Cascadia Code Light", 12),
    bg="#ccc",
    fg="black",
    borderwidth=5,
    relief=tk.RAISED,
    width=20,
    command= get_quote)
btn_calculate.pack()

# The label displaying the quote. Empty by default.
lbl_quote = tk.Label(master=frm_calculate,
    text="$ ...",
    bg="#222",
    fg="white",
    font=("Cascadia Code Light", 12),
    borderwidth=7,
    relief=tk.SUNKEN,
    width=20)
lbl_quote.pack()

btn_receipt = tk.Button(master=frm_calculate,
    text="Cannot save a receipt.",
    bg="#222",
    fg="white",
    activebackground="#222",
    activeforeground="white",
    font=("Cascadia Code Light", 12),
    borderwidth=5,
    relief=tk.FLAT,
    width=20)
btn_receipt.pack()

lbl_number_of_trees = tk.Label(master=frm_calculate,
    text="",
    bg="#222",
    fg="white",
    font=("Cascadia Code Light", 12))

lbl_number_of_trees.pack()
# Loop the tkinter code
rootwindow.mainloop()
