import yfinance as yf

def main():
    portfolio = {}  #map to keep track of transactions
    transaction_id=0  #transation id counter
    net_balance=0  #keeps track of total profits/loss after postions are closed

    while True:
        print("\n1. Add Transaction")
        print("2. Sell Stock")
        print("3. Display Portfolio")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
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


        elif choice == '2':
            transaction_id = int(input("Enter the transaction ID to sell stocks: "))
            if transaction_id in portfolio:
                sell_price = float(input("Enter the sell price per stock: "))
                portfolio[transaction_id][-1] = sell_price
                net_balance+= (sell_price-portfolio[transaction_id][2])*portfolio[transaction_id][1] #sell-buy * QTY
                print("Stocks sold successfully!")
                print("Total Profit/Loss: $" + str(net_balance))
            else:
                print("Invalid transaction")

        elif choice == '3':
            portfolio_value=0
            print("\n--- Portfolio Summary ---")
            print("Ticker Symbol\tQuantity\tBuy Price\tSell Price")

            for transaction_id, details in portfolio.items():
                portfolio_value+=(details[3]-details[2])*(details[1])
                print(details)

            print("Portfolio Value: $" + str(round(portfolio_value, 2))) #Prints value of portfolio, rounds to 2
            print("Total Profit/Loss: $" + str(round(net_balance, 2))) #Shows net profit/loss, rounds to 2


        elif choice == '4':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
