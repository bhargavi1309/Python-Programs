class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    pass
d=Dog()
d.sound()#dog inherits sound() method from Animal class
#output: Animal makes sound
