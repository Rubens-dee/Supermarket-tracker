import csv
import inventory_update
import offset_date
import pandas as pd
import tabulate

# Makes a report of the current date with date deviation
def report_inventory(date_offset):
    offset_date.offset_date(date_offset)
    update_inventory()
    inventory_csv = pd.read_csv('inventory.csv', usecols=['product', 'amount_bought', 'amount_sold', 'in_stock'])
    with open('offset_date.txt') as file:
        date = file.read()
        print(f'Inventory of: {date}')
        file.close()
    print(tabulate.tabulate(inventory_csv, headers='keys', tablefmt='grid', showindex=False))


# Updates the inventory with new data by building up the csv file each time.
def update_inventory():

    # Writes a header with column names
    # Open inventory.csv in writing modus
    with open('inventory.csv', 'w', newline='') as inventory_input:
        header = ['id_product', 'product', 'amount_bought', 'purchase_price', 'amount_sold', 'sell_price', 'in_stock']
        inventory_writer = csv.writer(inventory_input)
        # Writes header to inventory.csv
        inventory_writer.writerow(header)
        inventory_input.close()

    # Iterates with each unique product name over inventory_update
    # Open product_id.csv in reading modus
    with open('product_id.csv', 'r') as product_id_input:
        product_id_reader = csv.reader(product_id_input)
        next(product_id_reader)
        for row in product_id_reader:
            # Extract the product name to pass it to inventory_update
            product_name = row[1]
            inventory_update.inventory_update(product_name)
        product_id_input.close()
