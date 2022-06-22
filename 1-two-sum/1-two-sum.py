class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in range(len(nums)):      
            diff = target-nums[n]
            z = nums[n+1:]
            if diff in z:
                return [n,z.index(diff)+n+1]
                
        