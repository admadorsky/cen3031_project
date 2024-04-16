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

Frontend

  /src contains all js, css, component, and util files that interact.
  /public contains global-level assets.
  package.json and package-lock.json contain dependencies for  building and testing

  homepage is completed

  next up are portfolio and add stock pages. these will have the most interaction with backend.
