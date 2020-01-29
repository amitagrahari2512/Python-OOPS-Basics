print("When we have same method in parenta nd as well child, and when we call this method with child object"
      "it will call child method not parent method"
      "so this is called method overriding in python")

class A:

    def show(self):
        print("Show in A")

class B(A):
    def show(self):
        print("Show in B")

b = B()
b.show()

print("But if we don't have same method in child, then it will go to parent and search for method")

class B1(A):
    pass

b = B1()
b.show()


