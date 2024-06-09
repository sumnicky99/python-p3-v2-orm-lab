#!/usr/bin/env python3
# Shebang line specifying the Python interpreter to use

from __init__ import CONN, CURSOR
# Importing CONN and CURSOR objects from __init__.py for database interaction

import random
# Importing the random module for generating random numbers

from department import Department
from employee import Employee
from review import Review
# Importing classes from respective modules for database operations

import ipdb
# Importing the ipdb module for debugging

def reset_database():
    """Function to reset the database with seed data"""
    
    # Drop existing tables
    Review.drop_table()
    Employee.drop_table()
    Department.drop_table()
    
    # Create tables
    Department.create_table()
    Employee.create_table()
    Review.create_table()

    # Create seed data
    # Create departments
    payroll = Department.create("Payroll", "Building A, 5th Floor")
    human_resources = Department.create("Human Resources", "Building C, East Wing")
    
    # Create employees
    employee1 = Employee.create("Lee", "Manager", payroll.id)
    employee2 = Employee.create("Sasha", "Manager", human_resources.id)
    
    # Create reviews for employees
    Review.create(2023, "Efficient worker", employee1.id)
    Review.create(2022, "Good work ethic", employee1.id)
    Review.create(2023, "Excellent communication skills", employee2.id)

# Call the reset_database function to reset the database
reset_database()

# Set a breakpoint using ipdb for debugging
ipdb.set_trace()
