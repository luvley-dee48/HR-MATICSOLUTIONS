from flask import Flask
from flask_migrate import Migrate
from models import db, Department, Employee, LeaveAllocation, LeaveRequest


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hrMatic.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

migrate= Migrate(app, db)

db.init_app(app)


