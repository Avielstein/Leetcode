class Solution(object):
    def arithmeticTriplets(self, n, d):
        count=0
        for i in range(len(n)):
            if n[i]+d in n and n[i]+(2*d) in n:
                #print(n[i],n[i]+d,n[i]+(2*d))
                count+=1
        return count