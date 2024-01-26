print("----------------------------------------------------")
print("*** Welcome to Stock Value Calculator Program! ***")
print("----------------------------------------------------")

#taking user input

stock_name = input("Enter stock's name : " )
num_purchase = float(input("Enter the total number of purchased share : "))
buy_price = float(input("Enter the dollar amount per share purchased: "))
num_sold = float(input("Enter the total number of shares sold: "))
sell_price=float(input("Enter the dollar for per share sold : "))
total_buy = num_purchase * buy_price
total_sold = num_sold * sell_price

#output
print("*****************************************************")
print("                 Purchasing Report                  " )
print("*****************************************************")

print("Total Purchase Amount : ", total_buy)
print("*****************************************************")
print("                  Selling Report                     ")
print("*****************************************************")
print("Total Sold Amount: ", total_sold)


