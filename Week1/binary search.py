class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L=0
        R=len(nums)-1
        while L<=R:
            k=(L+R)//2
            if target==nums[k]:
                return k
            if target>nums[k]:
                L=k+1
                continue
                
            if target<nums[k]:
                R=k-1
                continue
                
        return -1 