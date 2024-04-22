from flask import request, jsonify
from config import app, db
from models import ( Position, User )
import yfinance as yf

# C |R| U D
# - read
@app.route("/portfolio", methods=["GET"])
def get_positions():
    positions = Position.query.all()
    
    users = User.query.all()
    for user in users:
        if user.is_active:
            active_user = user

    for position in positions:
        if not position.is_sold:
            stock = yf.Ticker(position.ticker)
            position.sell_price = stock.history(period='1d')['Close'].iloc[-1]

    db.session.commit()

    # convert list of positions as python objects to json, put in new list
    json_positions = []
    for position in positions:
        if position.user == active_user.id:
            json_positions.append(position.to_json())

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

    users = User.query.all()
    for user in users:
        if user.is_active:
            active_user = user

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
    new_position = Position(user=active_user.id,
                            ticker=ticker,
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

@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    json_users = list(map(lambda x: x.to_json(), users))
    return jsonify({"users": json_users})

@app.route("/create_user", methods=["POST"])
def create_user():
    username = request.json.get("createUsername")
    password = request.json.get("createPassword")

    print(username)
    print(password)

    if not username or not password:
        return jsonify({"message": "You must include a valid username and password."}), 400
    
    new_user = User(
        is_active = 0,
        username = username,
        password = password
    )

    # add the new entry to the database, while catching exceptions
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "Position Added."}), 201

@app.route("/set-active-user<int:user_id>", methods=["PATCH"])
def set_active_user(user_id):
    users = User.query.all()
    user = User.query.get(user_id)

    if not user:
        print("here")
        return jsonify({"message": "Username or password is incorrect."}), 400
    
    for listUser in users:
        listUser.is_active = 0

    user.is_active = 1;

    db.session.commit()

    print(str(user.is_active))
    return jsonify({"message": "User Logged in."}), 200

@app.route("/logout", methods=["PATCH"])
def logout():
    users = User.query.all()
    for user in users:
        user.is_active = 0

    db.session.commit()

    return jsonify({"message": "User logged out."})

if __name__ == "__main__":
    # spin up the databases if they don't already exist
    with app.app_context():
        db.create_all()

    app.run(debug=True)