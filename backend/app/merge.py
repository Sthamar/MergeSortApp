from fastapi import APIRouter, HTTPException, status
from typing import List
from schemas import ListNode
from utils import merge_two_lists, sort_list

router = APIRouter(prefix="/merge", tags=["Merge"])

@router.post("/", response_model=List[int])
def merge_list(list1: List[int], list2: List[int]) -> List[int]:
    if not list2:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="list2 cannot be empty")
    list2_node = ListNode(val=list2[0])
    if not list2:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="list2 is empty")
        
    list1_node = ListNode(val=list1[0])
    list2_node = ListNode(val=list2[0])
    
    current1 = list1_node
    for val in list1[1:]:
        current1.next = ListNode(val=val)
        current1 = current1.next
        
    current2 = list2_node
    for val in list2[1:]:
        current2.next = ListNode(val=val)
        current2 = current2.next
    
    sorted_list1 = sort_list(list1_node)  
    sorted_list2 = sort_list(list2_node)  
    merged_head = merge_two_lists(sorted_list1, sorted_list2)
    
    return merged_head.to_list()

