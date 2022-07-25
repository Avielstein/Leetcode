class Solution(object):
    def merge(self, nums1, m, nums2, n):
        x = sorted(nums1[:m]+nums2) #get all our numbers in one place
        for i in range(len(nums1)):
            nums1[i]=x[i]
            