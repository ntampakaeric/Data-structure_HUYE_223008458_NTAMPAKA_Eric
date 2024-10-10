class CourseManagement:
    def __init__(self):
        self.available_courses = [] 
        self.enrollment_queue = []   
        self.undo_stack = []           

    def add_course(self, course_name):
        """Add a course to the list of available courses."""
        self.available_courses.append(course_name)
        print(f"Course '{course_name}' added.")

    def enroll_student(self, student_name, course_name):
        """Enroll a student in a course if it is available."""
        if course_name in self.available_courses:
            self.enrollment_queue.append((student_name, course_name))
            self.undo_stack.append((student_name, course_name))  
            print(f"Student '{student_name}' enrolled in '{course_name}'.")
        else:
            print(f"Course '{course_name}' is not available.")

    def undo_registration(self):
        """Undo the last course registration."""
        if self.undo_stack:
            student_name, course_name = self.undo_stack.pop()
           
            self.enrollment_queue.remove((student_name, course_name))
            print(f"Registration of student '{student_name}' in '{course_name}' undone.")
        else:
            print("No registrations to undo.")

    def list_courses(self):
        """List all available courses."""
        if self.available_courses:
            print("Available courses:")
            for course in self.available_courses:
                print(f"- {course}")
        else:
            print("No available courses.")

    def list_enrollments(self):
        """List all current enrollments."""
        if self.enrollment_queue:
            print("Current enrollments:")
            for student, course in self.enrollment_queue:
                print(f"- {student} in {course}")
        else:
            print("No current enrollments.")


if __name__ == "__main__":
    cm = CourseManagement()
    
   
    cm.add_course("Mathematics")
    cm.add_course("Physics")
    cm.add_course("Chemistry")
    
    
    cm.list_courses()
    
   
    cm.enroll_student("Alice", "Mathematics")
    cm.enroll_student("Bob", "Physics")
    
    
    cm.list_enrollments()
    
  
    cm.undo_registration()
    
   
    cm.list_enrollments()
