from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from flaskr import apis, login, bcrypt, auth
from flask import Flask, session, request, abort, make_response
from models import models


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.password = self.password_to_hash(password)
    """
        Main common funtions and mechanisms
    """

    # generate hash
    def password_to_hash(self, password):
        return bcrypt.generate_password_hash(password).decode('utf-8')

    # verify hash
    def check_password(self, password) -> str:
        return check_password_hash(self.pw_hash, password)

    def log_in(self, username, password, table_name):
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400
        self.username = request.json.get('username', None)
        pwd_str = request.json.get('password', None)
        self.password = password_to_hash(pwd_str)
        if not username:
            return jsonify({"msg": "Missing username parameter"}), 400
        if not password:
            return jsonify({"msg": "Missing password parameter"}), 400
        if self.username != models.get_item_on_table(table_name, 'username', username) or self.password != models.get_item_on_table(table_name, 'password', self.password_to_hash(password)):
            return jsonify({"msg": "Bad username or password"}), 401
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

    def sign_up(self):
        self.username = request.args.get('username')
        self.password = self.password_to_hash(request.args.get('password'))
    
    """
        JWT Section
    """
    # authenticate user
    def authenticate(self, username, password):
        user = username.get(username, None)
        if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
            return user

    # keep user session
    @apis.route('/protected', methods=['GET'])
    @jwt_required
    def protected():
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), 200

    # identity payload
    def identity(payload):
        user_id = payload['identity']
        return userid_table.get(user_id, None)

    # uploading profile picture
    def upload_profile_picture(self, id):
        pass

## Flask-JWT Config
# apis.debug = True
# apis.config['SECRET_KEY'] = 'super-secret'
# apis.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
# jwt = JWT(apis)

# api.add_resource(User, '/user')

# if __name__ == '__main__':
#     app.run(debug=True)