class node(object):
    def __init__(self,value):
        self.val=value
        self.next=None

class stack(object):
    def __init__(self):
        self.top=None

    def is_empty(self):
        return self.top == None

    def push(self,value):
        new_node=node(value)
        new_node.next=self.top
        self.top=new_node

    def pop(self):
        if self.is_empty():
            print("No Element to pop")
        else:
            print(self.top.val,end="")
            self.top=self.top.next

    def display(self):
        temp=self.top
        print("Stack ",end=": ")
        while(temp != None):
            print(f"{temp.val} -> ",end="")
            temp=temp.next
        print("None")

S=stack()
s=input("Enter String : ")

for i in s:
    S.push(i)

print("Reversed String",end =' : "')
for i in range(len(s)):
    S.pop()
print('"')