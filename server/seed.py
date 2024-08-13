# from faker import Faker
# from sqlalchemy import func
# from app import app
# from models import db, Employees, Departments
# with app.app_context():
#     fake = Faker()

#     # Delete all records/rows in the Employees table
#     Employees.query.delete()
    
#     # List to hold the employees
#     employees = []

#     job_titles = ['Software Developer', 'Product Manager', 'Accountant', 'Sales Manager', 'Customer Support']
#     departments = ['Human Resource', 'Product Management', 'Sales and Marketing', 'IT Support', 'Finance']
#     roles = ['HR', 'Admin', 'Employee']

#     # Generate fake data for  employees
#     for _ in range(6):
#         first_name = fake.first_name()
#         last_name = fake.last_name()
#         domain = fake.free_email_domain()
#         email = f"{first_name.lower()}.{last_name.lower()}@{domain}"
#         password = fake.password()
#         phone_number = fake.phone_number()
#         address = fake.address()
#         job_title = fake.choice(job_titles)
#         department = fake.choice(departments)
#         date_hired = fake.date_time_this_decade()
#         salary = fake.random.randint(50000, 150000)
#         leave_records = fake.date_time_this_year()
#         role = fake.random(roles)

#         # Create an Employee object
#         employee = Employees(
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             password=password,
#             phone_number=phone_number,
#             address=address,
#             job_title=job_title,
#             department=department,
#             date_hired=date_hired,
#             salary=salary,
#             leave_records=leave_records
#         )

#         # Add the employee to the session
#         employees.append(employee)

#     # Add all employees to the database and commit
#     db.session.add_all(employees)
#     db.session.commit()

#     Departments.query.delete()

#     departments=[]

#     departments = ['Human Resource', 'Product Management', 'Sales and Marketing', 'IT Support', 'Finance']
#     description = ['The Human Resource department is responsible for managing the organizations most valuable asset: its employees. This department handles recruitment, employee relations, performance management, training and development, compensation and benefits, and compliance with labor laws. HR ensures that the company attracts, retains, and develops talent, fostering a positive work environment and aligning the workforce with the companys goals.' ,
                   
#      'The Product Management department is responsible for the strategy, roadmap, and feature definition of a product or a product line. Product managers work closely with engineering, design, marketing, and sales teams to ensure that products meet customer needs, are delivered on time, and align with the companys business objectives. They are involved in the entire product lifecycle, from ideation and development to launch and iteration.' , 

#     'The Sales and Marketing department is responsible for driving revenue by promoting the companys products or services and converting leads into customers. Marketing teams focus on market research, brand management, advertising, and content creation to attract potential customers. Sales teams then engage with prospects, build relationships, and close deals. This department is crucial for creating demand, expanding market reach, and achieving the companys growth targets.' 'The IT Support department provides technical assistance and support for the organizations computer systems, networks, and users. This department handles the installation, maintenance, and troubleshooting of hardware and software, ensuring that all technology functions smoothly. IT Support is essential for minimizing downtime, securing data, and enabling employees to use technology efficiently in their daily tasks.' , 

#     'The Finance department is responsible for managing the companys financial health. This includes budgeting, forecasting, accounting, financial reporting, tax management, and investment planning. The finance team ensures that the company has the financial resources to operate, grow, and meet its obligations. They also provide insights and analysis to guide strategic decision-making and maintain compliance with financial regulations.']

#     total_number_employees=['3', '4', '2', '3', '2']
# for _ in range (6): 

#     Department_name = fake.choice(departments)
#     Description = fake.choice(description)
#     Employees = fake.choice(total_number_employees)





#     Leave_Requests.query.delete()

#     leave_requests=[]

# employee_name = ['James Williams', 'Samantha Browns', 'Roman James', 'Moses Samuels']
# leave_type = ['Maternity Leave', 'Sick Leave', 'Annual Leave', 'Compansionate Leave', 'Paternity Leave']
# status = ['Approved', 'Pending', 'Rejected']
# approvername = ['Joseph', 'Deborah', 'Arnold']


# for _in range (6):

#     employee_name = fake.choice(employee_name)
#     start_date = fake.date_time
#     end_date = fake.date_time
#     leave_type =  fake.choice(leave_type)
#     status = fake.choice(status)
#     days_requested = fake.random.randint[2,30]
#     approver_name = fake.random(approvername)


# Leave_allocation.query.delete()

# leave_allocation=[]

# year = ['2022', '2023', '2024']

# employee_id = fake.random.randint(1,6)
# year = fake.choice(year)
# total_days_allocated = fake.random.randint[30]
# days_used = fake.random.randint[1,30]
# days_remaining = fake.random.randint[1,30]

from faker import Faker
from app import app
from models import db, Employees, Departments, LeaveRequests, LeaveAllocation

