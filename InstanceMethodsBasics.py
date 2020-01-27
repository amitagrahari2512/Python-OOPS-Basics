print("In python their are three types of method - ")
print("1 - Instance Method")
print("2 - Class Methods")
print("3 - Static Methods")

print("Inatance Method : For this we need to use self in method parameter")
print("Instance Method Work on instance method")

print("Method having two types")
print("1-Accessor Methods- Who only access the value") #like Getter
print("2-Mutator Methods - Who can change values") #like Setter

class Student:
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3


s1 = Student(10,20,50)
s2 = Student(100,300,299)

print("s1.avg() : ",s1.avg())
print("s2.avg() : ",s2.avg())

print("\n Accessor Method and Mutator Methods")
print("Setter and getter created in Python")
class StudentNew:
    def set_m1(self,m1): #Mutator Method
        self.m1 = m1

    def get_m1(self): #Accessor Method
        return self.m1

studentNew = StudentNew()
studentNew.set_m1(10)
print("studentNew.get_m1() : ",studentNew.get_m1())


