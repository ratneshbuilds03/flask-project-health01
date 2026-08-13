from flask import jsonify

def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error":"Resource not found"}),404
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"error":"Bad Request"}),400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({"error":" Unauthorized Access"}),401

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error":"Something Want Wrong , Please try again later.."}),500
        
    @app.errorhandler(Exception)
    def handle_exception(error):
        return jsonify({'error':"An unaxepected error occurted"}),500
        


    
    
    