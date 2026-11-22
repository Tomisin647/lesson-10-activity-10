# Class Student - 2 (complete activity 2, DSCM2L3). Python 3 standard library only.
# Run: python class_student_2.py  (or paste into one Google Colab cell and press Run)


class Student:
    school = "Sunrise School"                                  # A: class variable

    def introduction(self):
        """A method: a function inside the class. self is the object it is called on."""
        # Step 1: First method
        return "Hi, I am a student at " + self.school

    def details(self):
        # Step 2: Method that reads the object's own data
        return f"My name is {self.name} and I study in grade {self.grade}."


anna = Student()                                               # B: one object
anna.name = input("Student name? ")                                             # C: data stored on
anna.grade = int(input("Grade? "))                                                #    this object only
print(anna.introduction())
print(anna.details())
print(Student.details(anna))   # D: the same call written out; self is anna

# Step 3: Same methods, another object
ryan = Student()
ryan.name = "Ryan"
ryan.grade = 9
print(ryan.details())
