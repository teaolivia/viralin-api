from flaskr import apis, login, bcrypt, auth
from flask import Flask, session, request, abort, make_response
from flask_cognito import cognito_auth_required, current_user, current_cognito_jwt
from models import models


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
    """
        Main common funtions and mechanisms
    """
    # generate hash
    def set_password(self, password):
        self.pw_hash = bcrypt.generate_password_hash(password)

    # verify hash
    def check_password(self, password) -> str:
        return check_password_hash(self.pw_hash, password)

    def log_in(self, username, password):
        self.username = request.json.get('username')
        self.password = request.json.get('password')
        if self.username is None or self.password is None:
            abort(400)
        if self.check_password(self.password):
            session['logged_in'] = True
        else:
            print('wrong password')

    def sign_up(self):
        self.username = request.args.get('username')
        self.password = bcrypt.generate_password_hash(request.args.get('password')).decode('utf-8')
    
    """
        JWT Section
    """
    # authenticate user
    def authenticate(self, username, password):
        user = username.get(username, None)
        if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
            return user
    
    # identity payload
    def identity(payload):
        user_id = payload['identity']
        return userid_table.get(user_id, None)

    # uploading profile picture
    def upload_profile_picture(self, id):
        pass


    """ 
        AWS Cognito configuration
    """
    @route('/api/private')
    @cognito_auth_required
    def api_private():
        # user must have valid cognito access or ID token in header
        # (accessToken is recommended - not as much personal information contained inside as with idToken)
        return jsonify({
            'cognito_username': current_cognito_jwt['username'],   # from cognito pool
            'user_id': current_user.id,   # from your database
        })

## Flask-JWT Config
# apis.debug = True
# apis.config['SECRET_KEY'] = 'super-secret'
# apis.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
# jwt = JWT(apis)

# api.add_resource(User, '/user')

# if __name__ == '__main__':
#     app.run(debug=True)