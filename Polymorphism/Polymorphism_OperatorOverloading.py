a = 6
b = 5
print("a : {}, b : {},  a+b : {} ".format(a,b,a+b))

print("Behind the scene it can use int.__add__(a,b) inbuilt method and it takes both argument as a int")

print("a : {}, b : {},  int.__add__(a,b) : {} ".format(a,b,int.__add__(a,b)))

a = '6'
b = '5'
print("a : {}, b : {},  a+b : {} ".format(a,b,a+b))

print("Behind the scene it can use str.__add__(a,b) inbuilt method and it takes both argument as a string")

print("a : {}, b : {},  str.__add__(a,b) : {}".format(a,b,str.__add__(a,b)))

print("\n")
print("These method which predefined by object class itself , it is called magic methods."
      "like __add__(),__mul__(),__div__() etc"
      "We can overload this methods and define our code here")

print("Wehen we print a=6 , print(a), we will get 6"
      "But when we print any our object it will print object type "
      "but not value"
      "So python has provided one magic method __str__(), we need to change this method,a s we want to"
      "print our result when we call any object")

print("\n")

print("\n We can overload magic method and perform our operation")

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        r1 = self.m1 + other.m1
        r2 = self.m2 + other.m2
        return Student(r1,r2)

    def __sub__(self, other):
        r1 = self.m1 - other.m1
        r2 = self.m2 - other.m2
        return Student(r1,r2)

    def __mul__(self, other):
        r1 = self.m1 * other.m1
        r2 = self.m2 * other.m2
        return Student(r1,r2)

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        return r1>r2

    def __str__(self):
        return "m1 : {} , m2 : {}".format(self.m1,self.m2)

s1 = Student(50,100)
s2 = Student(40,70)

print("s1+s2 : ",s1+s2)
print("s1-s2 : ",s1-s2)
print("s1*s2 : ",s1*s2)
print("s1>s2 : ",s1>s2)

print("We overload __str__() method to show our output when call our object name")
print(s1)
print(s2)

