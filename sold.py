import csv
import create_id
import inventory
import offset_date

# Checks if product exist and if there enough products on stock
def check_inventory_sold_product(product_name, amount, sell_price):
    inventory.update_inventory()
    # Sets date to the sell date to check if the product is on stock on that date
    sell_date = offset_date.offset_date(0)
    inventory_stock = 0
    with open('inventory.csv', 'r') as inventory_input:
        inventory_reader = csv.reader(inventory_input)
        for row in inventory_reader:
            if product_name == row[1]:
                # Determine the current stock
                inventory_bought = int(row[2])
                inventory_stock = int(row[6])
        inventory_input.close()

    # Find the id of the product by reading product_id.csv
    with open('product_id.csv', 'r') as product_id_input:
        product_id_read = csv.reader(product_id_input)
        next(product_id_input)
        for row in product_id_read:
            if product_name == row[1]:
                id_product = row[0]
        product_id_input.close()

    with open('sold.csv', 'r') as sold_input:
        sold_read = csv.reader(sold_input)
        next(sold_input)
        total_sold = 0
        # Count the total amount sold products including the one in the future
        for row in sold_read:
            if id_product == row[1]:
                total_sold = total_sold + int(row[2])
        # Cheks if there are products in stock at all
        if inventory_stock > 0:
            # Chcecks if it possible to sell products on the current date
            # Takes into account with sold products in the future
            current_stock = inventory_bought - total_sold
            if int(amount) <= current_stock:
                append_sold_product(product_name, amount, sell_date, sell_price)
            else:
                if int(amount) <= inventory_stock:
                    print(f'To many {product_name} sold in the future!')
                else:
                    print(f'Not enough {product_name} in stock')
        else:
            print(f'No {product_name} in stock!')
        sold_input.close()


# Appends selling data to sold.csv
def append_sold_product(product, amount, sell_date, sell_price):
    # Open sold.csv in appending modus
    with open('sold.csv', 'a', newline='') as sold_input:
        field = ['id', 'stock_id', 'amount', 'sell_date', 'sell_price']
        sold_writer = csv.DictWriter(sold_input, fieldnames=field)
        # Make product row with a new id for each new row
        # Retrieves matching product id from product_id module
        product_row = {
            'id': create_id.create_new_id_sold(),
            'stock_id': return_product_id(product),
            'amount': amount,
            'sell_date': sell_date,
            'sell_price': sell_price,
            }
        sold_writer.writerow(product_row)
        sold_input.close()
    # Update inventory with new data
    inventory.update_inventory()


# Returns the id of the product
def return_product_id(product):
    with open('product_id.csv') as file:
        product_list = list(csv.reader(file))
        for row in product_list:
            if product in row:
                return row[0]
        file.close()
