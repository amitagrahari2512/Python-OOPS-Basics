print("Polymorphism - Means have many form in different Condition "
      "Its have bascically 4 types"
      "1 - Duck Typing"
      "2 - Operator Overloading"
      "3 - Method Overloading"
      "4 - Method Overriding")

print("Duck Typing - A bird which can run like a duck,"
      "Quack like a duck and"
      "swim like a duk , is a duck"
      "Means A bird who behaves like a duck is a Duck")

print("\n---------------------------")
print("Here we create a Laptop and in that we run IDE")
print("We an run any kind of IDE but it should have execute() method.")

class PyCharm:

      def execute(self):
            print("Compile Python ")
            print("Run Python")


class Eclipse:

      def execute(self):
            print("Compile Java ")
            print("Run Java")

class Laptop:

      def code(self,ide):#here we need to pass object of any class which have execute method
            ide.execute()

print("\n Here we run Pycharm Class Ide")
pycharmIde = PyCharm()
lap = Laptop()
lap.code(pycharmIde)

print("\n Here we run Eclipse Class Ide")
eclipse = Eclipse()
lap = Laptop()
lap.code(eclipse)

