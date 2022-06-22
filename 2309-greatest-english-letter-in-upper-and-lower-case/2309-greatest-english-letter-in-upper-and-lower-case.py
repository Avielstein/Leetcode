class Solution(object):
    def greatestLetter(self, s):
        greatest = ''
        x = sorted(set(s))
        for i in x[::-1]:
            if i.isupper():
                break
            if upper(i) in x:
                greatest = upper(i)
                break
        return greatest
        