# this file contains elementary exercises involving class construction and utilization


# creating a basic class with attributes and methods


class User():
    """Creates a basic user class to store personal data"""

    def __init__(self, first_name, last_name, age, job):
        """Creates an instance for a user profile"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = str(age)
        self.job = job.title()
        self.login_attempts = 0

    def describe_user(self):
        """Prints a neat summary of user's profile data"""
        print("\nFirst name: " + self.first_name)
        print("Last name: " + self.last_name)
        print("Age: " + self.age)
        print("Occupation: " + self.job)
        print("Number of login attempts: " + str(self.login_attempts))

    def greet_user(self):
        """A basic function to great the user to the database"""
        print("\nWelcome to the server, " + self.first_name + "!")

    def increment_login_attempts(self, number):
        """A function to increment the # of login attempts for a user"""
        self.login_attempts += number

    def reset_login_attempts(self):
        """A function to reset the login attempts attribute"""
        self.login_attempts = 0


joe = User('joe', 'pickert', 23, 'student')
joe.describe_user()
ben = User('ben', 'imlay', 86, 'master plumber')
ben.describe_user()
ben.greet_user()

joe.increment_login_attempts(3)
joe.describe_user()
joe.reset_login_attempts()
joe.describe_user()


class Restaurant():
    """A basic class that takes name and cuisine information for a restaurant"""

    def __init__(self, name, cuisine):
        """Creates an instance of a restaurant and stores name and cuisine information"""
        self.name = name.title()
        self.cuisine = cuisine.title()
        self.number_served = 0

    def describe_restaurant(self):
        """Prints an orderly summary of restaurant information"""
        print("\nRestaurant name: " + self.name)
        print("Cuisine type: " + self.cuisine)
        print("Number served: " + str(self.number_served))

    def open_restaurant(self):
        """Prints a message to indicate that the restaurant is open for business"""
        print(self.name + " is open for business!")

    def set_number_served(self, number):
        """Adds the additional attribute of # served to an instance"""
        self.number_served = number

    def increment_number_served(self, number):
        """Increments the # served by a specified amount"""
        self.number_served += number


restaurant1 = Restaurant("gino's", "italian")
restaurant2 = Restaurant("pablo's", "mexican")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant1.set_number_served(100)
restaurant1.describe_restaurant()

restaurant2.increment_number_served(200)
restaurant2.describe_restaurant()


# creating a new child class


class IceCreamStand(Restaurant):
    """A child class of the parent Restaurant class"""

    def __init__(self, name, cuisine):
        """
        Initializes attributes of the parent class
        Then initializes attributes of the ice cream stand
        """
        super().__init__(name, cuisine)
        self.options = []

    def add_flavors(self, *flavors):
        """Adds an attribute list of flavors to the ice cream shop"""
        for flavor in flavors:
            self.options.append(flavor)

    def describe_restaurant(self):
        """Overrides the parent function to include flavors"""
        print("\nIce Cream Ship name: " + self.name)
        print("Cuisine type: " + self.cuisine)
        print("Ice cream flavors: ")
        for flavor in self.options:
            print(flavor.title())


icecream = IceCreamStand('Sylas and Maddys', 'ice cream')
icecream.add_flavors('vanilla', 'chocolate', 'cookies and cream', 'strawberry')
icecream.describe_restaurant()


# creating a separate class to hold admin privileges


class Privileges():
    """A simple class to hold the admin-specific capabilities"""
    def __init__(self):
        self.privileges = ['can add post' , 'can delete post', 'can ban user']

    def show_privileges(self):
        """A new function to display admin-specific privileges"""
        print("\nThis user has the additional capabilities: ")
        for value in self.privileges:
            print(value.title())

# creating another child class


class Admin(User):
    """A child class of the parent User class"""

    def __init__(self, first_name, last_name, age, job):
        """
        Initializes attributes of the parent class
        Then initializes attributes of the Admin class
        """
        super().__init__(first_name, last_name, age, job)
        self.privileges = Privileges()


admin1 = Admin('joe', 'pickert', 22, 'student')
admin1.describe_user()
admin1.privileges.show_privileges()


