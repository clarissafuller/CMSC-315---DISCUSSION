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

## Implementation Summary

I implemented a `ParentClass` representing a general Person, with `name` and `age` as instance variables and `species` as a shared class variable. I added a constructor and a `display_info()` method that printed the object's details.

I created a `ChildClass` that inherited from `ParentClass` to represent a Student. I added `school_name` as a new class variable, and `student_id` and a mutable `courses` list as new instance variables. I called `super().__init__()` in the constructor to reuse the parent's initialization logic. I added two new methods, `enroll_course()` and `is_enrolled_in()`, and I overrode `display_info()` to include the student-specific fields.

For the namespace demonstration, I created two `ChildClass` objects and added a new attribute, `favorite_subject`, to only one of them. I displayed each object's `__dict__` to show that instance namespaces were independent, and I displayed the class namespace to show that `school_name` and the methods lived on the class rather than on either instance.

For the copying demonstration, I created a `ChildClass` object with a nested mutable `courses` list, then created a shallow copy using `copy.copy()` and a deep copy using `copy.deepcopy()`. I modified the original object's `courses` list and printed all three versions. The shallow copy reflected the change because it shared the same underlying list as the original, while the deep copy remained unchanged because it held a fully independent list.

I completed `main()` by creating and testing one `ParentClass` object and one `ChildClass` object, calling both demonstration functions, and verifying the printed output matched the expected behavior for inheritance, namespaces, and copying.