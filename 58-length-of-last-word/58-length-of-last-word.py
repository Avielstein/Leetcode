class Solution(object):
    def lengthOfLastWord(self, s):
        s = " ".join(s.split()) #get rid of extra spaces
        return len(s.split(' ')[-1])
        