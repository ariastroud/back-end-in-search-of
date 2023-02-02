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

@bp.route("", methods=["GET"])
def read_all_items():
    filter_query = request.args.get("filter")

    if filter_query == "xs":
        items = Item.query.filter(Item.size == "XS (0-2)")
    elif filter_query == "s":
        items = Item.query.filter(Item.size == "S (4-6)")
    elif filter_query == "m":
        items = Item.query.filter(Item.size == "M (8-10)")
    elif filter_query == "l":
        items = Item.query.filter(Item.size == "L (12-14)")
    elif filter_query == "xl":
        items = Item.query.filter(Item.size == "XL (16)")
    elif filter_query == "2xl":
        items = Item.query.filter(Item.size == "2XL (18-20)")
    elif filter_query == "clothing":
        items = Item.query.filter(Item.category == "Clothing")
    elif filter_query == "handbags":
        items = Item.query.filter(Item.category == "Handbags")
    elif filter_query == "jewelry":
        items = Item.query.filter(Item.category == "Jewelry")
    elif filter_query == "accessories":
        items = Item.query.filter(Item.category == "Accessories")
    elif filter_query == "shoes":
        items = Item.query.filter(Item.category == "Shoes")
    else:
        items = Item.query.all()

    items_response = [item.to_dict() for item in items]

    return jsonify(items_response), 200

@bp.route("search", methods=["GET"])
def search_items():
    title_query = request.args.get("title")

    if title_query:
        items = Item.query.filter(Item.title.ilike(f'%{title_query}%'))
    else:
        return (f'something went wrong~')
    
    items_response = [item.to_dict() for item in items]

    return jsonify(items_response), 200

@bp.route("<item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = validate_model(Item, item_id)

    db.session.delete(item)
    db.session.commit()

    return (f"Item {item.item_id} successfully deleted!")

