class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        if list1.val>=list2.val:
            sortedLL=ListNode(list2.val)
            list2=list2.next
        else:
            sortedLL=ListNode(list1.val)
            list1=list1.next
        result=sortedLL


        while list1!=None and list2!=None:
            if list1.val>=list2.val:
                sortedLL.next=ListNode(list2.val)
                list2=list2.next
            else:
                sortedLL.next=ListNode(list1.val)
                list1=list1.next
            sortedLL=sortedLL.next

        sortedLL.next = list1 if list1 else list2
        return result