import pandas as pd
import offset_date
import revenue


# Returns the profit of today, yesterday or a specific period
def profit(date_offset, date_offset_name):
    offset_date.offset_date(date_offset)
    with open('offset_date.txt') as file:
        date = file.read()
        file.close()
    bought_csv = pd.read_csv('sold.csv')
    # Sums the revenue total revenue of a given date
    revenue = bought_csv.loc[bought_csv['sell_date'] == date, 'sell_price'].sum()
    bought_csv = pd.read_csv('bought.csv')
    # Sums the purchase price of a given date
    purchase = bought_csv.loc[bought_csv['buy_date'] == date, 'price'].sum()
    profit = round(revenue - purchase, 2)
    print(date_offset_name, profit)


def profit_year_month(year_month):
    bought_csv = pd.read_csv('bought.csv')
    # Converts the column 'buy_date' to datetime format
    bought_csv['buy_date'] = pd.to_datetime(bought_csv['buy_date'])
    # Adds a column 'year_month' with the year and month the product was sold(YYYY-MM)
    bought_csv['year_month'] = bought_csv['buy_date'].dt.to_period('M')
    year_month_list = []
    for month in bought_csv['year_month']:
        # Adds all year-month from the sold products to a list
        year_month_list.append(str(month))
        # Checks if the given year-month is present in the list
    if year_month in year_month_list:
        # Groups buy_date(YYYY-MM-DD) to (YYYY-MM) and sums the buy_price in the period(YYYY-MM) in a new column
        bought_df = bought_csv.groupby(bought_csv['buy_date'].dt.strftime('%Y-%m')).agg(total_buy_price=('price', 'sum'))
        # Select the correct total buy price from the dataframe by year_month
        bought = bought_df.loc[year_month, 'total_buy_price']
        sold = revenue.revenue_year_month(year_month, True)
        if sold is None: sold = 0
        if bought is None: bought = 0
        profit = round(sold - bought, 2)
        # Makes a datetime from year_month
        name_month = pd.Timestamp(year_month)
        # Gives the year(YYYY) from year_month(YYYY-MM)
        year = name_month.year
        print(f'Profit from {name_month.month_name()} {year}: {round(profit,2)}')
    else:
        print('No profit in this period')
