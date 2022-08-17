class Solution(object):
    def arithmeticTriplets(self, n, d):
        count=0
        #for each number in the list we have to check if there is an arithmetic tripple
        for i in range(len(n)-2): #we only need to check up to the last 3 because we know there cant be more
            #so we see if we add the differences to our number if they exist in the list
            if n[i]+d in n and n[i]+(2*d) in n:
                #proof
                #print(n[i],n[i]+d,n[i]+(2*d))
                count+=1
        return count