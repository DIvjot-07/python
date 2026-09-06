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
        self.display()

    def peek(self):
        print(f"Peek of the Stack is {self.top.val}")

    def pop(self):
        if self.is_empty():
            print("No Element to pop")
        else:
            self.top=self.top.next
            self.display()

    def display(self):
        temp=self.top
        print("Stack ",end=": ")
        while(temp != None):
            print(f"{temp.val} -> ",end="")
            temp=temp.next
        print("None")

S=stack()
S.display()
S.pop()
S.push(10)
S.push(20)
S.push(30)
S.peek()
S.pop()
S.display()