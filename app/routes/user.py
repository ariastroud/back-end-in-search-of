from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.user import User
from app.models.item import Item

bp = Blueprint("user_bp", __name__, url_prefix="/users")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message": f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message": f"{cls.__name__} {model_id} not found"}, 404))

    return model

@bp.route("", methods=["POST"])
def create_user():
    request_body = request.get_json()

    new_user = User.from_dict(request_body)

    # check to see if exists in db
    existing_user = User.query.filter(User.email == request_body["email"]).first()
    if existing_user is not None:
        user_dict = existing_user.to_dict()
        return make_response(jsonify(user_dict, 201))

    db.session.add(new_user)
    db.session.commit()

    user_dict = new_user.to_dict()

    return make_response(jsonify(user_dict, 201))

@bp.route("/<user_id>/items", methods=["POST"])
def create_item(user_id):
    user = validate_model(User, user_id)

    request_body = request.get_json()
    new_item = Item(
        title=request_body["title"],
        brand=request_body["brand"],
        category=request_body["category"],
        size=request_body["size"],
        description=request_body["description"],
        user=user
    )

    db.session.add(new_item)
    db.session.commit()


    return make_response(jsonify(f"Item {new_item.title} by {new_item.user.name} posted"), 201)

@bp.route("/<user_id>/items", methods=["GET"])
def read_items_by_user(user_id):
    item_query = Item.query.filter(Item.user_id == user_id).all()
    item_response = [item.to_dict() for item in item_query]

    return jsonify(item_response), 201

# not for users
@bp.route("", methods=["GET"])
def read_all_users():
    users = User.query.all()

    users_response = [user.to_dict() for user in users]

    return jsonify(users_response), 200