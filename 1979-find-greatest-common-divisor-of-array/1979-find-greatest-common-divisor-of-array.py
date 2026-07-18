import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        l= float('-inf')
        r  =float('inf')
        for num in nums :
            if l < num:
                l= num
            if r > num :
                r= num
        return math.gcd(l,r)        
        
        