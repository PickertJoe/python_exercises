# Creating a test for the class created in Employee.py

import unittest
from Employee import Employee


class EmployeeTestCase(unittest.TestCase):
    """Test for 'Employee.py'"""

    def setUp(self):
        """Creates an employee for use in all test methods"""
        self.my_employee = Employee('joe', 'pickert', 65000)

    def test_give_default_raise(self):
        """Test to ensure that default raise == $5000"""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 70000)

    def test_give_cust_raise(self):
        """Test to ensure that custom raises are applied appropriately"""
        self.my_employee.give_raise(10000)
        self.assertEqual(self.my_employee.salary, 75000)


unittest.main()
