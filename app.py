from flask import Flask
from flask_login import LoginManager
from flask_socketio import SocketIO

from config import Config
from database.db import db
from models.user import User

from routes.auth_routes import auth_bp
from routes.task_routes import task_bp
from routes.dashboard_routes import dashboard_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

socketio = SocketIO(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


app.register_blueprint(auth_bp)
app.register_blueprint(task_bp)
app.register_blueprint(dashboard_bp)


@app.route('/')
def home():
    return "<h2>Smart Task Management System</h2>"


@socketio.on('task_update')
def handle_task_update(data):
    socketio.emit('notification', {'message': data['message']})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    socketio.run(app, debug=True)
