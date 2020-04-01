from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import jwt
import datetime
from  functools import wraps
app = Flask(__name__)

app.config['SECRETE_KEY'] = 'alskfsk^$$^*(bfksdfbs'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        
        if not token:
            return jsonify({'message':'Token is missing'}),403
        
        # return jwt.decode(token,app.config['SECRETE_KEY'])

        try:
            data = jwt.decode(token,app.config['SECRETE_KEY'])
        except:
            return jsonify({'message':'Token is invalid'}),403
        
        return f(*args, **kwargs)

    return decorated



@app.route('/unprotected')
def unprotected():
    return jsonify({'message':'anyone can view this'})

@app.route('/protected')
@token_required
def protected():
    return jsonify({'message':'admin can view this'})

@app.route('/login')
def login():
    auth = request.authorization
    
    # if auth and auth.password =='password':
        # return ''

    if not auth:
        return make_response('Could not verify alok',401,{'WWW.Authenticate':'Basic realm= "login Required"'})

    
    token   =jwt.encode({'user':auth.username,'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=30)}, app.config['SECRETE_KEY'])
    return jsonify({'token':token.decode('UTF-8')})



if __name__ == '__main__':
    app.run(debug=True)