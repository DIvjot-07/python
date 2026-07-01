import ctypes
class Makemylist:
    def __init__(self):
        self.size=1
        self.n=0
        self.A=self.__make_array(self.size)

    def __make_array(self,capacity):
        return (capacity*ctypes.py_object)()
    
    def __len__(self):
        return self.n
    
    def append(self,item):
        if self.n == self.size:
            self._resize(self.size*2)
        self.A[self.n]=item
        self.n += 1

    def _resize(self,capacity):
        B=self.__make_array(capacity)
        self.size=capacity 
        for i in range(self.n):
            B[i]=self.A[i]
        self.A=B

    def _print(self):
        print("Array : [",end="")
        for i in range(self.n):
            print(self.A[i] ,end="")
            for j in range(self.n-1):   
                if j==i:
                    print(",",end="")
        print("]")
        
    def __getitem__(self,index):
        if (0 <= index and index < self.n):
            return self.A[index]
        elif(index < 0 and index >= -(self.n) ):
            return self.A[index+self.n]
        else:
            print("Index Out Of Range")
    
    def pop(self):
        if(self.n==0):
            print("Empty List")
        else:
            print(f"Popped Element is {self.A[self.n-1]}")
            self.n=self.n-1

    def clear(self):
        self.size=1
        self.n=0

    def find(self,element):
        count=0
        for i in range(self.n):
            if(str(self.A[i])==element):
                print(f"Found at index {i}")
                count+=1
                return i
        if(count==0):
            print("Element Not Found")

    def insert(self,index,element):
        if(0 > index or index > self.n):
            print("Index Out Of List")
        else:
            if self.n == self.size:
                self._resize(self.size*2)
            for i in range(self.n,index,-1):
                self.A[i]=self.A[i-1]
            self.A[index]=element
            self.n += 1

    def delete(self,index):
        if(0 > index or index >= self.n):
            print("Index Out Of List")
        else:
            for i in range(index,self.n-1):
                self.A[i]=self.A[i+1]
            self.n-=1
    
    def remove(self,value):
        pos=self.find(value)
        if(type(pos)==int):
            self.delete(pos)
        else:
            print("Element Not Found")
    
    def extend(self):
        num=int(input("Enter Number of Element in new List:"))
        B=Makemylist()
        for i in range(num):
            print("\nElement 1")
            val=inputvalue()
            B.append(val)
            self.append(B[i])
        print("New ",end="")
        B._print()

    def min(self):
        i=0
        while(i<self.n):
            if(type(self.A[i]) != str):
                val=self.A[i]
                break
            i+=1

        for i in range(1,self.n):
            if(type(self.A[i]) != str):
                if(self.A[i] < val):
                    val=self.A[i]
        return val

    def max(self):
        i=0
        while(i<self.n):
            if(type(self.A[i]) != str):
                val=self.A[i]
                break
            i+=1
            
        for i in range(1,self.n):
            if(type(self.A[i])!= str):
                if(self.A[i] > val):
                    val=self.A[i]
        return val

    def sum(self):
        val=0
        for i in range(0,self.n):
            if(type(self.A[i]) != str):
                val += self.A[i]
        return val
    
    def slicing(self, start, end, step):
        if step == 0:
            print("Step Cannot Be Zero")
            return
        if -self.n <= start <= self.n and -self.n <= end <= self.n:
            B = Makemylist()
            for i in range(start, end, step):
                B.append(self[i])
            print("Sliced ", end="")
            B._print()
        else:
            print("Index Out Of List")
    
    def BubbleSort(self):
        for i in range(0,self.n-1):
            for j in range(0,self.n-i-1):
                if(self.A[j] > self.A[j+1]):
                    temp=self.A[j]
                    self.A[j]=self.A[j+1]
                    self.A[j+1]=temp
        
L=Makemylist()

def inputvalue():
    val=int(input("1. Int Input \n2. Float Input \n3. String Input \nEnter Input Choice : "))
    if(val==1):
        value=int(input("Enter Element : "))
        return value
    elif(val==2):
        value=float(input("Enter Element : "))
        return value
    elif(val==3):
        value=input("Enter Element : ")
        return value
    else:
        print("Wrong Input Choice")
        value = inputvalue()
        return value 


print("****** Main Menu ******")
print("1. Length Of array \n2. Append Element \n3. Print Array \n4. Size Of Array \n5. Pop Element \n6. Insert Element \n7. Delete Element \n8. Remove Element \n9. Find Element \n10. Clear Array \n11. Get Element at index \n12. Min Value in Array \n13. Max Value in Array \n14. Sum of numerical values in Array \n15. Sliced Array \n16. Extend \n17. Buubble Sort \n18. Exit" )

while(True):
    c=int(input("\nEnter Choice : "))
    if(c==1):
        print(f"Length of Array : {L.__len__()}")
    elif(c==2):
        element=inputvalue()
        L.append(element)
        L._print()
    elif(c==3):
        L._print()
    elif(c==4):
        print(f"Size of Array : {L.size}")
    elif(c==5):
        L.pop()
        L._print()
    elif(c==6):
        element=inputvalue()
        index=int(input("Enter Index : "))
        L.insert(index,element)
        L._print()
    elif(c==7):
        index=int(input("Enter Index : "))
        L.delete(index)
        L._print()
    elif(c==8):
        element=inputvalue()
        L.remove(element)
        L._print()
    elif(c==9):
        element=input("Enter Element")
        L.find(element)
    elif(c==10):
        L.clear()
        L._print()
    elif(c==11):
        index=int(input("Enter Index : "))
        print(f"L[{index}] : {L[index]}")
    elif(c==12):
        print(f"Minimum value in Array : {L.min()}")
    elif(c==13):
        print(f"Minimum value in Array : {L.max()}")
    elif(c==14):
        print(f"Sum of Numerical value in Array : {L.sum()}")
    elif(c==15):
        start=int(input("Enter Start : "))
        end=int(input("Enter end : "))
        step=int(input("Enter step : "))
        L.slicing(start,end,step)
    elif(c==16):
        L.extend()
        L._print()
    elif(c==17):
        L.BubbleSort()
        L._print()
    elif(c==18):
        break
    else:
        print("Wrong Choice")