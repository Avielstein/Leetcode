# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#from: https://leetcode.com/problems/linked-list-cycle-ii/discuss/1381922/Easy-Python-Solution-(Faster-than-95)

class Solution:
    def detectCycle(self, head):
        s, f = head, head
        
        #empty list
        if not s:
            return None
        
        #list with only one element
        if not s.next:
            return None
        
        #as long as there is a next one
        while f and f.next:
            
            #
            f, s = f.next.next, s.next
            if f == s:
                break
        
        if f == s:
            
            #move on to the next element
            while f != head:
                f = f.next
                head = head.next
            return head
        
        else:
            return None
        