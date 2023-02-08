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
    if existing_user:
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
        file=request_body["file"],
        user=user
    )

    db.session.add(new_item)
    db.session.commit()

    item_dict = new_item.to_dict()


    return make_response(jsonify({"item": item_dict}), 201)

@bp.route("/<user_id>/items", methods=["GET"])
def read_items_by_user(user_id):
    filter_query = request.args.get("filter")

    size_filters = ["none", "xs", "s", "m", "l", "xl", "2xl"]
    size_filters_strings = ["N/A", "XS (0-2)", "S (4-6)", "M (8-10)", "L (12-14)", "XL (16)", "2XL (18-20)"]

    category_filters = ["clothing", "handbags", "jewelry", "shoes"]
    category_filters_strings = ["Clothing", "Handbags", "Jewelry", "Shoes"]

    if filter_query in size_filters:
        filter_string_index = int(size_filters.index(filter_query))
        item_query = Item.query.filter(Item.user_id == user_id).filter(Item.size == size_filters_strings[filter_string_index]).order_by(Item.item_id.desc())
    elif filter_query in category_filters:
        filter_string_index = int(category_filters.index(filter_query))
        item_query = Item.query.filter(Item.user_id == user_id).filter(Item.category == category_filters_strings[filter_string_index]).order_by(Item.item_id.desc())
    else:
        item_query = Item.query.filter(Item.user_id == user_id).order_by(Item.item_id.desc()).all()

    item_response = [item.to_dict() for item in item_query]

    return jsonify(item_response), 201

# not for users
@bp.route("", methods=["GET"])
def read_all_users():
    users = User.query.all()

    users_response = [user.to_dict() for user in users]

    return jsonify(users_response), 200