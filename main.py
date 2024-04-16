import yfinance as yf
import matplotlib.pyplot as plt  # needed for pie chart
import numpy as np  # needed for pie chart
from mysql.connector import connect
from datetime import date, datetime, timedelta


def isfloat(string):  # copied a function that will check if a string is a float, with a boolean return
    try:
        float(string)
        return True
    except ValueError:
        return False


def getHistory(ticker_symbol, period):  # created a method for getting the history of a stock for a period of time
    stock = yf.Ticker(ticker_symbol)  # creates a ticker in the method
    hist = stock.history(period=period)  # gets the stock history from a given period
    prices = []  # creates a list that will store the prices over the time period

    # removes the headers of the given history data and isolates the values columns
    value = (str(hist).replace("                                 Open        High  ...  Dividends  Stock Splits",
                               "\b")).replace(
        "Date                                               ...                         ", "\b").split(" ")

    keep = True  # creates a boolean that will control what makes it into the value list
    for i in value:  # for loop that goes through the data and isolaetes the value volumns
        if (isfloat(i) and i != "0.0"):
            if (keep):
                prices.append(i)
            keep = not keep

    prices.pop(len(prices) - 1)  # cleans output at the end

    return prices  # returns a list of prices for the given duration


def getDates(ticker_symbol, period):
    stock = yf.Ticker(ticker_symbol)  # creates a ticker in the method
    hist = stock.history(period=period)  # gets the stock history from a given period
    dates = []  # creates a list that will store the prices over the time period

    # removes the headers of the given history data and isolates the values columns
    value = (str(hist).replace("                                 Open        High  ...  Dividends  Stock Splits",
                               "\b")).replace(
        "Date                                               ...                         ", "\b").split(" ")
    value = stock.history(period='1mo')['Open']  # gets the column stock data to grab the dates
    value = str(value).split("\n")

    for i in value:  # goes through and substrings all of the dates
        dates.append(i[0:11])

    # cleans output
    dates.pop(0)
    dates.pop(len(dates) - 1)

    return dates  # returns a list with all of the dates from the requested time period


