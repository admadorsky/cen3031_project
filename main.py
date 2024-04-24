import yfinance as yf 
import matplotlib.pyplot as plt #needed for pie chart
import numpy as np #needed for pie chart

def isfloat(string): #copied a function that will check if a string is a float, with a boolean return
    try:
        float(string)
        return True
    except ValueError:
        return False

def getHistory(ticker_symbol, period): #created a method for getting the history of a stock for a period of time
    stock = yf.Ticker(ticker_symbol) #creates a ticker in the method
    hist = stock.history(period=period) #gets the stock history from a given period
    prices = [] #creates a list that will store the prices over the time period

    #removes the headers of the given history data and isolates the values columns
    value = (str(hist).replace("                                 Open        High  ...  Dividends  Stock Splits", "\b")).replace("Date                                               ...                         ", "\b").split(" ")


    keep = True #creates a boolean that will control what makes it into the value list
    for i in value: #for loop that goes through the data and isolaetes the value volumns
        if(isfloat(i) and i != "0.0"):
            if(keep):
                prices.append(i)
            keep = not keep

    prices.pop(len(prices) - 1) #cleans output at the end

    return prices #returns a list of prices for the given duration

def getDates(ticker_symbol, period):
    stock = yf.Ticker(ticker_symbol)  # creates a ticker in the method
    hist = stock.history(period=period)  # gets the stock history from a given period
    dates = []  # creates a list that will store the prices over the time period

    # removes the headers of the given history data and isolates the values columns
    value = (str(hist).replace("                                 Open        High  ...  Dividends  Stock Splits",
                               "\b")).replace(
        "Date                                               ...                         ", "\b").split(" ")
    value = stock.history(period='1mo')['Open'] #gets the column stock data to grab the dates
    value = str(value).split("\n")

    for i in value: #goes through and substrings all of the dates
        dates.append(i[0:11])
    
    #cleans output
    dates.pop(0)
    dates.pop(len(dates) - 1)

    return dates #returns a list with all of the dates from the requested time period

def main():
    portfolio = {}  #map to keep track of transactions
    transaction_id=0  #transation id counter
    net_balance=0  #keeps track of total profits/loss after postions are closed
    breakdown = [] #stores the portfolio value of each investment for the pie chart
    percentValue = [] #stores the percentage value of how much each stock uses for pie chart
    labels = [] #stores the labels of the stocks for the pie chart

    while True:
        print("\n1. Add Transaction")
        print("2. Sell Stock")
        print("3. Display Portfolio")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            ticker_symbol = input("Enter the ticker symbol: ")

            qty = int(input("Enter the quantity of stocks bought: "))
            buy_price = float(input("Enter the buy price per stock: "))
            sell_choice = input("Do you want to enter a sell price now? (Y/N): ").upper()
            if sell_choice == 'Y':
                sell_price = float(input("Enter the sell price per stock: "))
                portfolio[transaction_id] = [ticker_symbol, qty, buy_price, sell_price]
                net_balance += sell_price - buy_price
                print("Transaction added successfully!")
                print("Total Profit/Loss: $" + str(net_balance))
            else:
                stock = yf.Ticker(ticker_symbol)
                current_price = stock.history(period='1d')['Close'].iloc[-1]
                portfolio[transaction_id] = [ticker_symbol, qty, buy_price, current_price]
                print("Transaction added successfully!")
            transaction_id += 1


        elif choice == 2:
            transaction_id = int(input("Enter the transaction ID to sell stocks: "))
            if transaction_id in portfolio:
                sell_price = float(input("Enter the sell price per stock: "))
                portfolio[transaction_id][-1] = sell_price
                net_balance+= (sell_price-portfolio[transaction_id][2])*portfolio[transaction_id][1] #sell-buy * QTY
                print("Stocks sold successfully!")
                print("Total Profit/Loss: $" + str(net_balance))
            else:
                print("Invalid transaction")

        elif choice == 3:
            portfolio_value=0
            print("\n--- Portfolio Summary ---")
            print("Ticker Symbol\tQuantity\tBuy Price\tSell Price")

            for transaction_id, details in portfolio.items():
                portfolio_value+=(details[3]-details[2])*(details[1])

                labels.append(details[0]) #stores the labels stored in the map
                breakdown.append((details[3]-details[2])*(details[1])) #stores the value of each stock

                print(details)

            for i in breakdown: #gets the value of all the stocks in the portfolio
                percentValue.append(i/portfolio_value) #stores the percentage of the total value each stock has to make a pie chart later on

            print("Portfolio Value: $" + str(round(portfolio_value, 2))) #Prints value of portfolio, rounds to 2
            print("Total Profit/Loss: $" + str(round(net_balance, 2))) #Shows net profit/loss, rounds to 2

            y = np.array(percentValue)
            plt.pie(y, labels=labels, autopct='%1.1f%%') #creates the pie chart with the array data, labels the data with the labels array, and then creates the percentage value
            plt.show() #prints the pie chart in a separate window

        elif choice == 4:
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
