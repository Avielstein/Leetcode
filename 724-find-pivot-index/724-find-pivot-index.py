class Solution(object):
    
    '''
    

    
    '''
    def pivotIndex(self, n):
        for i in range(len(n)):
            #test pivot condition
            if sum(n[:i])==sum(n[i+1:]): 
                #If the index is on the left edge of the array, then the 
                #left sum is 0 because there are no elements to the left. 
                #This also applies to the right edge of the array.
                if i==0 or i == len(n):
                    return 0
                return i
        
        
        #Return the leftmost pivot index. If no such index exists, return -1.
        return -1
        