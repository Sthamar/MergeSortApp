from typing import List, Optional
from schemas import ListNode

def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(val=-1)
    current = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    if list1:
        current.next = list1
    if list2:
        current.next = list2
        
    return dummy.next

def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
        
    # Split the list into two halves
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    mid = slow.next
    slow.next = None
        
    # Recursively split and merge
    left = sort_list(head)
    right = sort_list(mid)
        
    return merge_two_lists(left, right)

  