print("Python supports 3 types of inheritence")
print("1 - Single Level Inheritence")
print("2 - MultiLevel Inheritence")
print("3 = Multiple Inheritence")

print("We can use SubClasssName(ParentClassName) for inheritence")

print("\nSingle Level Inheritence -------------------------B inherit A")
class A:
    def feature1(self):
        print("Class A feature 1")

    def feature2(self):
        print("Class A feature 2")

class B(A):
    def feature3(self):
        print("Class B feature 3")

    def feature4(self):
        print("Class B feature 4")

b = B()

print("SigleLevel Inheritence : b.feature1", end=" : ")
b.feature1()
print("SigleLevel Inheritence : b.feature2", end=" : ")
b.feature2()
print("SigleLevel Inheritence : b.feature3", end=" : ")
b.feature3()
print("SigleLevel Inheritence : b.feature4", end=" : ")
b.feature4()

print("Single Level Inheritence -------------------------\n")

print("Multilevel Inheritence , C inherit B , B inherit A")

class C(B):
    def feature5(self):
        print("Class C feature 5")

c = C()
print("Multilevel Inheritence : c.feature1", end=" : ")
c.feature1()
print("Multilevel Inheritence : c.feature2", end=" : ")
c.feature2()
print("Multilevel Inheritence : c.feature3", end=" : ")
c.feature3()
print("Multilevel Inheritence : c.feature4", end=" : ")
c.feature4()
print("Multilevel Inheritence : c.feature5", end=" : ")
c.feature5()

print("MultiLevel Inheritence ---------------- \n")