def main():
    portfolio = {}  # map to keep track of transactions
    transaction_id = 0  # transation id counter
    net_balance = 0  # keeps track of total profits/loss after postions are closed
    breakdown = []  # stores the portfolio value of each investment for the pie chart
    percentValue = []  # stores the percentage value of how much each stock uses for pie chart
    labels = []  # stores the labels of the stocks for the pie chart

    conn = connect(
        user='root',
        password='vGAsF!6hnEZ6ADPkJ3uy.xfYtBw.kuGh',
        host='localhost',
        database='engfinproject')
    cursor = conn.cursor()

    while True:
        print("\n1. Add Transaction")
        print("2. Display Transactions")
        print("3. Display Positions")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            addTrans = ("INSERT INTO transactions "
                        "(tickerSymbol, transactionType, transactionQuantity, transactionPrice, transactionDate, userID)"
                        "VALUES (%s, %s, %s, %s, %s, %s)")
            ticker_symbol = input("Enter the ticker symbol: ")  # case sensitive!
            # if they don't put either "BOUGHT" or "SOLD" it should be an error
            transaction_type = input("Type 'BOUGHT' or 'SOLD' if you bought or sold the stock(s) in this transaction respectively: ")
            qty = int(input("Enter the quantity of stocks bought/sold: "))
            transaction_price = float(input("Enter the total transaction amount: "))
            user_ID = input("Enter the user ID: ")
            transaction_year = int(input("Enter the year of the transaction(eg: 2003): "))
            transaction_month = int(input("Enter the month of the transaction(do not use a leading 0): "))
            transaction_day = int(input("Enter the day of the month of the transaction(do not use a leading 0): "))
            dataTrans = (ticker_symbol, transaction_type, qty, transaction_price, date(transaction_year, transaction_month, transaction_day), user_ID)
            cursor.execute(addTrans, dataTrans)

            # update the positions table:
            # put all rows in the positions table with a matching ID and ticker symbol in your cursor object
            query = ("SELECT * FROM positions "
                     "WHERE userID = %s AND tickerSymbol = %s")
            dataQuery = (user_ID, ticker_symbol)
            cursor.execute(query, dataQuery)
            fetch = cursor.fetchone()
            if cursor.rowcount == 0:  # if position doesn't exist in their table, create a new entry for it, unless the
                # transaction was a sell in which it should draw an error(you're selling a stock you own none of)
                # Maybe if the transaction was invalid, delete the transaction with the highest transactionCounter
                cursor.reset()
                addPosition = ("INSERT INTO positions "
                               "(tickerSymbol, quantity, userID)"
                               "VALUES (%s, %s, %s)")
                dataPosition = (ticker_symbol, qty, user_ID)
                cursor.execute(addPosition, dataPosition)
                conn.commit()
            else:  # if position does exist in their table, update its quantity based upon the latest transaction
                # retrieve the column entries from that stock's row in positions(we need the counter and quantity)
                queryCounter, queryTicker, queryQuantity, queryID = fetch
                if transaction_type == "BOUGHT":  # if the transaction was a "buy"
                    # update the old position entry with the new quantity
                    updatePosition = ("UPDATE positions "
                                      "SET quantity = %s"
                                      "WHERE positionsCounter =%s")
                    updatePositionData = (queryQuantity + qty, queryCounter)
                    cursor.execute(updatePosition, updatePositionData)
                    conn.commit()
                else:  # if transaction was a "sell"
                    # update the old position entry with the new quantity
                    updatePosition = ("UPDATE positions "
                                      "SET quantity = %s"
                                      "WHERE positionsCounter =%s")
                    updatePositionData = (queryQuantity - qty, queryCounter)
                    cursor.execute(updatePosition, updatePositionData)
                    conn.commit()




        elif choice == 2:
            query = ("SELECT * FROM transactions")
            cursor.execute(query)
            result = cursor.fetchall()  # is there a better way to print these values? Do we even need fetchall?
            for r in result:
                print(r)

            #displaying a pie chart
            """portfolio_value = 0
            print("\n--- Portfolio Summary ---")
            print("Ticker Symbol\tQuantity\tBuy Price\tSell Price")

            for transaction_id, details in portfolio.items():
                portfolio_value += (details[3] - details[2]) * (details[1])

                labels.append(details[0])  # stores the labels stored in the map
                breakdown.append((details[3] - details[2]) * (details[1]))  # stores the value of each stock

                print(details)

            for i in breakdown:  # gets the value of all the stocks in the portfolio
                percentValue.append(
                    i / portfolio_value)  # stores the percentage of the total value each stock has to make a pie chart later on

            print("Portfolio Value: $" + str(round(portfolio_value, 2)))  # Prints value of portfolio, rounds to 2
            print("Total Profit/Loss: $" + str(round(net_balance, 2)))  # Shows net profit/loss, rounds to 2

            y = np.array(percentValue)
            plt.pie(y, labels=labels,
                    autopct='%1.1f%%')  # creates the pie chart with the array data, labels the data with the labels array, and then creates the percentage value
            plt.show()  # prints the pie chart in a separate window """

        elif choice == 3:
            print("Coming soon....")

        elif choice == 4:
            print("Exiting program.")
            cursor.close()
            conn.close()
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()

    """elif choice == 2:
                transaction_id = int(input("Enter the transaction ID to sell stocks: "))
                if transaction_id in portfolio:
                    sell_price = float(input("Enter the sell price per stock: "))
                    portfolio[transaction_id][-1] = sell_price
                    net_balance += (sell_price - portfolio[transaction_id][2]) * portfolio[transaction_id][
                        1]  # sell-buy * QTY
                    print("Stocks sold successfully!")
                    print("Total Profit/Loss: $" + str(net_balance))
                else:
                    print("Invalid transaction") """
