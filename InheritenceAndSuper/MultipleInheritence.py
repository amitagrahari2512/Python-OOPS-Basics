print("Multiple Inheritence --------------------------")

class A:
    def feature1(self):
        print("Class A feature 1")

    def feature2(self):
        print("Class A feature 2")

class B():
    def feature3(self):
        print("Class B feature 3")

    def feature4(self):
        print("Class B feature 4")

class C(A,B):
    def feature5(self):
        print("Class C feature 5")

c = C()
print("Multiple Inheritence : c.feature1", end=" : ")
c.feature1()
print("Multiple Inheritence : c.feature2", end=" : ")
c.feature2()
print("Multiple Inheritence : c.feature3", end=" : ")
c.feature3()
print("Multiple Inheritence : c.feature4", end=" : ")
c.feature4()
print("Multiple Inheritence : c.feature5", end=" : ")
c.feature5()


print("Multiple Inheritence with same method-------------------------- \n")

class P:
    def feature1(self):
        print("Class P feature 1")

    def feature2(self):
        print("Class P feature 2")

class Q():
    def feature1(self):
        print("Class Q feature 1")

    def feature2(self):
        print("Class Q feature 2")

class R(P,Q):
    def feature3(self):
        print("Class R feature 3")

r = R()
r.feature1()
r.feature2()
r.feature3()


print("Multiple Inheritence with same method-------------------------- \n")