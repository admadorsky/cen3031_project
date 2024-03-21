File to create portfolio

Background for the code.

Uses a map to store transaction id and transaction details.

portfolio[transaction_id] = [ticker_symbol, qty, buy_price, sell_price]

- If not sold, sell price is current market price
- Net_balance is variable to keep track of total profits

portfolio value= QTY * current Price  

Total Profits/Loss: Only counts closed positions  


Display Portfolio option.

  Returns each transaction
  
  Prints total value of portfolio
  
  Prints total profit/loss

  Creates a Pie chart with the purchases the user would like to make

  Creates three methods, isFloat checks if a string is a float and getHistory returns a list of a stock's price history for the duration inputted by the user, going to be used in portfolio tracking in future iterations. Also created a method to return the dates of a given period to be used in graph creation for portfolio tool later on. 

Questions:

Transaction Id is a counter currently do we want to keep it that way? Is there a better way to have it.



Here is an idea of front end later on to showcase portfolio/profits.
<img width="1151" alt="image" src="https://github.com/admadorsky/cen3031_project/assets/158636728/70bdc25b-7622-429e-84fd-f317c0fa1989">
