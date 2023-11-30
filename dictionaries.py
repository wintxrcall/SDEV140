# Renee Guldi
# 11/29/2023
"""
Course Management System:

This script provides a simple course management system implemented in Python.
It allows for the addition, removal, and checking of courses in a dictionary-based data structure.
"""
## Needed for type hints
from typing import Dict

# Reminder: you may remove the "pass" statements from the functions below once you implement them


def display_course_names(course_info: Dict[str, str]) -> None:
    """Display the names of all available courses."""
    print("\nAvailable Courses:")
    # TODO: Iterate through the course_info dictionary and print the course code and name for each course
    # use length to check that the course_info dictionary is not empty
    if len(course_info) == 0:
        print("No courses found...")
    # if the dictionary has variables, print them 
    else:
        print(course_info)
    
    


def add_course(course_info: Dict[str, str]) -> None:
    """Add a new course to the course_info dictionary."""
    # TODO: Prompt the user for a course code and name, then add the course to the course_info dictionary
    # The course code should be converted to uppercase before being added to the dictionary
    
    # prompt user for course code
    NewCourse_Code = input("Please enter your new course code: ")
    # use the upper function to capitalize user input and reassign the variable to itself
    NewCourse_Code = NewCourse_Code.upper()
    # prompt user for course name
    NewCourse_Name = input ("Please enter course name: ")
    # use the capitalize function to capitalize the first letter of course name input to reassign the variable to itself
    NewCourse_Name = NewCourse_Name.capitalize()

    # add information to our dictionary
    course_info[NewCourse_Code] = NewCourse_Name

    # f string to print course code and name for confirmation of addition to dictionary
    print(f"{NewCourse_Code} : {course_info[NewCourse_Code]} has been added to the course list!")



def remove_course(course_info: Dict[str, str]) -> None:
    """Remove an existing course from the course_info dictionary."""
    # TODO: Prompt the user for a course code to remove, then remove the course from the course_info dictionary
    # Python dictionary keys are case-sensitive, so the course code should be converted to uppercase before being removed
    # You must also make sure the course code exists in the dictionary before attempting to remove it.
    
    # prompt user to for course code to reference in course_info dict
    CourseRemove = input("Please enter the course code you would like to remove: ")
    # convert variable into all uppercase
    CourseRemove = CourseRemove.upper()
    # if statement to check for course code in course_info dict
    if CourseRemove in course_info:
    # .pop() method to remove specific variable and its attribute from dict
        course_info.pop(CourseRemove)
    # else statement if course is not found within database
    else:
        print("Course not found...")
        


def check_course_existence(course_info: Dict[str, str]) -> None:
    """Check if a course exists in the course_info dictionary."""
    # TODO: Prompt the user for a course code to check, then check if the course exists in the course_info dictionary
    # Again, the course code should be converted to uppercase before being checked

    # Prompt user for input:
    CourseCheck = input("Please enter course code to reference: ")
    # alter the variable to all caps
    CourseCheck = CourseCheck.upper()
    # reference dictionary for course code:
    if CourseCheck in course_info:
        # function string printed to include variable
        print(f"Found {CourseCheck}!")
    else:
        # Not found message if course not already added.
        print("Not Found...")



def main() -> None:
    """Main program loop."""

    # TODO: Initialize an empty dictionary to store course information
    course_info = {}

    while True:
        print("\nCourse Management System")
        print("1. Display Course Names")
        print("2. Add New Course")
        print("3. Remove Course")
        print("4. Check Course Existence")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        # TODO: Pass the course_info dictionary to the appropriate function based on the user's choice
        if choice == '1':
            display_course_names(course_info)
        
        elif choice == '2':
            add_course(course_info)
            
        elif choice == '3':
            remove_course(course_info)
            
        elif choice == '4':
            check_course_existence(course_info)
            
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == '__main__':
    main()
