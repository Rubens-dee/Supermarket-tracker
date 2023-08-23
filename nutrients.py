import requests
import pandas as pd
import csv
import tabulate
import matplotlib.pyplot as plt


# Requests nutrient info from an API for products which have been bought
def nutrient_API():
    with open('product_id.csv', 'r') as product_id_input:
        product_id_read = csv.reader(product_id_input)
        next(product_id_read)
        nutrients_dict = {}
        for row in product_id_read:
            product = row[1]
            response = requests.get(f'https://api.edamam.com/api/food-database/v2/parser?app_id=8c27a170&app_key=f46df379744a7a661adabe9e8b792052&ingr={product}&nutrition-type=cooking')
            # Returns a piece of the request in a list
            nutrient_list = response.json()["parsed"]
            if nutrient_list == []:
                pass
            else:
                # Filters the nutrients part
                nutrients = nutrient_list[0]['food']['nutrients']
                # Makes a key, value from the products and the nutrients in a dictionary
                nutrients_dict[product] = nutrients
        nutrients_df = pd.DataFrame.from_dict(nutrients_dict, orient='index')
        print(tabulate.tabulate(nutrients_df, headers='keys', tablefmt='grid'))
    product_id_input.close()
    # Plots horizontal bars from the dataframe wit matpoltlib
    try:
        nutrients_df.plot.bar()
        plt.show()
    except:
        print('Nutrients not available')


if __name__ == '__main__':
    nutrient_API()
