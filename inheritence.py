class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speaks(self):
        return f"{self.name} makes a sound"
    def IsAnimal(self):
        return True
    
class Cat(Animal):
    def speaks(self):
        return f"{self.name} meeeeoows"
    
class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.breed=breed
    def speaks(self):
        return f"{self.name} barks"
    
c=Cat("Max",4)
d=Dog("Charles",6,"Labra")
b=Animal("Carlos",2)

print(f"c speaks : {c.speaks}")
print(f"c name : {c.name}")
print(f"c age : {c.age}")
print(f"c.IsAnimal() : {c.IsAnimal()}")

print(f"d speaks : {d.speaks}")
print(f"d name : {d.name}")
print(f"d age : {d.age}")
print(f"d.IsAnimal() : {d.IsAnimal()}")
print(f"d breed : {d.breed}")

print(f"b speaks : {b.speaks}")
print(f"b name : {b.name}")
print(f"b age : {b.age}")
print(f"b.IsAnimal() : {b.IsAnimal()}")