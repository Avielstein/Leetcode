class Solution(object):
    def addBinary(self, a, b):
        #FYI:
        #bin converts number to its binrary form
        #int can convert a number of some base to a decimal
        x = bin(int(a,2)+int(b,2)) 
        return x[2:]
        