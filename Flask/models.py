from config import db

class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer)
    ticker = db.Column(db.String(5))
    quantity = db.Column(db.Float)
    buy_price = db.Column(db.Float)
    is_sold = db.Column(db.String)
    sell_price = db.Column(db.Float)

    def to_json(self):
        return {
            "id": self.id,
            "user": self.user,
            "ticker": self.ticker,
            "quantity": self.quantity,
            "buyPrice": self.buy_price,
            "isSold": self.is_sold,
            "sellPrice": self.sell_price
        }
    
class User(db.Model):
    __bind_key__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Integer)
    username = db.Column(db.String(16), unique=True)
    password = db.Column(db.String(16))

    def to_json(self):
        return {
            "id": self.id,
            "isActive": self.is_active,
            "username": self.username,
            "password": self.password
        }