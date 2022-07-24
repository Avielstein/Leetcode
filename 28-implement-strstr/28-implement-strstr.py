class Solution(object):
    def strStr(self, h, n):
        if n in h:
            return h.index(n)
        else:
            return -1
        