class Solution(object):
    def rearrangeCharacters(self, s, t):
        a = []
        for i in set(t):
            a.append(s.count(i)/t.count(i))
        return min(a)
        
        '''
        #we can use modulo to count
        l = 0 #letter of char we need
        
        #go through the list and 
        for i in s:
            #if we have incountered the next letter we need
            if i == t[l%len(t)]: 
                
                #update the count
                l+=1
                
        #then, since we used module
        #we can return the floor division 
        #to count full copies found
        return l//len(t)
        '''
                    
                
        
        
        
        
        