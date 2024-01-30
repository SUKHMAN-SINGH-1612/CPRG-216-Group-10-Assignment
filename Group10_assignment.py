aster = ("*****************************************************")
print("----------------------------------------------------")
print("*** Welcome to Stock Value Calculator Program! ***")
print("----------------------------------------------------")

#taking user input

stock_name = input("Enter stock's name : " )
num_purchase = float(input("Enter the total number of purchased share : "))
if num_purchase <= 0:
    print("Error: Number of purchased shares should be >0")
    exit()
buy_price = float(input("Enter the dollar amount per share purchased: "))
if buy_price <= 0:
    print("Error: Purchase amount should be >0")
    exit()

num_sold = float(input("Enter the total number of shares sold: "))
if num_sold <= 0:
    print("Error: Number of sold shares should be >0 and must be <= number of purchased shares")
    exit()
elif num_sold > num_purchase:
    print("Error: Number of sold shares should be >0 and must be <= number of purchased shares")
    exit()
sell_price=float(input("Enter the dollar for per share sold : "))
if sell_price <= 0:
    print("Error: Sold amount should be >0")
    exit()

#commision variable
if num_purchase < 1000:
    p_commision_rate = 100
else:
    p_commision_rate = 0

if num_sold < 1000:
    s_commision_rate = 100
elif num_sold >= 1000 and num_sold < 2000:
    s_commision_rate = 50
elif num_sold >= 2000:
    s_commision_rate = 0

#calculating the total purchase and sold amount and profit
total_buy = num_purchase * buy_price
total_sold = num_sold * sell_price
profit = total_sold - total_buy - p_commision_rate - s_commision_rate

#output
print("*****************************************************")
print("                 Purchasing Report                  " )
print("*****************************************************")
print("Stock Name : ", stock_name)
print("Total Purchase Amount : $", format(total_buy, ".2f"))
print("Purchase Commision : $", p_commision_rate)
print("*****************************************************")
print("                  Selling Report                     ")
print("*****************************************************")
print("Total Sold Amount: $", format(total_sold, ".2f"))
print("Sold Commision : $", s_commision_rate)
print("*****************************************************")
if profit > 0:
    print("Congratulations, Total Profit: $", format(profit, ".2f"))
elif profit < 0:
    print("Good Luck Next Time, You lost: $", format(profit, ".2f"))
elif profit == 0:
    print("No Profit or No Loss, Total Profit: $", format(profit, ".2f"))
print("*****************************************************")