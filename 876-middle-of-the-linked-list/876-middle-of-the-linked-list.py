# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def LL2pylist(l):
        final_l=[]
        while l!=None:
            final_l.append(l.val)
            l = l.next
        return final_l 

def pylist2LL(l):
    #start by creating the final node
    LL = ListNode(l[-1])
    #then remove
    l = l[:-1]
    
    #we have to add them backwards to form the list
    for i in l[::-1]:
        LL = ListNode(val=i, next=LL)
    
    return LL


class Solution(object):
    def middleNode(self, h):
        l = LL2pylist(h)
        return pylist2LL(l[int(len(l)/2):])

        