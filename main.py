import asyncio
from inventory import Inventory


def display_catalogue(catalogue):
    burgers = catalogue["Burgers"]
    sides = catalogue["Sides"]
    drinks = catalogue["Drinks"]

    print("--------- Burgers -----------\n")
    for burger in burgers:
        item_id = burger["id"]
        name = burger["name"]
        price = burger["price"]
        print(f"{item_id}. {name} ${price}")

    print("\n---------- Sides ------------")
    for side in sides:
        sizes = sides[side]

        print(f"\n{side}")
        for size in sizes:
            item_id = size["id"]
            size_name = size["size"]
            price = size["price"]
            print(f"{item_id}. {size_name} ${price}")

    print("\n---------- Drinks ------------")
    for beverage in drinks:
        sizes = drinks[beverage]

        print(f"\n{beverage}")
        for size in sizes:
            item_id = size["id"]
            size_name = size["size"]
            price = size["price"]
            print(f"{item_id}. {size_name} ${price}")

    print("\n------------------------------\n")


async def main():
    inv = Inventory()
    print('Welcome to the ProgrammingExpert Burger Bar!')
    task = asyncio.create_task(inv.get_catalogue())
    print('Loading catalogue...')
    result = await task
    display_catalogue(result)
    user_entry = None

    while user_entry != 'no':
        print('Please enter the number of items that you would like to add to your order. Enter q to complete your order.')
        # items the user will be ordering. Will be reset after each order
        order = []
        # list of tasks for each item in the order. Will be reset after each order
        order_validation_tasks = []
        order_summary = []  # list of ordered items and their availability
        final_order = []  # list of ordered items which are in stock
        while True:
            # ask the user to enter an item number
            user_order = input('Enter an item number: ')

            # if user enters a character which is not a digit and the character is not 'q' they are asked to enter a valid choice
            if not user_order.isdigit() and user_order != 'q':
                print('Please enter a valid number.')

            # if the user enters a number and it is less than 0 they are asked to enter a valid choice
            elif user_order.isdigit() and int(user_order) < 0:
                print('Please enter a valid number.')

            # if the user enters a number which is higher than the number of items on the menu they will be asked to enter a valid choice
            elif user_order.isdigit() and int(user_order) > 20:
                print('Please enter a number below 21.')

            elif user_order == 'q':  # if the user enters 'q' the order is placed
                break

            else:

                task = asyncio.create_task(
                    inv.decrement_stock(int(user_order)))  # a task is created for each item on the list to decrease the stock of the item in the inventory
                # task is added to list of tasks
                order_validation_tasks.append(task)

                # each valid choice gets added to the order list
                order.append(int(user_order))

        print("Placing order ...")

        # wait for the tasks to finish
        task_result = await asyncio.gather(*order_validation_tasks)

        # create a list of tuples. each item is assigned the return value from the inventory.decrement_stock() method
        order_summary = (list(zip(order, task_result)))

        for item in order_summary:
            if item[1] == False:  # if item not in stock
                print(
                    f'Unfortunately item number {item[0]} is out of stock and has been removed from your order. Sorry!')
            else:
                # add item to final order
                final_order.append(inv.items.get(item[0]))

        burgers = list(
            filter(lambda x: x['category'] == 'Burgers', final_order))  # create list of ordered burgers
        # create list of ordered sides
        sides = list(filter(lambda x: x['category'] == 'Sides', final_order))
        # create list of ordered drinks
        drinks = list(filter(lambda x: x['category'] == 'Drinks', final_order))

        # sort burgers by highest price
        burgers.sort(key=lambda item: item.get('price'), reverse=True)
        sides.sort(key=lambda item: item.get('price'),
                   reverse=True)  # sort sides by highest price
        drinks.sort(key=lambda item: item.get('price'),
                    reverse=True)  # sort drinks by highest price

        combo = []  # create an empty list for possible combos
        total_price = []  # create an empty list for prices
        # while there is at least one item in each group of items create combos
        while len(burgers) > 0 and len(sides) > 0 and len(drinks) > 0:
            # create a combo from the most expensive items in each group
            combo_item = [burgers[0], sides[0], drinks[0]]
            combo.append(combo_item)  # add combo to list of combos
            burgers.pop(0)  # remove most expensive item from list
            sides.pop(0)  # remove most expensive item from list
            drinks.pop(0)  # remove most expensive item from list

        print(f"Here is a summary of your order: \n")
        for c in combo:  # loop through list of combos
            # get the price of the combo (15% discount)
            combo_price = sum(list(map(lambda d: d['price'] * 0.85, c)))
            print(f"${combo_price: .2f} Burger Combo")
            for i in c:
                if i['id'] < 7:
                    print('\t', i['name'])
                else:
                    print('\t', i['size'], i['subcategory'])
            # add the price of the combo to the running total
            total_price.append(combo_price)
        for b in burgers:  # print remaining items
            print(f"$ {b['price']} {b['name']}")
            # add price of remaining item to running total
            total_price.append(b['price'])
        for s in sides:  # print remaining items
            print(f"$ {s['price']} {s['size']} {s['subcategory']}")
            # add price of remaining item to running total
            total_price.append(s['price'])
        for d in drinks:  # print remaining items
            print(f"$ {d['price']} {d['size']} {d['subcategory']}")
            # add price of remaining item to running total
            total_price.append(d['price'])

        print(f''' 
        Subtotal: ${sum(total_price):.2f} \n
        Tax: ${0.05 * sum(total_price):.2f} \n
        Total: ${(sum(total_price) + (0.05 * sum(total_price))):.2f}
        ''')

        make_order = input(
            f"Would you like to purchase this order for ${(sum(total_price) + (0.05 * sum(total_price))):.2f} (yes/no)?")
        if make_order.lower() == 'yes':
            print('Thank you for your order!')
        user_entry = input('Would you like to make another order (yes/no)? ')
    print('Goodbye')

if __name__ == "__main__":
    asyncio.run(main())
