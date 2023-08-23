# Imports
import argparse
import bought
import sold
import valid_date
import inventory
import revenue
import profit
import advance_time
import check_expired
import nutrients

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
# The CLI with multiple subparsers
def main():

    parser = argparse.ArgumentParser(description='Welcome to the Supermarket Tracker!')
    subparsers = parser.add_subparsers(dest='command')
    subparsers.required = True

    # Create Buy parser
    buy_parser = subparsers.add_parser('buy', help='select if you want to buy products')
    buy_parser.add_argument('product', type=str, help='name of the product you want to buy')
    buy_parser.add_argument('amount', type=str, help='how many you want to buy of this product')
    buy_parser.add_argument('price', type=float, help='the price of the product where it was bought for')
    buy_parser.add_argument('expiration_date', type=valid_date.validate, help='the expiration date of the product')

    # Create Sell parser
    sell_parser = subparsers.add_parser('sell', help='select if you want to sell products')
    sell_parser.add_argument('product', type=str, help='name of the product you want to sell')
    sell_parser.add_argument('amount', type=str, help='how many you want to sell of this product')
    sell_parser.add_argument('price', type=float, help='the selling price of the product')

    # Create timemachine parser and check for a postive integer
    # Adjust today
    timemachine_parser = subparsers.add_parser('advance-time', help='select if you want to travel to the future')
    timemachine_parser.add_argument('amount-days', type=advance_time.advance_time, help='select the amount of days you want to travel')

    # Create report parser.
    report_parser = subparsers.add_parser('report', help='select for a report of the inventory, revenue, profit, nutrients or expired products in stock')
    report_subparser = report_parser.add_subparsers(dest='report_command', required=True)

    # Create report inventory parser
    report_inventory_parser = report_subparser.add_parser('inventory', help='select for a report of the inventory without expired products')
    report_inventory_parser.add_argument('today_yesterday', type=str, choices=['today', 'yesterday'], help='choose today or yesterday for the inventory of that day')

    # Create report revenue partser
    report_revenue_parser = report_subparser.add_parser('revenue', help='choose the period you want to view the revenue')
    report_revenue_subparser = report_revenue_parser.add_subparsers(dest='report_revenue_command', required=True)
    report_revenue_subparser.add_parser('today', help='total revenue of today')
    report_revenue_subparser.add_parser('yesterday', help='total revenue of yesterday')

    # Create report revenue period parser
    report_revenue_period_parser = report_revenue_subparser.add_parser('period', help="enter 'period' followed by: YYYY-MM")
    report_revenue_period_parser.add_argument('year_month', type=valid_date.validate_year_month, help='choose the period you want to view the revenue(YYYY-MM)')

    # Create report profit partser
    report_profit_parser = report_subparser.add_parser('profit', help='choose the period you want to view the profit')
    report_profit_subparser = report_profit_parser.add_subparsers(dest='report_profit_command', required=True)
    report_profit_subparser.add_parser('today', help='total profit of today')
    report_profit_subparser.add_parser('yesterday', help='total profit of yesterday')

    # Create report profit period parser
    report_profit_period_parser = report_profit_subparser.add_parser('period', help="enter 'period' followed by: YYYY-MM")
    report_profit_period_parser.add_argument('year_month', type=valid_date.validate_year_month, help='choose the period you want to view the profit(YYYY-MM)')

    # Create report nutrients
    report_subparser.add_parser('nutrients', help='shows a report of the nutrients of the products which haven been bought')

    # Create report expired
    report_subparser.add_parser('expired', help='shows a report of products in stock and if they are expired or not')

    # Parse arguments
    args = parser.parse_args()

    if args.command == 'buy':
        bought.append_product(args.product, args.amount, args.price, args.expiration_date)
        print('OK')

    if args.command == 'sell':
        sold.check_inventory_sold_product(args.product, args.amount, args.price)
        print('OK')

    if args.command == 'report':
        if args.report_command == 'inventory':
            if args.today_yesterday == 'today':
                inventory.report_inventory(0)
            elif args.today_yesterday == 'yesterday':
                inventory.report_inventory(-1)
        if args.report_command == 'revenue':
            if args.report_revenue_command == 'today':
                revenue.revenue(0, 'Today\'s revenue so far:')
            elif args.report_revenue_command == 'yesterday':
                revenue.revenue(-1, 'Yesterday\'s revenue:')
            elif args.report_revenue_command == 'period':
                revenue.revenue_year_month(args.year_month)
        if args.report_command == 'profit':
            if args.report_profit_command == 'today':
                profit.profit(0, 'Today\'s profit so far:')
            elif args.report_profit_command == 'yesterday':
                profit.profit(-1, 'Yesterday\'s profit:')
            elif args.report_profit_command == 'period':
                profit.profit_year_month(args.year_month)
        if args.report_command == 'nutrients':
            nutrients.nutrient_API()
        if args.report_command == 'expired':
            check_expired.expired()


if __name__ == "__main__":
    main()
