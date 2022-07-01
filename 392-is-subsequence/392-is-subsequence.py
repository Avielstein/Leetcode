class Solution(object):
    def isSubsequence(self, s, t):
        
        #
        start = 0
        if start==len(s): return True
        
        
        for i in range(len(t)):  
            #print(t[i], s[start])
            if start >= len(s):
                return True
            
            if t[i] == s[start]:
                start+=1
            
        if start == len(s): 
            return True
        else: 
            return False

        