from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///hrMatic.db"
db = SQLAlchemy(app, metadata=MetaData())

class SerializerMixin:
    def serialize(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

class Department(db.Model, SerializerMixin):
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=True)

    employees = db.relationship('Employee', backref='department', lazy=True)

    @hybrid_property
    def total_employees(self):
        return len(self.employees)

    def serialize(self):
        data = super().serialize()
        data['total_employees'] = self.total_employees
        return data


class Employee(db.Model, SerializerMixin):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)  
    phonenumber = db.Column(db.String(20), nullable=False)  
    address = db.Column(db.String(200), nullable=False)
    job_title = db.Column(db.String(80), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    date_hired = db.Column(db.DateTime, nullable=False)  
    salary = db.Column(db.Integer, nullable=False)  
    leave_records = db.Column(db.String, nullable=True)
    role = db.Column(db.String(80), nullable=False)  # Role field added

    leave_allocations = db.relationship('LeaveAllocation', backref='employee', lazy=True)
    leave_requests = db.relationship('LeaveRequest', backref='employee', lazy=True)

    @hybrid_property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def serialize(self):
        data = super().serialize()
        data['full_name'] = self.full_name
        data['leave_allocations'] = [allocation.serialize() for allocation in self.leave_allocations]
        data['leave_requests'] = [request.serialize() for request in self.leave_requests]
        return data


class LeaveAllocation(db.Model, SerializerMixin):
    __tablename__ = 'leave_allocation'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    total_days_allocated = db.Column(db.Integer, nullable=False)
    days_used = db.Column(db.Integer, default=0)
    days_remaining = db.Column(db.Integer, nullable=False)
    employee_name_column = db.Column(db.String(160), nullable=False)  # Renamed column

    @hybrid_property
    def employee_name(self):
        return self.employee.full_name

    def serialize(self):
        data = super().serialize()
        data['employee_name'] = self.employee_name
        return data


class LeaveRequest(db.Model, SerializerMixin):
    __tablename__ = 'leave_requests'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)  
    end_date = db.Column(db.DateTime, nullable=False)  
    type = db.Column(db.String(50), nullable=False)  
    status = db.Column(db.String(20), nullable=False)
    days_requested = db.Column(db.Integer, nullable=False) 
    approver_name = db.Column(db.String(80), nullable=True)
