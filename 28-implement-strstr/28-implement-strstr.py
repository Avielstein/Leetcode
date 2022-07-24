class Solution(object):
    def strStr(self, h, n):
        if n not in h:
            return -1
        else:
            return h.index(n)
        