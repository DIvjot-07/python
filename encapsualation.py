class car:
    def __init__(self,age):
        self.name="mercedes"
        self._model="AMG"
        self.__serial="One"
        self.__age=age
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,val):
        if(val<0):
            raise ValueError("Age Can't Be Negative")
        self.__age=val

c=car(10)
print(f"Name : {c.name}")
print(f"model : {c._model}")
print(f"serial : {c._car__serial}")
print(f"Age : {c._car__age}")
c.age=6
print(f"Age : {c._car__age}")

