class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s=[]
        s1=[]
        s2=[]
        map1={}
        map2= {}
        for i in nums1 :
            if i not in map1 :
                map1[i]=1
            else :
                map1[i]+=1    
        for j in nums2 :
            if j not in map2 :
                map2[j]=1
            else :
                map2[j]+=1    
        for a in map1:
            if a not in map2:
                s1.append(a)
        for b in map2:
            if b not in map1:
                s2.append(b) 
        s.append(s1)
        s.append(s2)    
        return s  