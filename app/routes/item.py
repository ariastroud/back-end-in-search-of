from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.item import Item

bp = Blueprint("item_bp", __name__, url_prefix="/items")

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

    new_item = Item.from_dict(request_body)

    db.session.add(new_item)
    db.session.commit()

    item_dict = new_item.to_dict()

    return make_response(jsonify({"item": item_dict}, 201))

@bp.route("", methods=["GET"])
def read_all_items():
    items = Item.query.all()

    items_response = [item.to_dict() for item in items]

    return jsonify(items_response), 200

@bp.route("<item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = validate_model(Item, item_id)

    db.session.delete(item)
    db.session.commit()

    return (f"Item {item.item_id} successfully deleted!")

