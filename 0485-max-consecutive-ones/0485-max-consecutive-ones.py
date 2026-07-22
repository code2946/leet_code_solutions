class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l =0 
        r =0
        count=[]
        while r < len(nums):
            if nums[l]==1 and nums[r]==1 :
                count.append(r-l+1)
                r+=1 
            elif nums[r]== 0 and nums[l]==1:
                l =r   
            elif nums[r]== 0 and nums[l]==0:
                l+=1
                r+=1
        return max(count) if count else 0       
