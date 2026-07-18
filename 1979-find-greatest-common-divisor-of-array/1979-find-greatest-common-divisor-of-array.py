import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        l= float('-inf')
        r  =float('inf')
        for num in nums :
            l = max(l , num)
            r = min(r,num)
        return math.gcd(l,r)        
        
        