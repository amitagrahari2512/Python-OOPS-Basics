print("In Python Super keyword can be use on constructor,methods and variable,"
      "It can be use in any order in constructor or in method")

class A:
    i = 10
    def __init__(self):
        print("Class A Init")

    def feature1(self):
        print("Class A feature 1")


class B(A):
    i = 20
    def __init__(self):
        print("Class B Init")
        super().__init__()

    def feature2(self):
        super().feature1()
        print("super().i : ",super().i)
        print("Class B feature 2")
        super().__init__()

b = B()
b.feature2()