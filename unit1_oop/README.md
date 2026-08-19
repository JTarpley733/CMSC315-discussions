# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

# Unit 1 Discussion - August 18, 2026

## Implementation
This program demonstrates object-oriented programming concepts in Python, including inheritance,
class and instance variables, namespaces, and shallow and deep copying.

### ParentClass
The 'ParentClass' includes:
- A class variable named 'category'
- Instance variables for 'name' and 'age'
- A constructor that initializes the instance variables
- A 'display_info()' method that displays information about the object

### ChildClass
The 'ChildClass' inherits from 'ParentClass' and includes:
- A class variable named 'type'
- Additional instance variables for 'student_id' and 'major'
- A 'change_major()' method
- An overridden 'display_info()' method

The parent constructor is called using 'super()' to initialize the inherited 'name'
and 'age' attributes.

### Namespace Demonstration
The 'demonstrate_namespace()' function demonstrates the difference between class and
inheritance namespaces. Two 'ChildClass' objects are created, and an additional attribute
is added to only one object. The '__dict__' attribute is used to display the separate 
instance namespaces and the class namespace.

### Shallow and Deep Copying
The 'demonstrate_copying()' function demonstrates shallow and deep copying using an object
containing a mutable list of courses.

A shallow copy shares the nested mutable list with the original object. Therefore,
modifying the original list also affects the shallow copy.

A deep copy creates an independent copy of the nested mutable list. Changes to the original
list therefore do not affect the deep copy.

### Main Function
The 'main()' function creates objects from both the parent and child classes and calls their
methods to demonstrate inheritance and method overriding. It also calls the namespace and copying
demonstration functions.