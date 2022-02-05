from app import ma
from marshmallow import fields, validates, ValidationError

from app.models import User


class UserSchemaClass(ma.Schema):
    class Meta:
        fields = ("id", "name", "email", "created_at", "updated_at")


class CreateUserSchema(ma.Schema):
    name = fields.Str(required=True)
    email = fields.Str(required=True)

    @validates("email")
    def email_already_taken(self, value):
        print(value)
        user = User.query.filter_by(email=value).first()
        if user:
            raise ValidationError("Email is already taken")


UserSchema = UserSchemaClass()
UsersSchema = UserSchemaClass(many=True)
