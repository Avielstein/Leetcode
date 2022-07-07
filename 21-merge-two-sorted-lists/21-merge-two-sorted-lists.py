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
    
    def mergeTwoLists(self, l1, l2):
        
        #handle empty lists
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        return pylist2LL(sorted(LL2pylist(l1) + LL2pylist(l2)))


        
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def r(l1,l2,l3):
    print('----')
    print(l1)
    print(l2)
    
    #if l1.next== None and l2.next== None:
    if l1 == None and l2 == None:
        return l3
    elif l1 == None:
        l3.next = ListNode(l2.val)
        l2=l2.next
    elif l2 == None:
        l3.next = ListNode(l1.val)
        l1=l1.next
    else:
        a = l1.val
        b = l2.val
        if a>=b:
            l3.next = ListNode(l1.val)
            l1=l1.next
        else:
            l3.next = ListNode(l2.val)
            l2=l2.next
    
    return r(l1,l2,l3)

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        a = list1.val
        b = list2.val
        if a>=b:
            l3 = ListNode(list1.val)
            list1=list1.next
        else:
            l3 = ListNode(list2.val)
            list2=list2.next
        return r(list1,list2,l3)

'''
        