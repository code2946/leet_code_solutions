class Solution:
    def sumAndMultiply(self, n: int) -> int:
        p=str(n)
        u=0
        s=""
        for i in p :
            if i!='0':
                
                s+=i
            u+=int(i)    
        return  u * int(s) if s else 0
          

