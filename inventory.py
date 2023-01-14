from tabulate import tabulate


# start by creating a class called shoe and add in the attributes
# x and y are to do with the method to return a string representation of the class
# get_cost and get_quantity return the value and amount of the chosen product
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        print(f"The {self.product} costs £{self.cost}.")

    def get_quantity(self):
        print(f"There are {self.quantity} of {self.product} left in stock.")

    def __str__(self):
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost:{self.cost}, Quantity:{self.quantity}"


shoe_list = []


def read_shoes_data():
    try:
        # Open the file in read mode
        with open('inventory.txt', 'r') as f:
            # Skip the first line
            f.readline()

            # Iterate over the remaining lines
            for line in f:
                # Strip leading and trailing whitespace from the line
                line = line.strip()

                # Split the line into individual data elements
                data = line.split(',')

                # Create a Shoe object with the data
                shoe = Shoe(data[0], data[1], data[2], data[3], data[4])

                # Append the Shoe object to the shoe_list
                shoe_list.append(shoe)
    except FileNotFoundError:
        print('Could not find the inventory file.')


def capture_shoes():
    country = input('Enter the country name: ')

    code = input('Enter the code of the shoe: ')

    product = input('Enter the name of the shoe: ')

    cost = input('Enter the price of the shoe: ')

    quantity = input('Enter the stock amount of the shoe: ')

    # Create a shoe object with the data
    shoe = country, code, product, cost, quantity

    # Append the shoe object to the shoe list
    shoe_list.append(shoe)


def view_all():
    # Create a list of lists to hold the shoe data
    shoes = []

    # Iterate over the shoes list
    for shoe in shoe_list:
        # Add the data for the current shoe to the data list
        shoes.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])

    # Use the tabulate function to create a table from the data
    table = tabulate(shoes, headers=["Country", "Code", "Product", "Cost", "Quantity"], tablefmt="fancy_grid")

    # Print the table
    print(table)


def re_stock():
    # Find the shoe with the lowest quantity
    low_qty_shoe = min(shoe_list, key=lambda x: int(x.quantity))

    # Prompt the user to enter the new quantity
    new_qty = input(f"Enter the new quantity for {low_qty_shoe.product}: ")

    # Update the quantity of the shoe
    low_qty_shoe.quantity = new_qty

    # Open the file in write mode
    with open('inventory.txt', 'w') as f:
        # Write the updated data to the file
        for shoe in shoe_list:
            f.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

    # Return the updated shoe object
    return low_qty_shoe


def search_shoe():
    # Prompt the user to enter a shoe code
    code = input('Enter the code of the shoe: ')

    # Find the shoe with the given code
    shoe = next((x for x in shoe_list if x.code == code), None)

    # Check if the shoe was found
    if shoe:
        # Print the shoe
        print(f"Code: {shoe.code}, Product: {shoe.product}, Cost: {shoe.cost}, Quantity: {shoe.quantity}")
    else:
        print(f"No shoe was found with code {code}.")


def value_per_item():
    # Iterate over the shoes list
    for shoe in shoe_list:
        # Calculate the value of the shoe
        value = float(shoe.cost) * float(shoe.quantity)

        # Print the value of the shoe
        print(f"The value of {shoe.product} is £{value}")


def highest_qty():
    # Find the shoe with the highest quantity
    high_qty_shoe = max(shoe_list, key=lambda x: int(x.quantity))

    # Print the product and quantity of the shoe
    print(f"The product with the highest quantity is {high_qty_shoe.product} with {high_qty_shoe.quantity} in stock.")
    print(f"{high_qty_shoe.product} should now be on sale.")


# ==========Main Menu=============

read_shoes_data()

while True:
    # Print the menu
    print("1. Capture shoe data")
    print("2. View all shoes")
    print("3. Re-stock shoe with the lowest quantity")
    print("4. Search for a shoe")
    print("5. Calculate the value of each shoe in stock")
    print("6. View the shoe with the highest quantity in stock")
    print("7. Exit")

    # Prompt the user to choose an option
    option = input("Enter your choice: ")

    if option == '1':
        # Capture shoe data
        capture_shoes()
    elif option == '2':
        # View all shoes
        view_all()
    elif option == '3':
        # Re-stock shoe with the lowest quantity
        re_stock()
    elif option == '4':
        # Search for a shoe
        search_shoe()
    elif option == '5':
        # Calculate the value of each shoe in stock
        value_per_item()
    elif option == '6':
        # View the shoe with the highest quantity in stock
        highest_qty()
    elif option == '7':
        # Exit the program
        break
    else:
        print("Invalid option. Please try again.")
