from config import db

class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(5), unique=False, nullable=False)
    quantity = db.Column(db.Float)
    buy_price = db.Column(db.Float)
    is_sold = db.Column(db.Boolean)
    sell_price = db.Column(db.Float)

    def to_json(self):
        return {
            "id": self.id,
            "ticker": self.ticker,
            "quantity": self.quantity,
            "buyPrice": self.buy_price,
            "isSold": self.is_sold,
            "sellPrice": self.sell_price
        }