print("Inner class is class within class")

print("We can create object of inner class inside the outer class")
print("Or")
print("We can create object of inner class outside the outer class"
      "provided you use outer class name to call it")

class Student:
    def __init__(self,name,rollNo):
        self.name = name
        self.rollNo = rollNo
        self.lap = self.Laptop()

    def show(self):
        print("name : {} , rollNo : {} ".format(self.name , self.rollNo))
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.name = "HP"
            self.ram = "8GB"
            self.hdd = "500GB"

        def show(self):
            print("Laptop : name : {} , ram : {} , hdd : {}".format(self.name,self.ram,self.hdd))


s1 = Student("Amit",12)
s2 = Student("Kishan",24)
s1.show()
s2.show()

print("\n--------------------------------------------------")
print("We can call Inner class directly from Outer Class object")
lap = Student.Laptop()
lap.show()
print("----------------------------------------------------\n")