with app.app_context():
    fake = Faker()

    # Delete all records/rows in the Employees table
    Employees.query.delete()

    # List to hold the employees
    employees = []

    job_titles = ['Software Developer', 'Product Manager', 'Accountant', 'Sales Manager', 'Customer Support']
    departments = ['Human Resource', 'Product Management', 'Sales and Marketing', 'IT Support', 'Finance']
    roles = ['HR', 'Admin', 'Employee']

    # Generate fake data for employees
    for _ in range(6):
        first_name = fake.first_name()
        last_name = fake.last_name()
        domain = fake.free_email_domain()
        email = f"{first_name.lower()}.{last_name.lower()}@{domain}"
        password = fake.password()
        phone_number = fake.phone_number()
        address = fake.address()
        job_title = fake.random.choice(job_titles)
        department = fake.random.choice(departments)
        date_hired = fake.date_time_this_decade()
        salary = fake.random.randint(50000, 150000)
        leave_records = fake.date_time_this_year()
        role = fake.random.choice(roles)

        # Create an Employee object
        employee = Employees(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            phone_number=phone_number,
            address=address,
            job_title=job_title,
            department=department,
            date_hired=date_hired,
            salary=salary,
            leave_records=leave_records
        )

        # Add the employee to the session
        employees.append(employee)

    # Add all employees to the database and commit
    db.session.add_all(employees)
    db.session.commit()

    # Delete all records/rows in the Departments table
    Departments.query.delete()

    departments_list = []

    department_names = ['Human Resource', 'Product Management', 'Sales and Marketing', 'IT Support', 'Finance']
    descriptions = [
        'The Human Resource department is responsible for managing the organization’s most valuable asset: its employees. This department handles recruitment, employee relations, performance management, training and development, compensation and benefits, and compliance with labor laws. HR ensures that the company attracts, retains, and develops talent, fostering a positive work environment and aligning the workforce with the company’s goals.',
        'The Product Management department is responsible for the strategy, roadmap, and feature definition of a product or a product line. Product managers work closely with engineering, design, marketing, and sales teams to ensure that products meet customer needs, are delivered on time, and align with the company’s business objectives. They are involved in the entire product lifecycle, from ideation and development to launch and iteration.',
        'The Sales and Marketing department is responsible for driving revenue by promoting the company’s products or services and converting leads into customers. Marketing teams focus on market research, brand management, advertising, and content creation to attract potential customers. Sales teams then engage with prospects, build relationships, and close deals. This department is crucial for creating demand, expanding market reach, and achieving the company’s growth targets.',
        'The IT Support department provides technical assistance and support for the organization’s computer systems, networks, and users. This department handles the installation, maintenance, and troubleshooting of hardware and software, ensuring that all technology functions smoothly. IT Support is essential for minimizing downtime, securing data, and enabling employees to use technology efficiently in their daily tasks.',
        'The Finance department is responsible for managing the company’s financial health. This includes budgeting, forecasting, accounting, financial reporting, tax management, and investment planning. The finance team ensures that the company has the financial resources to operate, grow, and meet its obligations. They also provide insights and analysis to guide strategic decision-making and maintain compliance with financial regulations.'
    ]

    total_number_employees = [3, 4, 2, 3, 2]

    for i in range(5):
        department = Departments(
            department_name=department_names[i],
            description=descriptions[i],
            total_number_employees=total_number_employees[i]
        )
        departments_list.append(department)

    db.session.add_all(departments_list)
    db.session.commit()

    # Delete all records/rows in the LeaveRequests table
    LeaveRequests.query.delete()

    leave_requests = []

    employee_names = ['James Williams', 'Samantha Browns', 'Roman James', 'Moses Samuels']
    leave_types = ['Maternity Leave', 'Sick Leave', 'Annual Leave', 'Compassionate Leave', 'Paternity Leave']
    statuses = ['Approved', 'Pending', 'Rejected']
    approver_names = ['Joseph', 'Deborah', 'Arnold']

    for _ in range(6):
        employee_name = fake.random.choice(employee_names)
        start_date = fake.date_this_year()
        end_date = fake.date_this_year()
        leave_type = fake.random.choice(leave_types)
        status = fake.random.choice(statuses)
        days_requested = fake.random.randint(2, 30)
        approver_name = fake.random.choice(approver_names)

        leave_request = LeaveRequests(
            employee_name=employee_name,
            start_date=start_date,
            end_date=end_date,
            leave_type=leave_type,
            status=status,
            days_requested=days_requested,
            approver_name=approver_name
        )

        leave_requests.append(leave_request)

    db.session.add_all(leave_requests)
    db.session.commit()

    # Delete all records/rows in the LeaveAllocation table
    LeaveAllocation.query.delete()

    leave_allocation = []

    years = ['2022', '2023', '2024']

    for _ in range(6):
        employee_id = fake.random.randint(1, 6)
        year = fake.random.choice(years)
        total_days_allocated = fake.random.randint(15, 30)
        days_used = fake.random.randint(1, total_days_allocated)
        days_remaining = total_days_allocated - days_used

        allocation = LeaveAllocation(
            employee_id=employee_id,
            year=year,
            total_days_allocated=total_days_allocated,
            days_used=days_used,
            days_remaining=days_remaining
        )

        leave_allocation.append(allocation)

    db.session.add_all(leave_allocation)
    db.session.commit()
