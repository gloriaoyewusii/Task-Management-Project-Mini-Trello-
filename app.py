import os
from datetime import timedelta
# from src.extensions import db
from flask import Flask
from flask_jwt_extended import JWTManager
from mongoengine import connect

from src.routers.boardrouter import board_router
from src.routers.taskrouter import task_router
from src.routers.user_router import user_router

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=30)
app.config['JWT_TOKEN_LOCATION'] = ['headers']
app.config['JWT_HEADER_NAME'] = 'Authorization'
app.config['JWT_HEADER_TYPE'] = 'Bearer'

connect(
    db='task-management',
    host='localhost',
    port=27017,
)

jwt = JWTManager(app)
app.register_blueprint(user_router)
app.register_blueprint(task_router)
app.register_blueprint(board_router)


@app.route('/')
def hello_world():  # put application's code here
    return '<p>Hello World!</p>'


if __name__ == '__main__':
    app.run(debug=True)
