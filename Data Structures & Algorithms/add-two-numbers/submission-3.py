# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a1,a2=[],[]
        while l1!=None:
            a1.append(l1.val)
            l1=l1.next

        while l2!=None:
            a2.append(l2.val)
            l2=l2.next

        num1=0
        num2=0
        for i in range(len(a1)):
            num1+=a1[i]*10**i
        for i in range(len(a2)):
            num2+=a2[i]*10**i
        
        result=num1+num2
        if result==0:
            return ListNode(0,None)
        head=ans=ListNode(0,None)
        while result:
            ans.next=ListNode(0,None)
            ans.next.val=result%10
            ans.next.next=None
            ans=ans.next
            result=result//10

        return head.next