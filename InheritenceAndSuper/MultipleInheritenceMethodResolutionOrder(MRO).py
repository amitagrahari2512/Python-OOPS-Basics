print("Multiple Inheritence With MRO--------------------------")
print("ClassC(ClassA,ClassB)")
print("MRO - Method Resolution Order - It Will Run Left to Right ")
print("It will find constructor or method of super class from Left to right side"
      "Where it find the data,that's data is shown")
print("Here It find the data first in ClassA and then it will move to ClassB")

print("Multiple Inheritence with MRO-------------------------- \n")

class P:

    def __init__(self):
        print("Init Of P")

    def feature1(self):
        print("Class P feature 1")

    def feature2(self):
        print("Class P feature 2")

class Q():

    def __init__(self):
        print("Init Of Q")

    def feature1(self):
        print("Class Q feature 1")

    def feature2(self):
        print("Class Q feature 2")

class R(P,Q):
    def __init__(self):
        super().__init__() # it will use MRO concept here to find init of super class,Here in left P class, So it will show P class init
        print("Init Of R")

    def feature3(self):
        print("Class R feature 3")

r = R()
print("We have same feature1() and feature2() in P and Q both , So it will use MRO and find methos first in P class"
      "It can find method and print it, If not found then it can check to Q class also")
r.feature1()
r.feature2()
r.feature3()


print("Multiple Inheritence with MRO-------------------------- \n")