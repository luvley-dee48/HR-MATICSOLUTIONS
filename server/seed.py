from app import app
from models import db, Department, Employee, LeaveAllocation, LeaveRequest
from datetime import datetime

with app.app_context():
    # Drop all tables and recreate them
    db.drop_all()
    db.create_all()

    # Clear existing data
    Department.query.delete()
    Employee.query.delete()
    LeaveAllocation.query.delete()
    LeaveRequest.query.delete()
    
    departments = [
        {'name': 'Engineering', 'description': 'Handles all engineering and technical tasks.'},
        {'name': 'Human Resources', 'description': 'Manages recruitment, employee relations, and benefits.'},
        {'name': 'Marketing', 'description': 'Responsible for promoting and selling products or services.'},
        {'name': 'Sales', 'description': 'Handles sales and customer relationships.'},
    ]

    db.session.add_all([Department(**d) for d in departments])
    db.session.commit()

    employees = [
        {'first_name': 'John', 'last_name': 'Doe', 'email': 'john.doe@example.com', 'password': 'hashed_password_1', 'phonenumber': '123-456-7890', 'address': '123 Elm Street', 'job_title': 'Software Engineer', 'department_id': 1, 'date_hired': datetime(2023, 1, 15), 'salary': 90000, 'leave_records': '[]', 'role': 'Employee'},
        {'first_name': 'Jane', 'last_name': 'Smith', 'email': 'jane.smith@example.com', 'password': 'hashed_password_2', 'phonenumber': '123-456-7891', 'address': '456 Oak Avenue', 'job_title': 'HR Manager', 'department_id': 2, 'date_hired': datetime(2022, 11, 1), 'salary': 75000, 'leave_records': '[]', 'role': 'Employee'},
        {'first_name': 'Alice', 'last_name': 'Johnson', 'email': 'alice.johnson@example.com', 'password': 'hashed_password_3', 'phonenumber': '123-456-7892', 'address': '789 Pine Road', 'job_title': 'Marketing Specialist', 'department_id': 3, 'date_hired': datetime(2023, 3, 25), 'salary': 65000, 'leave_records': '[]', 'role': 'HR'},
        {'first_name': 'Bob', 'last_name': 'Brown', 'email': 'bob.brown@example.com', 'password': 'hashed_password_4', 'phonenumber': '123-456-7893', 'address': '101 Maple Lane', 'job_title': 'Sales Representative', 'department_id': 4, 'date_hired': datetime(2021, 7, 10), 'salary': 55000, 'leave_records': '[]', 'role': 'Admin'},
    ]

    db.session.add_all([Employee(**e) for e in employees])
    db.session.commit()

    leave_allocations = [
        {'employee_id': 1, 'year': 2024, 'total_days_allocated': 20, 'days_used': 5, 'days_remaining': 15, 'employee_name_column': 'John Doe'},
        {'employee_id': 2, 'year': 2024, 'total_days_allocated': 25, 'days_used': 10, 'days_remaining': 15, 'employee_name_column': 'Jane Smith'},
        {'employee_id': 3, 'year': 2024, 'total_days_allocated': 15, 'days_used': 2, 'days_remaining': 13, 'employee_name_column': 'Alice Johnson'},
        {'employee_id': 4, 'year': 2024, 'total_days_allocated': 18, 'days_used': 4, 'days_remaining': 14, 'employee_name_column': 'Bob Brown'},
    ]

    db.session.add_all([LeaveAllocation(**l) for l in leave_allocations])
    db.session.commit()

    leave_requests = [
        {'employee_id': 1, 'start_date': datetime(2024, 6, 1), 'end_date': datetime(2024, 6, 5), 'type': 'Vacation', 'status': 'Approved', 'days_requested': 5, 'approver_name': 'Jane Smith'},
        {'employee_id': 2, 'start_date': datetime(2024, 7, 10), 'end_date': datetime(2024, 7, 12), 'type': 'Sick Leave', 'status': 'Approved', 'days_requested': 3, 'approver_name': 'John Doe'},
        {'employee_id': 3, 'start_date': datetime(2024, 8, 15), 'end_date': datetime(2024, 8, 18), 'type': 'Personal', 'status': 'Pending', 'days_requested': 4, 'approver_name': None},
        {'employee_id': 4, 'start_date': datetime(2024, 9, 1), 'end_date': datetime(2024, 9, 7), 'type': 'Vacation', 'status': 'Approved', 'days_requested': 7, 'approver_name': 'Alice Johnson'},
    ]

    db.session.add_all([LeaveRequest(**r) for r in leave_requests])
    db.session.commit()
