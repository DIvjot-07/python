class node(object):
    def __init__(self,val):
        self.data=val
        self.next=None

class LinkedList(object):
    def __init__(self):
        self.head=None
        self.len=0
    
    def Create(self):
        n=int(input("Enter Number of Elements in Linked List : "))
        if(n>0):
            val=int(input("Enter Element 1 : "))
            self.head=node(val)
            temp=self.head
            self.len+=1
            for i in range(1,n):
                val=int(input(f"Enter Element {i+1} : "))
                new_node=node(val)
                temp.next=node(val)
                temp=temp.next
                self.len+=1
        self.Display()

    def reverseList(self):
        prev=None
        temp=self.head
        while(temp!=None):
            next_n=temp.next
            temp.next=prev
            prev=temp
            temp=next_n
        self.head=prev
        self.Display()

    def reverseBetween(self, left, right):
        if left == right:
            return
        temp=self.head
        for i in range(1,left):
            temp=temp.next
        prev=None
        curr=temp.next
        for i in range(1,right-left+1):
            next_n=curr.next
            curr.next=prev
            prev=curr
            curr=next_n
        temp.next=prev
        temp1=self.head
        for i in range(1,right):
            temp1=temp1.next
        curr.next=temp1

        
        

        

    
    def Display(self):
        temp=self.head
        print("Linked List :",end=' ')
        for i in range(self.len):
            print(f"{temp.data}",end=" -> ")
            temp=temp.next
        print("None")
    
L=LinkedList()
L.Create()
L.reverseList()

