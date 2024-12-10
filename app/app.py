from flask import Flask
from routes.health_routes import health_routes
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)
app.register_blueprint(health_routes,url_prefix='/public/health')
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)
