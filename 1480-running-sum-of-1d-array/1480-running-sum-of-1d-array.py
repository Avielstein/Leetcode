class Solution(object):
    def runningSum(self, n):
        '''
        a = []
        for i in range(len(n)):
            a.append(sum(n[:i+1]))
        return a
        '''
        
        #this is a slightly faster "dynamic solution"
        #but its longer to write, we save time by not repeating sum
        a = []
        total = sum(n)
        for i in range(len(n)):
            a.append(total)
            total-=n[-(i+1)]
        return a[::-1]