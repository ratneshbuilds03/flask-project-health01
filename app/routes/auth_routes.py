from flask import Blueprint ,request ,jsonify
from app.services.auth_service import login_user ,signup_user

auth_bp = Blueprint("auth",__name__)

@auth_bp.route("/signup",methods=["POST"])
def signup():
    data=request.get_json()
    if not data or not data.get('email') or not data.get('password') or not data.get('name'):
        return jsonify({"error":"name , email or password are required"}),400

    user,error=signup_user(data)

    if error:
        return jsonify({"error":error}),404
    
    return jsonify(user),201


@auth_bp.route("/login",methods=["POST"])
def login():
    data=request.get_json()
    
    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"error":"Email or password are required"}),400
    
    result ,error = login_user(data)
    
    if error:
        return jsonify({"error":error}),401
    
    return jsonify(result),200
