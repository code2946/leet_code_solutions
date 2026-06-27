
class Solution:
    from typing import List

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s=[]
        for num in nums :
            index =abs(num)-1
            if nums[index]>0:
                nums[index]=-nums[index]
        for i in range(len(nums)):
            if nums[i]>0:
                s.append(i +1)
        return s        
