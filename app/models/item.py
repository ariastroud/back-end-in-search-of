from app import db

class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    brand = db.Column(db.String)
    category = db.Column(db.String)
    size = db.Column(db.String)
    description = db.Column(db.String)
    # some nested attribute like which user post belongs to

    def to_dict(self):
        item_as_dict = {
            "id": self.item_id,
            "title": self.title,
            "brand": self.brand,
            "category": self.category,
            "size": self.size,
            "description": self.description
        }
        return item_as_dict
    
    @classmethod
    def from_dict(cls, item_data):
        new_item = cls(
            title=item_data["title"],
            brand=item_data["brand"],
            category=item_data["category"],
            size=item_data["size"],
            description=item_data["description"]
        )
        return new_item