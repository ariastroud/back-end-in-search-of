from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.user import User

bp = Blueprint("user_bp", __name__, url_prefix="/users")

@bp.route("", methods=["POST"])
def create_user():
    request_body = request.get_json()

    # check to see if exists in db
    test_user = User.query.filter(User.email == request_body["email"]).first()
    if test_user is not None:
        return make_response('User in database')

    new_user = User.from_dict(request_body)

    db.session.add(new_user)
    db.session.commit()

    user_dict = new_user.to_dict()

    return make_response(jsonify({"user": user_dict}, 201))


@bp.route("", methods=["GET"])
def read_all_users():
    users = User.query.all()

    users_response = [user.to_dict() for user in users]

    return jsonify(users_response), 200