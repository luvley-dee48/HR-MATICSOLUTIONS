from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import MetaData

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///hrMatic.db"
db = SQLAlchemy(app, metadata=MetaData())

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    roles = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    employee = db.relationship('Employee', backref='user', uselist=False)


class Department(db.Model):
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=True)
    employee = db.Column(db.String, nullable=True)

    employees = db.relationship('Employee', backref='department', lazy=True)


class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Integer, nullable=False)  
    phonenumber = db.Column(db.Integer, nullable=False)  
    address = db.Column(db.String(200), nullable=False)
    job_title = db.Column(db.String(80), nullable=False)
    department = db.Column(db.String, nullable=True)  
    date_hired = db.Column(db.DateTime, nullable=False)  
    salary = db.Column(db.Integer, nullable=False)  
    leave_records = db.Column(db.String, nullable=True)  

    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    leave_allocations = db.relationship('LeaveAllocation', backref='employee', lazy=True)
    leave_requests = db.relationship('LeaveRequest', backref='employee', lazy=True)

    @hybrid_property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class LeaveAllocation(db.Model):
    __tablename__ = 'leave_allocation'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    total_days_allocated = db.Column(db.Integer, nullable=False)
    days_used = db.Column(db.Integer, default=0)
    days_remaining = db.Column(db.Integer, nullable=False)

    @hybrid_property
    def employee_name(self):
        return self.employee.full_name


class LeaveRequest(db.Model):
    __tablename__ = 'leave_requests'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    employee_name = db.Column(db.String(120), nullable=False) 
    start_date = db.Column(db.DateTime, nullable=False)  
    end_date = db.Column(db.DateTime, nullable=False)  
    type = db.Column(db.String(50), nullable=False)  
    status = db.Column(db.String(20), nullable=False)
    days_requested = db.Column(db.Integer, nullable=False) 
    approver_name = db.Column(db.String(80), nullable=True)
