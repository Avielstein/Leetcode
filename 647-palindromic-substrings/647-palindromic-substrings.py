def is_palin(s):
    return s==s[::-1]

def slide_window(s, w): #string, window size
    count=0
    for i in range(len(s)-w+1):
        if is_palin(s[i:i+w]):
            count+=1
    return count
    

class Solution(object):
    def countSubstrings(self, s):
        count = len(s)
        for i in range(2,len(s)+1):
            count+=slide_window(s,i)
            
        return count
            
        