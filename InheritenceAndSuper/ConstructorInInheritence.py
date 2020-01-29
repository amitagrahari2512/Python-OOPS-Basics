print("When we create any SubClassObject , Python first check for SubClass __init__ method,"
      "If it is present then it will call SubClass __init__ method"
      "If it is not present in sub class then it will go to check and call super class __init__ method"
      "If super class don't have this method then no issue")

print("If we have init in Super and Sub class both , and We want to print both init method"
      "then We need to use super().__init__ to call super class methods")

class A:
    def __init__(self):
        print("init Of A - Super class")

    def feature1(self):
        print("Class A Feature 1")

class B(A):
    def feature2(self):
        print("Class B Feature 2")

b = B()
print("Here it find init in super class")

print("\n-------------------------------")
class P:
    def __init__(self):
        print("init Of P - Super class")

    def feature1(self):
        print("Class P Feature 1")

class Q(P):
    def __init__(self):
        print("init Of Q - Sub class")

    def feature2(self):
        print("Class Q Feature 2")

q = Q()
print("Here it find init in sub class")
print("\n-------------------------------")

print("\n---Super----------------------------")
class R:
    def __init__(self):
        print("init Of R - Super class")

    def feature1(self):
        print("Class R Feature 1")

class S(R):
    def __init__(self):
        super().__init__()
        print("init Of S - Sub class")

    def feature2(self):
        print("Class S Feature 2")

s = S()
print("Here it find init in sub class")
print("\n-----Super--------------------------")



