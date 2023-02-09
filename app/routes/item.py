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

    size_filters = ["none", "xs", "s", "m", "l", "xl", "2xl", "5", "6", "7", "8", "9", "10", "11"]
    size_filters_strings = ["N/A", "XS (0-2)", "S (4-6)", "M (8-10)", "L (12-14)", "XL (16)", "2XL (18-20)", "5", "6", "7", "8", "9", "10", "11"]

    category_filters = ["clothing", "handbags", "jewelry", "shoes"]
    category_filters_strings = ["Clothing", "Handbags", "Jewelry", "Shoes"]

    if filter_query in size_filters:
        filter_string_index = int(size_filters.index(filter_query))
        item_query = Item.query.filter(Item.size == size_filters_strings[filter_string_index]).order_by(Item.item_id.desc())
    elif filter_query in category_filters:
        filter_string_index = int(category_filters.index(filter_query))
        item_query = Item.query.filter(Item.category == category_filters_strings[filter_string_index]).order_by(Item.item_id.desc())
    elif not filter_query:
        item_query = Item.query.order_by(Item.item_id.desc())

    item_response = [item.to_dict() for item in item_query]

    return jsonify(item_response), 201

@bp.route("search", methods=["GET"])
def search_items():
    title_query = request.args.get("title")
    filter_query = request.args.get("filter")

    size_filters = ["none", "xs", "s", "m", "l", "xl", "2xl"]
    size_filters_strings = ["N/A", "XS (0-2)", "S (4-6)", "M (8-10)", "L (12-14)", "XL (16)", "2XL (18-20)"]

    category_filters = ["clothing", "handbags", "jewelry", "shoes"]
    category_filters_strings = ["Clothing", "Handbags", "Jewelry", "Shoes"]

    if filter_query in size_filters:
        filter_string_index = int(size_filters.index(filter_query))
        item_query = Item.query.filter(Item.title.ilike(f'%{title_query}%')).filter(Item.size == size_filters_strings[filter_string_index]).order_by(Item.item_id.desc())
    elif filter_query in category_filters:
        filter_string_index = int(category_filters.index(filter_query))
        item_query = Item.query.filter(Item.title.ilike(f'%{title_query}%')).filter(Item.category == category_filters_strings[filter_string_index]).order_by(Item.item_id.desc())
    else:
        item_query = Item.query.filter(Item.title.ilike(f'%{title_query}%')).order_by(Item.item_id.desc())

    item_response = [item.to_dict() for item in item_query]

    return jsonify(item_response), 201

@bp.route("<item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = validate_model(Item, item_id)

    db.session.delete(item)
    db.session.commit()

    return (f"Item {item.item_id} successfully deleted!")

@bp.route("<item_id>/mark_found", methods=["PATCH"])
def update_item(item_id):
    item = validate_model(Item, item_id)
    item.found = True
    db.session.commit()

    return {"item": item.to_dict()}

@bp.route("/<item_id>", methods=["GET"])
def handle_item(item_id):
    item = validate_model(Item, item_id)
    item_response = item.to_dict()

    return jsonify(item_response), 200







