class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values={}
        length=len(nums)
        for index in range(length):
            difference = target - nums[index]
            if difference in values:
                return values[difference],index
            values[nums[index]]=index