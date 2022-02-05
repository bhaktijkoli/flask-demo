from http.client import BAD_REQUEST
from os import abort
from flask import Blueprint, jsonify, request
from app import db
from app.models import User
from app.schemas import CreateUserSchema, UserSchema, UsersSchema
from marshmallow import ValidationError


users = Blueprint("users", __name__, url_prefix="/api/v1/users")


@users.route("/", methods=["GET"])
def getUsers():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 20, type=int)
    pagination = User.query.paginate(page=page, per_page=per_page)
    data = UsersSchema.dump(pagination.items)
    return jsonify(page=pagination.page, pages=pagination.pages, per_page=pagination.per_page, total=pagination.total, data=data)


@users.route("/<id>", methods=["GET"])
def getUserByID(id):
    user = User.query.filter_by(id=id).first()
    return jsonify(data=UserSchema.dump(user))


@users.route("", methods=["POST"])
def addUser():
    try:
        CreateUserSchema().load(request.get_json())
        name = request.get_json().get("name", "")
        email = request.get_json().get("email", "")
        user = User(name, email, email)
        db.session.add(user)
        db.session.commit()
        return jsonify(data=UserSchema.dump(user))
    except ValidationError as err:
        return jsonify(err.messages), 400
