# Link: https://leetcode.com/problems/add-two-numbers
# Status: Solution accepted and beats 68.29%

# Problem statement: You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# My solution uses an auxiliar sum function that sums the values between two nodes taking into account the sum carry. Then we use it while looping through the Nodes until both are None.

from typing import Optional

#Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def sum_nodes(n1: ListNode, n2: ListNode, carry: int = 0) -> tuple[ListNode, int]:
            if n1 is None and n2 is None:
                return None
            if n1 is None:
                return ListNode(val=(n2.val + carry)%10), (n2.val + carry)//10
            if n2 is None:
                return ListNode(val=(n1.val + carry)%10), (n1.val + carry)//10
            
            return ListNode(val=(n1.val+n2.val + carry)%10), (n1.val+n2.val + carry)//10
        
        head, carry = sum_nodes(l1, l2)
        l1 = l1.next
        l2 = l2.next

        current_node = head

        while l1 is not None or l2 is not None:
            current_node.next, carry = sum_nodes(l1,l2,carry)
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            current_node = current_node.next
        
        if carry == 1:
            current_node.next = ListNode(val=1)
        return head

if __name__ == "__main__":
    testcases = [[[9,9,9,9,9,9,9], [9,9,9,9]]]

    for ts in testcases:
        head1 = ListNode(ts[0][0])

        cn = head1

        for n in ts[0]:
            node = ListNode(n)
            cn.next=node
            cn = node
        
        head2 = ListNode(ts[1][0])

        cn = head2

        for n in ts[1]:
            node = ListNode(n)
            cn.next=node
            cn = node

        r_head = Solution.addTwoNumbers(None,head1,head2)

        print(f"testcase: {ts} Result: ", end="")
        
        r_node = r_head
        while r_node is not None:
            print(f"{r_node.val},", end="")
            r_node = r_node.next