from app import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    items = db.relationship("Item", back_populates="user")

    def to_dict(self):
        user_as_dict = {"id": self.user_id, "name": self.name, "email": self.email}
        return user_as_dict
    
    @classmethod
    def from_dict(cls, user_data):
        new_user = cls(name=user_data["name"], email=user_data["email"])

        return new_user