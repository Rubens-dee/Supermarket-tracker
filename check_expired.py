from datetime import datetime
import csv
import pandas as pd
import inventory
import tabulate


# Creates a report with on stock bought products and if they are expired or not
def expired():
    inventory.update_inventory()
    with open('inventory.csv', 'r') as inventory_input:
        inventory_reader = csv.reader(inventory_input)
        header = next(inventory_reader)
        # Creates a dictionary with product name and sold items
        dict_inventory = {}
        for row in inventory_reader:
            dict_inventory[row[1]] = (row[4])
    inventory_input.close()

    with open('today.txt', 'r') as today_input:
        date = str(today_input.read())
        today = datetime.strptime(date, '%Y-%m-%d').date()
    today_input.close()

    with open('bought.csv', 'r') as bought_input:
        bought_reader = csv.reader(bought_input)
        header = next(bought_reader)
        # Appends extra column to header
        header.append('expired?')
        bought_df = pd.DataFrame(columns=['id', 'product_name', 'amount', 'buy_date', 'price', 'expiration_date', 'expired?'])
        # Iterates with product and amount from inventory
        if len(dict_inventory) != 0:
            for k, v in dict_inventory.items():
                df_return = adjust_amount(k, v, bought_df, today)
            # Leaves product which have been completly sold from dataframe
            df_return = df_return[df_return['amount'] != 0]
            # Writes dataframe to expired.csv
            df_return.to_csv('expired.csv', index=False)
            # Views the dataframs in a table
            print(tabulate.tabulate(df_return, headers='keys', tablefmt='grid', showindex=False))
        else:
            print('No report to view')


# Checks if products are expired on a certain date
# Adjust the amount of bought for each row with totally sold products
def adjust_amount(k, v, bought_df, today):
    with open('bought.csv', 'r') as bought_input:
        reader = csv.reader(bought_input)
        v = int(v)
        for row in reader:
            if row[1] == k:
                # If there are more products on stock than on the specific row
                # The row amount will set to 0
                # Checks if product row has been expired or not
                if int(row[2]) <= v:
                    v = v - int(row[2])
                    row[2] = int(row[2]) - int(row[2])
                    if today > datetime.strptime(row[5], '%Y-%m-%d').date():
                        row.append('yes')
                    else:
                        row.append('no')
                    # Adds row to dataframe
                    bought_df.loc[len(bought_df)] = row
                # If there are products on the row than on stock
                # The amount on the row will be adjusted and stock to 0
                # Checks if product row has been expired or not
                else:
                    row[2] = int(row[2]) - v
                    if today > datetime.strptime(row[5], '%Y-%m-%d').date():
                        row.append('yes')
                    else:
                        row.append('no')
                    # Adds row to dataframe
                    bought_df.loc[len(bought_df)] = row
                    v = 0
        bought_input.close()
        return bought_df
