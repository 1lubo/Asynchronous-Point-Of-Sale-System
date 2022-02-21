
# Asynchronous-Point-Of-Sale-System

For this project you'll be asked to create an asynchronous point of sale/checkout system for the ProgrammingExpert Burger Bar. The ProgrammingExpert Burger Bar is a brand-new fast-food restaurant that is exclusively for ProgrammingExpert students. The program you'll create needs to be able to display all the burger bars items and collect customer orders.

This restaurant sells three types of items: Burgers, Sides and Drinks. Customers can purchase individual items or combos that are comprised of any burger, side, and drink. All items that are apart of a combo will be discounted by 15%. Your program will need to automatically group items into combos while ensuring that the most expensive items are added to combos first. For example, if a customer were to order the following items:

1. Python Burger $5.99
2. C Burger $4.99
3. Medium Fries $3.49
4. Small Fries $2.49
5. Large Coke $2.99

Then the combo that should be created would include the Python Burger, Medium Fries and Large Coke because those are the most expensive items that can be used to create a combo.

For this project you will be provided a class named `Inventory` that contains the following methods:

* `get_number_of_items()`: An async method that returns the number of unique items in the restaurants catalogue.
* `get_catalogue()`: An async method that returns a dictionary containing the restaurants catalogue. This catalogue contains the categories, subcategories (when applicable), names, prices, sizes (when applicable) and ids of items.
* `get_stock(item_id)`: An async method that returns the quantity of an item in the inventory based on it's `item_id`.
* `decrement_stock(item_id)`: An async method that decrements the count of an item in the inventory based on it's `item_id`.
* `get_item(item_id)`: An async method that returns the details about a specific item based on it's `item_id`.

Please experiment with this class to get an idea of the format of the data that is returned and possible errors you may run into. It's important to note that all this classes public methods are async, meaning you will need to use asynchronous programming in this project.

To simplify things, we have also provided a `display_catalogue(catalogue)` function in the `main.py` file that can be used to output all the items in the catalogue. The ids of items in the inventory will be the same as the item numbers that are displayed by the `display_catalogue(catalogue)` function.

Your program should start by welcoming the customer to the ProgrammingExpert Burger Bar and displaying the catalogue. Next you should collect the customers order by asking them to enter the numbers of items they would like to order (these numbers are displayed by the `show_catalogue(catalogue)` function before each item). The user should be prompted to enter one item number at a time and have their input validated (i.e., they cannot order an item that doesn't exist). There should also be no delay that causes that user to have to wait before adding another item to their order.

Once the user has selected all the items they would like in their order they should be able to place their order by entering "`q`". At this point the program will need to validate that there is sufficient stock of the items they would like to order and inform them if an item they ordered is out of stock. The process of placing and validating the order should happen as quickly as possible.

Once the users order has been placed your program should automatically create any possible combos and display an order summary. This summary should outline each combo and their price as well as all individual item and their prices. Next, your program should display the subtotal, tax and total (subtotal + tax) of this order. For this project, please use a tax rate of 5% for the entire order.

Finally, your program needs to ask the user for confirm that they would like to purchase this order. After purchasing or declining to purchase the program should ask them if they would like to order again.

See below for some examples of how this program should behave. Please ensure your outputs and prompts match exactly what is seen below.

## Sample Program Execution 1

```
Welcome to the ProgrammingExpert Burger Bar!
Loading catalogue...
--------- Burgers -----------

1. Python Burger $5.99
2. C Burger $4.99     
3. Ruby Burger $6.49
4. Go Burger $5.99
5. C++ Burger $7.99
6. Java Burger $7.99

---------- Sides ------------ 

Fries
7. Small $2.49
8. Medium $3.49
9. Large $4.29

Caesar Salad
10. Small $3.49
11. Large $4.49

---------- Drinks ------------

Coke
12. Small $1.99
13. Medium $2.49
14. Large $2.99

Ginger Ale
15. Small $1.99
16. Medium $2.49
17. Large $2.99

Chocolate Milk Shake
18. Small $3.99
19. Medium $4.49
20. Large $4.99

------------------------------

Please enter the number of items that you would like to add to your order. Enter q to complete your order.
Enter an item number: 1
Enter an item number: 10
Enter an item number: 20
Enter an item number: q
Placing order...

Here is a summary of your order:

$12.3 Burger Combo
  Python Burger
  Small Caesar Salad
  Large Chocolate Milk Shake

Subtotal: $12.3
Tax: $0.62
Total: $12.92
Would you like to purchase this order for $12.92 (yes/no)? yes
Thank you for your order!
Would you like to make another order (yes/no)? yes

Please enter the number of items that you would like to add to your order. Enter q to complete your order.
Enter an item number: 1
Enter an item number: 2
Enter an item number: 3
Enter an item number: 4
Enter an item number: 5
Enter an item number: 6
Enter an item number: 9
Enter an item number: 11
Enter an item number: 12
Enter an item number: 13
Enter an item number: 14
Enter an item number: q
Placing order...

Here is a summary of your order:

$13.15 Burger Combo
  C++ Burger
  Large Caesar Salad
  Large Coke
$12.55 Burger Combo
  Java Burger
  Large Fries
  Medium Coke
$4.99 C Burger
$5.99 Go Burger
$5.99 Python Burger
$6.49 Ruby Burger
$1.99 Small Coke

Subtotal: $51.15
Tax: $2.56
Total: $53.71
Would you like to purchase this order for $53.71 (yes/no)? yes
Thank you for your order!
Would you like to make another order (yes/no)? yes

Please enter the number of items that you would like to add to your order. Enter q to complete your order.
Enter an item number: 10
Enter an item number: 20
Enter an item number: 19
Enter an item number: 18
Enter an item number: -1
Please enter a valid number.
Enter an item number: hello
Please enter a valid number.
Enter an item number: 21
Please enter a number below 21.
Enter an item number: 22
Please enter a number below 21.
Enter an item number: 9
Enter an item number: q
Placing order...

Here is a summary of your order:

$3.49 Small Caesar Salad
$4.29 Large Fries
$3.99 Small Chocolate Milk Shake
$4.49 Medium Chocolate Milk Shake
$4.99 Large Chocolate Milk Shake

Subtotal: $21.25
Tax: $1.06
Total: $22.31
Would you like to purchase this order for $22.31 (yes/no)? yes
Thank you for your order!
Would you like to make another order (yes/no)? no
Goodbye! 
```
