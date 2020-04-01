from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ASFNSFJ56708559564$*%^$&%('
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:8889/blog_flask'
db = SQLAlchemy(app)

class Users(db.Model):
    usr_id = db.Column(db.Integer, primary_key=True)
    usr_username = db.Column(db.String(50))
    usr_password = db.Column(db.String(200))
    usr_token = db.Column(db.String(200))
    usr_status = db.Column(db.Boolean)

class Posts(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(255))
    post_content = db.Column(db.String(255))
    post_time = db.Column(db.String(255))
    filename = db.Column(db.String(255))

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None
        # current_user =''
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
            # return token
        # return token
        if not token:
            return jsonify({'message': 'a valid token is missing'})
        # return token
        try:
            # return token
            data = jwt.decode(token, app.config['SECRET_KEY'])
            # return data
            current_user = Users.query.filter_by(usr_username=data['username']).first()
            # return current_user
        except:
           return jsonify({'message': 'token is invalid1'})
          
        return f(current_user, *args, **kwargs)

    return decorator


@app.route('/register', methods=['GET', 'POST'])
def signup_user():
    data = request.get_json(force=True)
    # return request.json.get('username')
    # return format(data)
    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = Users(usr_username=data['username'], usr_password=hashed_password, usr_token ='', usr_status=1)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'registered successfully'})

@app.route('/login1', methods=['GET', 'POST'])
def login_user():
    auth = request.authorization
    # return auth
    if not auth or not auth.username or not auth.password:
        return make_response('could not verify1', 401, {'WWW.Authentication': 'Basic realm: "login required"'})
    
    user = Users.query.filter_by(usr_username=auth.username).first()

    if check_password_hash(user.usr_password, auth.password):
        token = jwt.encode({'username': user.usr_username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token' : token.decode('UTF-8')})
    
    return make_response('could not verify',  401, {'WWW.Authentication': 'Basic realm: "login required"'})




@app.route('/users', methods=['GET'])

def get_all_users():
    users = Users.query.all()
    result = []

    for user in users:
        user_data = {}
        user_data['id'] = user.usr_id
        user_data['username'] = user.usr_username
        user_data['password'] = user.usr_password
        user_data['token'] = user.usr_token
        user_data['status'] = user.usr_status

        result.append(user_data)
    return jsonify(result)

@app.route("/createpost", methods=['POST','GET'])
@token_required
def posts(current_user):
    now = datetime.datetime.utcnow()
    my_datetime = now.strftime('%Y-%m-%d %H:%M:%S')
    data = request.get_json(force=True)
    # return data
    new_post = Posts(post_title=data['post_title'],post_content=data['post_content'],post_time=my_datetime,filename=data['filename'])
    db.session.add(new_post)
    db.session.commit()

    return jsonify({'message':"new post created"})

@app.route("/posts/<post_id>", methods=['GET'])
@token_required
def get_post(current_user,post_id):
    posts = Posts.query.filter_by(post_id=post_id).all()

    if not posts:
       return jsonify({'message': 'Post does not exist'})
    
    output = []

    for post in posts:
        post_data = {}
        post_data['post_title']=post.post_title
        post_data['post_content']=post.post_content
        post_data['filename']=post.filename

        output.append(post_data)

    return jsonify({"list of posts":output})


@app.route('/post/delete/<post_id>', methods = ['DELETE'])
@token_required
def post_delete(current_user,post_id):
    posts = Posts.query.filter_by(post_id=post_id).first()
    if not posts:
        return jsonify({"message":"Post does not exists"})
    
    db.session.delete(posts)
    db.session.commit()

    return jsonify({"message":"Post with id "+ post_id+" deleted"})



app.run(debug=True)
