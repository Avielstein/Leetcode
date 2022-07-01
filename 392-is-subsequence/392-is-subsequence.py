class Solution(object):
    def isSubsequence(self, s, t):
        
        #set up var and check for empty string
        start = 0
        if start==len(s): return True
        
        for i in range(len(t)):  
            
            #we found the whole substring
            if start >= len(s):
                return True
            
            #we found the letter
            if t[i] == s[start]:
                start+=1
        
        #final check
        if start == len(s): 
            return True
        else: 
            return False

        