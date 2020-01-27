print("We can use same name as instance variable and class variable , but we need not to use it"
      "because it is confusing")
print("We can call class method and static method with object also.")
print("Here we use school as as Instance Variable as well as Class Variable")
class Student:
    school = "IndianSchool"

    def __init__(self,m1,m2,m3,school):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.school = school

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def schoolName(cls):
        return cls.school

    @staticmethod
    def schoolInfo():
        print("This is a static method.Here we not work on instance variable or class variable")

s1 = Student(10,20,30,"A")
s2 = Student(100,200,300,"B")
print(s1.avg())

print("We can use same name as instance variable and class variable , but we need not to use it"
      "because it is confusing")
print("We can call class method and static method with object also.")

print("Student.schoolName()",Student.schoolName())
print("s1.schoolName() : {} , s1.school : {}, ".format(s1.schoolName(),s1.school))
print("s2.schoolName() : {} , s2.school : {}, ".format(s2.schoolName(),s2.school))
Student.schoolInfo()
s1.schoolInfo()
s2.schoolInfo()
