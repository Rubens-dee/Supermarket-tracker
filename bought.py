import csv
import create_id
import inventory


# Appends entered buying data from CLI to bought.csv file.
def append_product(product, amount, price, expiration_date):
    with open('today.txt', 'r') as today_input:
        today = today_input.read()
        today_input.close()
    # Opens csv file in appending mode.
    with open('bought.csv', 'a', newline='') as bought_input:
        # Create column names.
        field = ['id', 'product_name', 'amount', 'buy_date', 'price', 'expiration_date']
        bought_writer = csv.DictWriter(bought_input, fieldnames=field)
        # Writes entered data to new a row with a unique id from create_id module.
        product_row = {
            'id': create_id.create_new_id_bought(),
            'product_name': product,
            'amount': amount,
            'buy_date': today,
            'price': price,
            'expiration_date':  expiration_date
            }
        # Appends new row to the csv file.
        bought_writer.writerow(product_row)
        bought_input.close()
    # Create new id for product if the product was not bought before.
    create_id.create_new_product_id(product)
    # Updates the inventory
    inventory.update_inventory()
