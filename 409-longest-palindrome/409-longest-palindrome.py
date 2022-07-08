'''
summary: the code aims to count how many characters have an odd frequency.

longer explination:

i) The set 'ss' defined above stores the count of unique letters that have odd counts. So, for an array [b, e, d, d, b, b] it would store b and e as they have odd counts.
Follow up question: What's the use of doing that?
Explanation: Well, the main intention is to count one for all odd count letters after accounting for the even pairs in them if any. For example in [b, e, d, d, b, b] we know that for b and e only one count should be taken after accounting for the pair 'bb' for 'b'. This is because it doesn't make any difference in the final answer whether you have b or e in the middle('bdedb' or 'bdbdb' returns 5). Hope this clears some confusion.

ii) Finally, if there are no odd count letters present we want to count all even values for the counts(which is basically the length of the given array) as the final answer. Otherwise, we would need to adjust for the extra odd counts that we are doing when we are counting all the values by removing the count of all distinct odd letters and then counting 1 for them.

'''


class Solution(object):
    def longestPalindrome(self, s):
        ss = set()
        for letter in s:
            if letter not in ss:
                ss.add(letter)
            else:
                ss.remove(letter)
        if len(ss) != 0:
            return len(s) - len(ss) + 1
        else:
            return len(s)

        