print("Python have speacial method called __init__(self), "
      "this method will automatically run when we create object,it act as a constructor"
      "If we not use in our code but it will definatedly run by the compiler")

print("This act like a constructor")

print("If we want to set variables , we can use this method and pass the variable in this methoad after self")

class Computer:
    def __init__(self,r,pro,hd):
        print("Init Method")
        self.ram = r
        self.processor = pro
        self.hdd = hd


    def config(self):
        print("Ram : ",self.ram)
        print("Processor : ",self.processor)
        print("HDD : ",self.hdd)

comp1 = Computer("16GB","I5","1Tb")
comp2 = Computer("8GB","I3","500GB")

print("comp1 property")
comp1.config()

print("------------------------------------------------------")

print("comp2 property")
comp2.config()

