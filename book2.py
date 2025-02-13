import pickle
from typing import List

class User:
    def __init__(self):
        self.user = ""
        self.passwd = ""

class Student:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name

class Course:
    def __init__(self, course_name, course_id, max_students, current_students, instructor_name, course_section, course_location):
        self.course_name = course_name
        self.course_id = course_id
        self.max_students = max_students
        self.current_students = current_students
        self.instructor_name = instructor_name
        self.course_section = course_section
        self.course_location = course_location
        self.student_list = []
    
    def print_course(self):
        print(f"Course Name: {self.course_name}, ID: {self.course_id}, Instructor: {self.instructor_name}, Location: {self.course_location}, Students: {self.current_students}/{self.max_students}")

    def set_instructor_name(self, name):
        self.instructor_name = name

    def set_course_location(self, location):
        self.course_location = location
    
    def get_course_name(self):
        return self.course_name
    
    def get_course_id(self):
        return self.course_id
    
    def get_current_students(self):
        return self.current_students
    
    def get_max_students(self):
        return self.max_students
    
    def get_student_list(self):
        return self.student_list

class Admin(User):
    master_registry: List[Student] = []
    course_list: List[Course] = []
    
    def __init__(self):
        super().__init__()
        self.user = "admin"
        self.passwd = "admin001"
    
    def create_course(self):
        course_name = input("Enter the course name: ")
        course_id = input("Enter the course ID: ")
        max_students = int(input("Enter max number of students: "))
        current_students = int(input("Enter current number of students: "))
        instructor_name = input("Enter instructor's name: ")
        course_section = int(input("Enter course section: "))
        course_location = input("Enter course location: ")
        
        new_course = Course(course_name, course_id, max_students, current_students, instructor_name, course_section, course_location)
        self.course_list.append(new_course)
        print(f"Course {course_name} has been successfully added!")
    
    def delete_course(self):
        course_name = input("Enter the course name to delete: ")
        for course in self.course_list:
            if course.get_course_name() == course_name:
                self.course_list.remove(course)
                print(f"The course {course_name} has been successfully removed!")
                return
        print("Oops! Course not found.")
    
    def edit_course(self):
        option = input("Enter '1' to change instructor or '2' to change location: ")
        course_name = input("Enter the course name: ")
        
        for course in self.course_list:
            if course.get_course_name() == course_name:
                if option == "1":
                    new_instructor = input("Enter new instructor name: ")
                    course.set_instructor_name(new_instructor)
                    print("Instructor updated successfully.")
                elif option == "2":
                    new_location = input("Enter new location: ")
                    course.set_course_location(new_location)
                    print("Location updated successfully.")
                return
        print("Course not found.")
    
    def display_a_course(self):
        course_id = input("Enter course ID: ")
        for course in self.course_list:
            if course.get_course_id() == course_id:
                course.print_course()
                return
        print("Course not found.")
    
    def register_student(self):
        first_name = input("Enter student's first name: ")
        last_name = input("Enter student's last name: ")
        new_student = Student(first_name, last_name)
        self.master_registry.append(new_student)
        print("Student successfully registered!")
    
    def admin_view_all_courses(self):
        for course in self.course_list:
            course.print_course()
    
    def view_full_courses(self):
        full_courses = [course for course in self.course_list if course.get_current_students() == course.get_max_students()]
        for course in full_courses:
            course.print_course()
        return full_courses
    
    def view_registered_students(self):
        course_name = input("Enter course name: ")
        for course in self.course_list:
            if course.get_course_name() == course_name:
                print("Registered Students:")
                for student in course.get_student_list():
                    print(f"* {student.get_first_name()} {student.get_last_name()}")
                return
        print("Course not found.")
    
    def view_all_student_courses(self):
        first_name = input("Enter student's first name: ")
        last_name = input("Enter student's last name: ")
        
        print(f"Courses for {first_name} {last_name}:")
        for course in self.course_list:
            for student in course.get_student_list():
                if student.get_first_name() == first_name and student.get_last_name() == last_name:
                    print(f"* {course.get_course_name()}")
                    break
    
    def sort_courses(self):
        self.course_list.sort(key=lambda course: course.get_current_students())
        print("Courses sorted by number of registered students.")
        self.admin_view_all_courses()
    
    def write_to_file_full_courses(self):
        file_name = "full_courses.txt"
        with open(file_name, "w") as file:
            for course in self.view_full_courses():
                file.write(f"{course.get_course_name()}\n")
        print(f"Full courses written to {file_name}.")