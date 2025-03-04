from app import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "email", "password_hash", "about_me", "last_seen")

user_schema = UserSchema()
users_schema = UserSchema(many=True)