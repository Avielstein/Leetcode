class Solution(object):
    def shortestSequence(self, rolls, k):
        vis, cnt, ans = set(), 0, 1;
        
        for x in rolls:
            if x not in vis:
                vis.add(x)
                cnt += 1
            if cnt == k:
                vis, ans, cnt = set(), ans+1, 0
        
        return ans

        
#this solution works but isnt fast enough        
'''
from itertools import product

#https://www.geeksforgeeks.org/python-k-dice-combinations/
def get_all_seqs(num,lenth):
        # using list comprehension to formulate elements
        temp = [list(range(1, num+1)) for _ in range(lenth)]

        # using product() to get Combinations
        res = list(product(*temp))
        
        return res
    
def seq_in_rolls(seq,rolls):
    complete = []
    for r in rolls:
        if len(complete)==len(seq):
            break
        if r == seq[len(complete)]:
            complete.append(r)
    
    if len(complete)==len(seq):
        return True
    else:
        return False
    

class Solution(object):
    def shortestSequence(self, rolls, k):
        for i in range(len(rolls)):
            seqs = get_all_seqs(k,i+1)
            for s in seqs:
                if seq_in_rolls(s,rolls)==False:
                    return len(s)

            
        

        

'''