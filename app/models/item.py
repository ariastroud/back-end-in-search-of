from app import db

class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    brand = db.Column(db.String)
    category = db.Column(db.String)
    size = db.Column(db.String)
    description = db.Column(db.String)
    file = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    user = db.relationship("User", back_populates="items")

    def to_dict(self):
        item_as_dict = {
            "id": self.item_id,
            "title": self.title,
            "brand": self.brand,
            "category": self.category,
            "size": self.size,
            "description": self.description,
            "file": self.file,
            "user_id": self.user_id,
            "user": self.user.name
        }
        return item_as_dict
    
    @classmethod
    def from_dict(cls, item_data):
        new_item = cls(
            title=item_data["title"],
            brand=item_data["brand"],
            category=item_data["category"],
            size=item_data["size"],
            description=item_data["description"],
            file=item_data["file"],
            user_id=item_data["user_id"],
            user=item_data["user.name"]
        )
        return new_item