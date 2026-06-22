class car:
    type="vehicle"
    count=0

    def __init__(self,company,model):
        self.company=company
        self.model=model
        car.count+=1

    def starts(self):
        return f"Car Starts....."
    
c1=car("Ford","Mustang")
c2=car("Ferrai","SF90")
print(f"car type : {car.type}")
print(f"c1 type : {c1.type}")
print(f"c1 company : {c1.company}")
print(f"c1 model : {c1.model}")
print(f"c1.starts() : {c1.starts()}")
print(f"c2 type : {c2.type}")
print(f"c2 company : {c2.company}")
print(f"c2 model : {c2.model}")
print(f"c2.starts() : {c2.starts()}")
print(f"car count : {car.count}")