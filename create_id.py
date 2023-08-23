import csv


# Create new id for each new bought product entry
def create_new_id_bought():
    # Open bought.csv in reading modus
    with open('bought.csv', 'r') as bought_input:
        # Skips the heading
        next(bought_input)
        bought_reader = csv.reader(bought_input)
        bought_id = 0
        # Iterate over each row to get the latest bought id
        for row in bought_reader:
            bought_id = row[0]
        # Raises bought id by 1
        bought_id = int(bought_id) + 1
        bought_input.close()
    return bought_id


def create_new_id_sold():

    with open('sold.csv') as file:
        # Skips the heading
        next(file)
        product_list = csv.reader(file)
        # Iterate over each row in the csv file
        # using reader object
        product_id = 0
        for row in product_list:
            product_id = row[0]
        product_id = int(product_id) + 1
    return product_id


# Create unique product id if product was not bought before
def create_new_product_id(product):
    # Open product_id.csv in reading modus
    with open('product_id.csv', 'r') as product_id_input:
        # Skips the heading.
        next(product_id_input)
        product_id_reader = csv.reader(product_id_input)
        product_list = []
        product_id_list = [0]
        # Iterate over each row to make product and id list
        for row in product_id_reader:
            # Makes a list of excisting products
            product_list.append(row[1])
            # Makes a list of excisting product id's
            product_id_list.append(int(row[0]))
        # If the product does not excist, it will get a new id
        if product not in product_list:
            # Gets the highest id number
            product_id = max(product_id_list)
            # Adds by 1.
            product_id = product_id + 1
            # Pass the new product and id to append_new_product_id
            append_new_product_id(product_id, product)
        product_id_input.close()


# Append new id and product to product_id.csv
def append_new_product_id(product_id, product):
    # Open product_id.csv in appending modus
    with open('product_id.csv', 'a', newline='') as product_id_input:
        product_id_writer = csv.writer(product_id_input)
        # Makes a new row for the file
        product_row = [product_id, product]
        # Append the new row to product_id.csv
        product_id_writer.writerow(product_row)
        product_id_input.close()
