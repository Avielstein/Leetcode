class Solution(object):
    def plusOne(self, d):
        
        #convert from list to number
        tens_place=0
        count=0
        for i in d[::-1]:
            count+=(i*(10**tens_place))
            tens_place+=1
            
        #add one
        count+=1
        
        #convert from number to list
        #and add to new list
        new=[]
        for i in str(count):
            new.append(i)
            
        return new
        
        