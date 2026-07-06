class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        r =0
        s =""
        while l < len(word1) or r <len(word2):
            if l <len(word1):
                s+=word1[l]
            if r <len(word2):
                s+=word2[r]
            l+=1
            r+=1
        return s        
        

                

    
                
                          



