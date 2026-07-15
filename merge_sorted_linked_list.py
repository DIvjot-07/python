class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        result=ListNode()
        temp=result
        while(list1 is not None and list2 is not None):
            node=ListNode()
            if(list1.val < list2.val):
                node.val=list1.val
                list1=list1.next
            else:
                node.val=list2.val
                list2=list2.next
            temp.next=node
            temp=temp.next
        while(list1 is not None):
            node=ListNode()
            node.val=list1.val
            temp.next = node
            temp = temp.next
            list1=list1.next
        while(list2 is not None):
            node=ListNode()
            node.val=list2.val
            temp.next = node
            temp = temp.next
            list2=list2.next
        return result.next