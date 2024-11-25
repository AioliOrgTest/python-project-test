from flask import Blueprint, jsonify
health_routes=Blueprint('health_routes',__name__)
@health_routes.route('/v1/ping',methods=['GET'])
def ping():
    """
    /v1/ping endpoint returning 'pong'.
    ---
    responses:
      200:
        description: A successful response with 'pong'.
    """
    return 'pong'

@health_routes.route('/v1/all',methods=['GET'])
def health():
    """
    Health endpoint returning JSON response.
    ---
    responses:
      200:
        description: A successful response with status 'OK'.
        schema:
          type: object
          properties:
            status:
              type: string
              example: "OK"
    """
    return jsonify({'status':'OK'})
