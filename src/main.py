import yfinance as yf

userReq = input("Enter the stock you would like the information for: ") #takes user input for the stock the user would like to pull data for. I have been MSFT (Microsoft) data to test the functions
print("\n")

stock = yf.Ticker(userReq) #IMPORTANT!! this uses the ticker function to select which stock from its list the user would like the information for

# get option chain for specific expiration
opt = stock.option_chain('2024-03-01')

# get all stock info
stockOverview = stock.info #stock.info gives the general information related to the entire stock

print(str(stockOverview).replace("', '", "\n").replace("'", "") + "\n") #prints the general information, creating a new line for each point of data and removing all single quotes to make output cleaner


# get historical market data, can adjust the value to get information from futher back, even using the "max" keyword to get the entire stock history. Uses "mo" for month and "y" for year.
timePeriod = input("What is the period of time you would like the financial data for?\n" + "(Please use the format of 'mo' for month, 'y' for year, or type 'max' to get all financial data): ")
hist = stock.history(period=timePeriod)

if(timePeriod != 'max'): #if the user asks for stock information in a specific time window, make a statement presenting that
    print("\n" + "Here is all the information for stock " + userReq + " for the past " + timePeriod + ":")
else: #if the user asks for the all time financial information, state it
    print("\n" + "Here is the all time information for stock " + userReq + ":")

print(hist) #prints the stock data from the last month


#HAVEN'T TESTED DATA BELOW THIS POINT

# show meta information about the history (requires history() to be called first)
stock.history_metadata

# show actions (dividends, splits, capital gains)
stock.actions
stock.dividends
stock.splits
stock.capital_gains  # only for mutual funds & etfs

# show share count
stock.get_shares_full(start="2022-01-01", end=None)

# show financials:
# - income statement
stock.income_stmt
stock.quarterly_income_stmt

# - balance sheet
stock.balance_sheet
stock.quarterly_balance_sheet

# - cash flow statement
stock.cashflow
stock.quarterly_cashflow
# see `Ticker.get_income_stmt()` for more options

# show holders
stock.major_holders
stock.institutional_holders
stock.mutualfund_holders
stock.insider_transactions
stock.insider_purchases
stock.insider_roster_holders

# show recommendations
stock.recommendations
stock.recommendations_summary
stock.upgrades_downgrades

# Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default.
# Note: If more are needed use
# stock.get_earnings_dates(limit=XX) with increased limit argument.
stock.earnings_dates

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
stock.isin

# show options expirations
stock.options

# show news
stock.news


# data available via: opt.calls, opt.puts
