print("Static Method - When we don't want to work on Instance variable and "
      "Class Variable we need to use Static Method")
print("So in this time we not pass either self or cls")
print("We need to use @staticmethod in method")
print("We can call Static method with object also.")

class Student:

    @staticmethod
    def schoolInfo():
        print("This is a static method.Here we not work on instance variable or class variable")


Student.schoolInfo()

print("---------------------------")
print("We can call Static method with object also.")
s =Student()
s.schoolInfo()