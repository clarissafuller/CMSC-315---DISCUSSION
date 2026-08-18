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

class ParentClass:
    """Represents a general Person with a name and age."""

    species = "Homo sapiens"  # class variable, shared by all instances

    def __init__(self, name: str, age: int):
        self.name = name        # instance variable
        self.age = age          # instance variable

    def display_info(self):
        """Display the person's basic information."""
        print(f"Name: {self.name}, Age: {self.age}, Species: {ParentClass.species}")


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.

class ChildClass(ParentClass):
    """Represents a Student, inheriting from ParentClass (Person)."""

    school_name = "Generic University"  # new class variable

    def __init__(self, name: str, age: int, student_id, courses=None):
        super().__init__(name, age)          # call parent constructor
        self.student_id = student_id          # new instance variable
        self.courses = courses if courses is not None else []  # new instance variable (mutable list)

    def enroll_course(self, course_name: str):
        """New method: adds a course to the student's course list."""
        self.courses.append(course_name)

    def is_enrolled_in(self, course_name: str) -> bool:
        """New method: checks if student is enrolled in a given course."""
        return course_name in self.courses

    def display_info(self):
        """Override parent method to include student-specific details."""
        courses_str = f"[{', '.join(self.courses)}]" if self.courses else "[]"
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}, "
              f"School: {ChildClass.school_name}, Courses: {courses_str}")


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    # Create two child class objects
    student1 = ChildClass('Maya', 23, 'S5555')
    student2 = ChildClass('Owen', 20, 'S6789')

    # Access class variable through the class itself
    print("Accessing via class:", ChildClass.school_name)

    # Access the same class variable through an object
    print("Accessing via instance (student1):", student1.school_name)

    # Add a new attribute to only ONE object after creation
    student1.favorite_subject = "Biology"

    # Display each object's namespace using __dict__
    print("\nstudent1.__dict__:", student1.__dict__)
    print("student2.__dict__:", student2.__dict__)
    # Notice: only student1 has 'favorite_subject' — instance namespaces
    # are independent, so adding an attribute to one object does not
    # affect the other.

    # Display class namespace
    print("\nChildClass.__dict__ (partial view of class namespace):")
    for key, value in ChildClass.__dict__.items():
        if not key.startswith('__'):
            print(f"  {key}: {value}")
    # Notice: 'school_name' lives in the CLASS namespace, not in either
    # instance's __dict__, which is why it doesn't show up above for
    # student1 or student2 individually — it's looked up on the class
    # when not found on the instance.


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    # Create an object with nested mutable data (the courses list)
    original = ChildClass('Dana', 22, 'S9876', courses=['Biology', 'Chemistry'])

    # Create a shallow copy and a deep copy
    shallow = copy(original)
    deep = deepcopy(original)

    # Modify the original object's nested data
    original.courses.append('Physics')

    print("Original:", original.courses)
    print("Shallow copy:", shallow.courses)
    print("Deep copy:", deep.courses)

    # EXPLANATION:
    # - shallow copy: copy() duplicates the ChildClass object itself,
    #   but its 'courses' attribute still POINTS TO THE SAME LIST as
    #   the original. So modifying original.courses also changes
    #   shallow.courses — they share the same underlying list in memory.
    # - deep copy: deepcopy() recursively copies every nested object,
    #   including the 'courses' list itself, creating a completely
    #   independent copy. Modifying original.courses has no effect
    #   on deep.courses.


# TODO 5:
# Complete the main function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    # Create and test a parent object
    person = ParentClass('Cleo', 45)
    person.display_info()

    # Create and test a child object
    student = ChildClass('Ben', 20, 'S1234')
    student.enroll_course('Math 101')
    student.enroll_course('History 202')
    student.display_info()
    print("Enrolled in Math 101?", student.is_enrolled_in('Math 101'))
    print("Enrolled in Art?", student.is_enrolled_in('Art'))

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()