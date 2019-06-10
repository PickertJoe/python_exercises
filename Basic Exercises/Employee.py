# Creating a class for use in later testing


class Employee():
    """Create a unique employee with personal information"""

    def __init__(self, first, last, salary):
        """Creates a new employee"""
        self.first = first.title()
        self.last = last.title()
        self.salary = int(salary)

    def give_raise(self, number=""):
        """Awards the employee a raise of $5000 by default or more/less if specified"""
        if number:
            self.salary += number
        else:
            self.salary += 5000

    def show_info(self):
        print("Employee name: " + self.first + " " + self.last)
        print("Employee salary: " + str(self.salary))
