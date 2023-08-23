import pandas as pd
import offset_date
import inventory

# Gives the total revenue of all sold products
def revenue(date_offset, revenue_text):
    # Updates the inventory
    inventory.update_inventory()
    # Changes the offset date
    offset_date.offset_date(date_offset)
    with open('offset_date.txt') as offset_date_input:
        date = offset_date_input.read()
    offset_date_input.close()
    # Makes dataframe from sold.csv
    sold_csv = pd.read_csv('sold.csv')
    # Sums all values in the column 'sell_date'
    revenue = round(sold_csv.loc[sold_csv['sell_date'] == date, 'sell_price'].sum(), 2)
    print(revenue_text, revenue)


# Gives the total revenue in a certain month (YYYY-MM)
def revenue_year_month(year_month, profit=False):
    # Makes dataframe from sold.csv
    sold_csv = pd.read_csv('sold.csv')
    # Converts the column 'sell_date' to datetime format
    sold_csv['sell_date'] = pd.to_datetime(sold_csv['sell_date'])
    # Adds a column 'year_month' with the year and month the product was sold(YYYY-MM)
    sold_csv['year_month'] = sold_csv['sell_date'].dt.to_period('M')
    year_month_list = []
    for month in sold_csv['year_month']:
        # Adds all year-month from the sold products to a list 
        year_month_list.append(str(month))
        # Checks if the given year-month is present in the list
    if year_month in year_month_list:
        # Groups sell_date(YYYY-MM-DD) to (YYYY-MM) and sums the sell_price in the period(YYYY-MM) in a new column
        revenue_df = sold_csv.groupby(sold_csv['sell_date'].dt.strftime('%Y-%m')).agg(total_sell_price=('sell_price', 'sum'))
        # Makes a datetime from year_month
        name_month = pd.Timestamp(year_month)
        # Gives the year(YYYY) from year_month(YYYY-MM)
        year = name_month.year
        # Select the correct total sell price from the dataframe by year_month
        revenue = round(revenue_df.loc[year_month, 'total_sell_price'], 2)
        if profit is False:
            # Prints the written name of the month
            print(f'Revenue from {name_month.month_name()} {year}: {revenue}')
        else:
            return revenue
    elif year_month not in year_month_list and profit is False:
        # If there was nothing sold in the given period
        print('No revenue in this period')
