from app import db
from app.models.user import User
from flask_jwt_extended import create_access_token

def signup_user(data):
    email = data.get("email")
    existing_user =User.query.filter_by(email=email).first()
    if existing_user:
        return None,"email Already Registerd"
    new_user = User(
        name=data.get("name"),
        email=email
        )
    
    new_user.set_password(data.get("password"))
    
    db.session.add(new_user)
    db.session.commit()
    
    return new_user.to_dict(),None


def login_user(data):
    email = data.get("email")
    password = data.get("password")
    
    user = User.query.filter_by(email=email).first()
    
    if not user or not user.check_password(password):
        return None ,"Invalid email or Password"
    
    access_token= create_access_token(identity=str(user.id))
    return {"access_token":access_token,"user":user.to_dict()},None