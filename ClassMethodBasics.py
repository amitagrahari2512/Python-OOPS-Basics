print("For class method we need to use cls in method parameter")
print("For class method we need to use @classmethod in method,otherwise we will get error.")
print("Class Method works on class variable")
print("We can call Class method with object also.")

class Student:
    school="IndianSchool"

    @classmethod
    def schoolName(cls):
        return cls.school

print("Student.schoolName() : ", Student.schoolName())

print("Change school Name : ")
Student.school = "Indian School Upgrade"
print("Student.schoolName() : ", Student.schoolName())


print("---------------------------")
print("We can call Class method with object also.")
s =Student()
print("s.schoolName()",s.schoolName())