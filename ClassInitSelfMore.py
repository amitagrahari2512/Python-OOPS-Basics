print("When we create object, Object memory is creating in a heap area")
print("Python does not provide compare method")
print("If we create any variable inside __init__ method, it act as a instance variable and we can "
      "call that variable from object")

class Human:
    def __init__(self):
        self.name = "Amit"
        self.age = 29

    def update(self):
        self.age = 28

    def compare(self,otherObj):
        if self.age == otherObj.age:
            return True
        else:
            return False

h1 = Human()
h2 = Human()

print("id(h1) : ",id(h1))
print("id(h2) : ",id(h2))

print("h1.name: {0} , h1.age : {1}".format(h1.name,h1.age))
print("h2.name: {0} , h2.age : {1}".format(h2.name,h2.age))

print("I want to change name of object h1 , and age of object h2")
h1.name = "Vinay"
h2.age = 30

print("After changing values")

print("h1.name: {0} , h1.age : {1}".format(h1.name,h1.age))
print("h2.name: {0} , h2.age : {1}".format(h2.name,h2.age))

print("We can value from creating own method also,here we create update method for change age")

h1.update()
h2.update()

print("h1.name: {0} , h1.age : {1}".format(h1.name,h1.age))
print("h2.name: {0} , h2.age : {1}".format(h2.name,h2.age))

print("Here we create compare method to compare age for both object")
print("we create method compare(self.otherObj), so which object we called compare() self = that object. "
      "and pass other object in method is act as a diff object")
h2.age = 40 #Here I change age of h2 obj.
if h1.compare(h2):
    print("Age is same")
else:
    print("Age is different")
