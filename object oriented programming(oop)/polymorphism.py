class cat:
    def sound(self):
        print("Meow")
class dog:
    def sound(self):
        print("Bark")
for i in [cat(), dog()]:
    i.sound()#same method name but different classes, this is called polymorphism
#output: Meow 
# output: Bark