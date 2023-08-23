import csv
from datetime import datetime


# Determine the amount of products on stock by product name
# Condition is if they are in stock on the offset date
# Condition is that the product has not passed it expiration date
def inventory_update(product_name):

    # Read offset date for view of inventory report
    with open('offset_date.txt', 'r') as offset_date_input:
        offset_date_read = str(offset_date_input.read())
        # Set offset_date to datetime format
        offset_date = datetime.strptime(offset_date_read, '%Y-%m-%d')
    offset_date_input.close()

    # Calculate the amount of bought products
    # Calculate the purchase price of the product
    # Open bought.csv in reading modus
    with open('bought.csv', 'r') as bought_input:
        next(bought_input)
        bought_reader = csv.reader(bought_input)
        amount_bought = 0
        purchase_price = 0.0
        for row in bought_reader:
            if product_name == row[1]:
                # Set buy_date and expiration_date to datetime format
                buy_date = datetime.strptime(row[3], '%Y-%m-%d')
                expiration_date = datetime.strptime(row[5], '%Y-%m-%d')
                # Check the buy_date and off_set date
                if buy_date <= offset_date and offset_date < expiration_date:
                    # Calculates the total amount of the product
                    amount_bought = amount_bought + int(row[2])
                    # Calculates the total purchase price of the product
                    purchase_price = round(amount_bought * float(row[4]), 1)
        bought_input.close()

    # Find the id of the product by reading product_id.csv
    with open('product_id.csv', 'r') as product_id_input:
        product_id_read = csv.reader(product_id_input)
        next(product_id_input)
        for row in product_id_read:
            if product_name == row[1]:
                id_product = row[0]
    product_id_input.close()

    # Calculate the amount of sold products
    # Calculate the selling price of the product
    # Calculate the total of the product on stock
    # Open sold.csv in reading modus
    with open('sold.csv', 'r') as sold_input:
        sold_reader = csv.reader(sold_input)
        amount_sold = 0
        sell_price = 0.0
        for row in sold_reader:
            # Check for each existing product if it was sold
            if id_product == row[1]:
                # Set sell_date to datetime format
                sell_date = datetime.strptime(row[3], '%Y-%m-%d')
                # Check sell date is before offset date for correct view of report
                if sell_date <= offset_date:
                    # Calculate the total selling proce
                    amount_sold = amount_sold + int(row[2])
                    sell_price = round(amount_sold * float(row[4]), 1)
        # Calculate the total amount of the product in stock
        in_stock = amount_bought - amount_sold
    sold_input.close()

    # Append the row to inventory.csv by writing
    with open('inventory.csv', 'a', newline='') as inventory_input:
        inventory_writer = csv.writer(inventory_input)
        # Write the row with alle the collected and calculated values
        product_row = [id_product, product_name, amount_bought,
                       purchase_price, amount_sold, sell_price, in_stock]
        inventory_writer.writerow(product_row)
    inventory_input.close()
