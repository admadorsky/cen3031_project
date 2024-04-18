from flask import request, jsonify
from config import app, db
from models import Position
import yfinance as yf

# C |R| U D
# - read
@app.route("/portfolio", methods=["GET"])
def get_positions():
    positions = Position.query.all()

    for position in positions:
        if not position.is_sold:
            stock = yf.Ticker(position.ticker)
            position.sell_price = stock.history(period='1d')['Close'].iloc[-1]

    db.session.commit()

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
            jsonify({"message": "You must inlcude a ticker, quantity, and buy price."}),
            400
        )
    
    # if the stock is sold, verify that a sell price was specified
    if ( is_sold == 1 ) and not sell_price:
        return (
            jsonify({"message": "If you indicate that the position is sold, you must include a sell price."}),
            400
        )
    
    # generate a yf Ticker object and verify that the selected ticker exists
    stock = yf.Ticker(ticker)
    info = None
    info = stock.history(period = '7d', interval = '1d')
    if not ( len(info) > 0 ):
        return (
            jsonify({"message": "Please enter a valid ticker."}),
            400
        )
    
    # assign current_price with either input or current market price, depending on is_sold selection
    current_price = 0.0
    if is_sold != 1:
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
    
    return jsonify({"message": "Position Added."}), 201

# C R |U| D
# - update
@app.route("/update_position/<int:position_id>", methods=["PATCH"])
def update_position(position_id):
    position = Position.query.get(position_id)

    if not position:
        return jsonify({"message": "Position not found."}), 404
    
    data = request.json
    # modify position in db according to input passed as json
    position.quantity = data.get("quantity", position.quantity)
    position.buy_price = data.get("buyPrice", position.buy_price)

    db.session.commit()

    return jsonify({"message": "Position updated."}), 200

# C R |U| D
# - update (sell stock)
@app.route("/sell_stock/<int:position_id>", methods=["PATCH"])
def sell_stock(position_id):
    position = Position.query.get(position_id)

    if not position:
        return jsonify({"message": "Position not found."}), 404
    
    data = request.json
    if position.is_sold:
        return jsonify({"message": "Position is already sold."})
    
    position.is_sold = True
    position.sell_price = data.get("sellPrice", position.sell_price)

    db.session.commit()

    return jsonify({"message": "Position sold."}), 200

# C R U |D|
# - delete
@app.route("/delete_position/<int:position_id>", methods=["DELETE"])
def delete_position(position_id):
    position = Position.query.get(position_id)

    if not position:
        return jsonify({"message": "Position not found."}), 404
    
    db.session.delete(position)
    db.session.commit()

    return jsonify({"message": "Position deleted."}), 200

if __name__ == "__main__":
    # spin up the database if it doesn't already exist
    with app.app_context():
        db.create_all()

    app.run(debug=True)
