# Shoe Inventory Management System
This is a simple program that allows you to manage a list of shoe products, including adding new products, viewing all products, restocking a product, and searching for a product by its code. The program reads the initial data from a file called inventory.txt and writes the updated data back to the file.

## Getting Started
These instructions will help you get the program running on your local machine.

### Prerequisites
You will need to have Python 3 and the tabulate library installed on your machine. You can install the tabulate library using pip:

pip install tabulate

### Running the Program
1. Clone or download the repository to your local machine.
2. In the root directory of the project, you will find a file called inventory.txt, this file contains the initial data for the shoe products.
3. Run the program by executing the following command in the terminal:

python inventory_manager.py

The program will prompt you to select an operation to perform.

#### Adding a new product
Select option 1 to add a new product. You will be prompted to enter the following information:

- Country
- Code
- Product
- Cost
- Quantity

#### Viewing all products
Select option 2 to view all products. A table of all products will be displayed in the terminal.

#### Restocking a product
Select option 3 to restock a product. The program will find the product with the lowest quantity and prompt you to enter a new quantity for that product.

#### Searching for a product
Select option 4 to search for a product. You will be prompted to enter a code, the program will search for a product with that code and display the product details if found.

### Built With
Python - The programming language used
tabulate - Used to create tables for displaying data in the terminal
