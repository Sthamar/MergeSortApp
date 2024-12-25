from pydantic import BaseModel
from typing import List, Optional

class ListNode(BaseModel):
    val: int
    next: Optional['ListNode'] = None
    
    def to_list(self):
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return result
    
