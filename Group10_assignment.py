print("----------------------------------------------------")
print("*** Welcome to Stock Value Calculator Program! ***")
print("----------------------------------------------------")

#taking user input

stock_name = input("Enter stock's name : " )
num_purchase = float(input("Enter the total number of purchased share : "))
buy_price = float(input("Enter the dollar amount per share purchased: "))
num_sold = float(input("Enter the total number of shares sold: "))
sell_price=float(input("Enter the dollar for per share sold : "))

#validation of the user input
if num_purchase <= 0 or buy_price <= 0 or num_sold <= 0 or sell_price <= 0:
    print("Error: Negative values are not allowed!")
    exit()
if num_purchase < num_sold:
    print("Error: Total number of shares sold cannot be greater than the total number of shares purchased!")
    exit()

#commision variable
if num_purchase < 1000:
    p_commision_rate = 100
else:
    p_commision_rate = 0

if num_sold <= 1000:
    s_commision_rate = 100
elif num_sold > 1000 and num_sold < 2000:
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
print("Total Purchase Amount : $", total_buy)
print("Purchase Commision : $", p_commision_rate)
print("*****************************************************")
print("                  Selling Report                     ")
print("*****************************************************")
print("Total Sold Amount: $", total_sold)
print("Sold Commision : $", s_commision_rate)
print("*****************************************************")
if profit > 0:
    print("Congratulations, Total Profit: $", profit)
elif profit < 0:
    print("Good Luck Next Time, You lost: $", profit)
elif profit == 0:
    print("No Profit or No Loss, Total Profit: $", profit)
print("*****************************************************")