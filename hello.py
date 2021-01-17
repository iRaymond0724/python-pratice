class Parent:
    def myMethod(self):
        print("father Method")

class Child(Parent):
    def myMethod(self):
        print("child Method")

c = Child()
c.myMethod()