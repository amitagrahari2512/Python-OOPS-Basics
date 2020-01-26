print("We can create class in python having use class keyword")
print('when we create any method in class it automatically use self argument in method')
print("This self is act like a object of particular class")
print("We can create a object by using className()")

class Computer:
    def config(self):
        print("Ram : 16Gb, Processor : i5, HDD : 1TB")

comp1 = Computer()

print("Type of class")
print(type(comp1))

print("----------------------------------------------------")
print("Call a method of a class")
print("We can use two way to call a method")
print("1st we can use ClassName.methodName(CurrentClassObject)")

print("Call Config method : ",Computer.config(comp1))
Computer.config(comp1);

print("----------------------------------------------------")
print("2nd We can call directly from classObjectName.methodName()")
print("In this way, on time of run, object automatically passed to methodName(classObjectName) as argument")

comp1.config()




