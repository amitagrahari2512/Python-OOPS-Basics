print("Python does not support method Overloading,If we want to achieve this in Python ,"
      "we need to do some trick")

class Student:

    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!=None:
            return a+b
        else :
            return a

s1 = Student()
print(s1.sum(9,5))
print(s1.sum(9,9,5))


