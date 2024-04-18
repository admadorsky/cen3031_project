from flask import request, jsonify
from config import app, db
from models import Position
import yfinance as yf

# C |R| U D
# - read
@app.route("/portfolio", methods=["GET"])
def get_positions():
    positions = Position.query.all()
    # convert list of positions as python objects to json, put in new list
    json_positions = list(map(lambda x: x.to_json(), positions))
    return jsonify({"positions": json_positions})

# |C| R U D
# - create
@app.route("/create_position", methods=["POST"])
def create_position():
    ticker = request.json.get("ticker")
    quantity = request.json.get("quantity")
    buy_price = request.json.get("buyPrice")
    is_sold = request.json.get("isSold")
    sell_price = request.json.get("sellPrice")

    # verify that input exists for ticker, quantity, and buy price
    if not ticker or not quantity or not buy_price:
        return (
            jsonify({"message": "You must inlcude a ticker, quantiy, and buy price."}),
            400
        )
    
    # if the stock is sold, verify that a sell price was specified
    if is_sold and not sell_price:
        return (
            jsonify({"message": "If you indicate that the position is sold, you must include a sell price."}),
            400
        )
    
    # generate a yf Ticker object and verify that the selected ticker exists
    stock = yf.Ticker(ticker)
    info = None
    if (stock.info['regularMarketPrice'] == None):
        return (
            jsonify({"message": "Please enter a valid ticker symbol."}),
            400
        )
    
    # assign current_price with either input or current market price, depending on is_sold selection
    current_price = 0.0
    if not is_sold:
        current_price = stock.history(period='1d')['Close'].iloc[-1]
    else:
        current_price = sell_price

    # create a database entry object for new position
    new_position = Position(ticker=ticker,
                            quantity=quantity,
                            buy_price=buy_price,
                            is_sold=is_sold,
                            sell_price=current_price)
    
    # add the new entry to the database, while catching exceptions
    try:
        db.session.add(new_position)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "Position Added!"}), 201

# C R |U| D
# - update

# function will go here to update existing positions


# C R U |D|
# - delete

# function will go here to delete existing positions
    

if __name__ == "__main__":
    # spin up the database if it doesn't already exist
    with app.app_context():
        db.create_all()

    app.run(debug=True)
