"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy

# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    # Creates class Variable
    category = "General"

    # The Constructor
    def __init__(self, name, age):
        # The instance variables
        self.name = name
        self.age = age

    # Creates the Method that displays information about the object(s)
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Category: {self.category}")



# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    # Creates new class variable
    type = "Student"

    # The Constructor
    def __init__(self, name, age, student_id, major):
        # Calls the parent constructor
        super().__init__(name, age)

        # Creates new instance variables
        self.student_id = student_id
        self.major = major

    # Creates new method
    def change_major(self, new_major):
        self.major = new_major

    # To override parent method
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, "f"ID: {self.student_id}, "
              f"Major: {self.major}, " f"Type: {self.type}")




# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    # Creates the two objects of the child class
    child1 = ChildClass("Jessica", 42, "S1001", "Computer Science")
    child2 = ChildClass("Andrew", 45, "S1002", "Psychology")

    # Creates access to class variable through the class
    print("Class variable through class:")
    print(ChildClass.type)

    # Creates access to the same class variable through an object
    print("\nClass variable through object")
    print(child1.type)

    # Adds new attribute to only one object (child1)
    child1.status = "Active"

    print("\n=== Namespace Demonstration ===")

    # Displays each object's instance namespace
    print("\nChild 1 namespace:")
    print(child1.__dict__)
    print("\nChild 2 namespace:")
    print(child2.__dict__)

    # Displays information about the class namespace
    print("\nChildClass namespace:")
    print(ChildClass.__dict__)

    print("TODO: Implement namespace demonstration")



# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    print("TODO: Implement shallow copy and deep copy demonstration")

    # Creates an object with nested mutable data
    original = ChildClass("Jessica", 42, "S1001", "Computer Science")
    original.courses = ["Python", "Java"]

    # A shallow copy creates a new object, but nested mutable objects such as
    # the courses list are still shared with the original
    shallow_copy = copy(original)

    # A deep copy creates a new object and also creates independent copies of nested
    # mutable objects.
    deep_copy = deepcopy(original)

    # Modifies the nested list in the original object
    original.courses.append("SQL")

    # Displays each object's namespace
    print("\nOriginal object:")
    print(original.__dict__)

    print("\nShallow copy:")
    print(shallow_copy.__dict__)

    print("\nDeep copy:")
    print(deep_copy.__dict__)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    # Creates an object from the parent class
    parent = ParentClass("Jessica", 42)

    # Creates an object from the child class
    child = ChildClass("Andrew", 45, "S9637", "Biology")

    print("\nTODO: Create and test your parent object")
    # Creates and demonstrates parent method
    print("Parent object:")
    parent.display_info()

    print("\nTODO: Create and test your child object")

    # Creates and demonstrates child method
    print("\nChild object:")
    child.display_info()

    # Demonstrates a method specific to the child Class
    child.change_major("Psychology")
    print("\nChild object after changing major:")
    child.display_info()

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()