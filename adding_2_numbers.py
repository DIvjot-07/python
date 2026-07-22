# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        num1,num2=0,0
        output=ListNode()
        temp=output
        count1,count2=0,0
        temp1=l1
        temp2=l2
        while(temp1 is not None and temp1.val==0):
            count1+=1
            temp1=temp1.next
        while(temp2 is not None and temp2.val==0):
            count2+=1
            temp2=temp2.next
        while(l1 is not None):
            num1*=10
            num1+=l1.val
            l1=l1.next
        while(l2 is not None):
            num2*=10
            num2+=l2.val
            l2=l2.next
        num1=str(num1)
        num1=num1[::-1]
        num1=int(num1)
        num2=str(num2)
        num2=num2[::-1]
        num2=int(num2)
        num1=num1*(10**count1)
        num2=num2*(10**count2)
        num=num1+num2
        if num == 0:
            return ListNode(0)
        while(num!=0):
            temp.next=ListNode(num%10)
            temp=temp.next
            num //= 10
        return output.next