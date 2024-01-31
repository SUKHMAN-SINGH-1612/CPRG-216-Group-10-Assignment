''' 
Stock Value Scenario
'''

# ---------------CONSTANTS-------------------
# - THREDSHOLDS
THREDSHOLD_1000 = 1000
THREDSHOLD_2000 = 2000
# - COMMISSIONS
COMMISSION_FREE = 0
COMMISSION_50 = 50
COMMISSION_100 = 100
# - output asterisks
OUTPUT_ASTERISKS = "****************************************************"
WELCOME_DASHLINE = "----------------------------------------------------"


# intro
print(WELCOME_DASHLINE)
print("*** Welcome to Stock Value Calculator Program! ***")
print(WELCOME_DASHLINE)

#taking user input
stock_name = input("Enter stock's name : " )
num_purchase = float(input("Enter the total number of purchased share : "))
buy_price = float(input("Enter the dollar amount per share purchased: "))
num_sold = float(input("Enter the total number of shares sold: "))
sell_price=float(input("Enter the dollar for per share sold : "))


# -------------process starts here-----------------
# check illegal inputs
# check purchase shares, which cannot be zero or negative
if num_purchase < 0:
    # print error msg and end here
    print("Error: Number of purchased shares should be >= 0")
# check sale shares, which cannot be zero or negative,
#  and make sure purchased shares are greater than sold shares
elif num_sold < 0 or num_purchase < num_sold:
    print("Error: Number of sold shares should be >= 0 and must be <= number of purchased shares")
# check amount paid per purchased share, which cannot be zero or negative
elif buy_price <= 0:
    print("Error: the purchase maount should be > 0")
# check amount paid per sold share, which cannot be zero or negative
elif sell_price <= 0:
    print("The sold amount should be > 0")
else:
    # -----process: deduct commissions start-------------------------
    commission_purchase = COMMISSION_FREE
    commission_sale = COMMISSION_FREE
    # calculate commission_purchase 
    if num_purchase < 1000:
    # --------------------------------calculating profit or loss---------------------------------
        commission_purchase = COMMISSION_100
    # calculate commission_sale
    if num_sold < 1000:
        commission_sale = COMMISSION_100
    elif 1000 <= num_sold < 2000:
        commission_sale = COMMISSION_50
    else:
        pass
    # -----process: deduct commissions end, commission_purchase and commission_sale can be add to the end of every purchase or sale output-------------------------

    # purchase and sale calculation section
    #output
    total_buy = num_purchase * buy_price
    total_sold = num_sold * sell_price
    print("Purchasing Report" )
    print("Total Purchase Amount : ", total_buy)
    print("Selling Report")
    print("Total Sold Amount: ", total_sold)

    print(OUTPUT_ASTERISKS)
    print("                 Purchasing Report                  " )
    print(OUTPUT_ASTERISKS)
    print("Stock Name : ", stock_name)
    print("Total Purchase Amount : $", format(total_buy, ".2f"))
    print("Purchase Commision : $", commission_purchase)
    print(OUTPUT_ASTERISKS)
    print("                  Selling Report                     ")
    print(OUTPUT_ASTERISKS)
    print("Total Sold Amount: $", format(total_sold, ".2f"))
    print("Sold Commision : $", commission_sale)
    print(OUTPUT_ASTERISKS)

    # ------profit or loss output: deduct commission, add profit or loss output-----------------
    result = total_sold - total_buy - commission_purchase - commission_sale
    if result == 0:
        print("No Profit or Loss, Total Profit: $0")
        print(OUTPUT_ASTERISKS)
    elif result > 0:
        print("Congratulation, Total Profit: $", format(result,".2f"))
        print(OUTPUT_ASTERISKS)
    else:
        print("Good Luck Next Time, You Lost: $", format(result,".2f"))
        print(OUTPUT_ASTERISKS)
