print("Variable has two types:")
print("1 - Instance Variables - It will change for object to object")
print("2 - Class Variables or Static Variables - It will same for all the object,If we change this variable,"
      "same change reflect to other object also")

print("Python : we have two types of namespace:")
print("1 : Instance Namespace - Where we store instance Object memory")
print("2 : Class Namespace - Where we store Class variable or Static Variable Object memory")


print("\n------------------------------------------------")

print("If we create any variable inside __init__ method, it act as a instance variable and we can "
      "call that variable from object")

print("We can create any variable outside __init__ method but inside class is act as a Class Variable or Static Variable")

print("--------------------------------------------------\n")

class Car:
    wheels = 4

    def __init__(self):
        self.mileage = 10
        self.company = "TATA"


c1 = Car()
c2 = Car()
c1.mileage = 120

print("c1.mileage : {} , c1.company : {} , wheels : {}".format(c1.mileage,c1.company,c1.wheels))
print("c2.mileage : {} , c2.company : {} , wheels : {}".format(c2.mileage,c2.company,c2.wheels))

print("\n------------------------------------------------")

print("If we change wheels variable with using Class Name, It will reflect both object automatically,because it is a static variable")

Car.wheels = 5
print("c1.mileage : {} , c1.company : {} , wheels : {}".format(c1.mileage,c1.company,c1.wheels))
print("c2.mileage : {} , c2.company : {} , wheels : {}".format(c2.mileage,c2.company,c2.wheels))

print("------------------------------------------------\n")

print("Class Variable can use with object name as well as class name also.")
print("Car.wheels : {} , c1.wheels : {}".format(Car.wheels,c1.wheels))

print("\n------------------------------------------------")



