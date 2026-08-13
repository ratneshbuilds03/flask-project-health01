from flask import Blueprint, jsonify ,request
from app.services.task_service import create_task , get_all_tasks ,update_task ,get_task_by_id,delete_task
from flask_jwt_extended import jwt_required ,get_jwt_identity

task_bp = Blueprint("tasks", __name__)

@task_bp.route("/health",methods=["GET"])
def health_check():
    return jsonify({"status":"ok"}),200

@task_bp.route("/tasks",methods=["POST"])
@jwt_required()
def add_task():
    data = request.get_json()
    user_id =get_jwt_identity()
    
    if not data or not data.get("title"):
        return jsonify({"error":"title is required"}),400
    
    
    task =create_task(data,user_id)
    return jsonify(task),201
    
@task_bp.route("/tasks",methods=["GET"])
@jwt_required()
def list_task():
    
    user_id = get_jwt_identity()
    status=request.args.get("status")
    priority =request.args.get("priority")
    page=request.args.get("page",1,type=int)
    per_page=request.args.get("per_page",10,type=int)
    result = get_all_tasks(user_id,status,priority,page,per_page)
    return jsonify(result),200

@task_bp.route("/tasks/<int:task_id>",methods=["GET"])
def get_task(task_id):
    task=get_task_by_id(task_id)
    if not task:
        return jsonify({"error":"Task Not Found"}),404
    
    return jsonify(task),200

@task_bp.route("/tasks/<int:task_id>",methods=["PUT"])
def edit_task(task_id):
    data=request.get_json()
    task=update_task(task_id,data)
    if not task:
        return jsonify({"error":"Task Not Found"}),404
    return jsonify(task),200

@task_bp.route("/tasks/<int:task_id>",methods=["DELETE"])
def remove_task(task_id):
    task = delete_task(task_id)
    if not task:
        return jsonify({"error":"Task Not Found"}),404
    return jsonify({"Message":"Task Delete Successfully"}),200