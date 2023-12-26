class Solution:
    def isPalindrome(self, x: int) -> bool:
        b=[]
        if (x<0):
            return False
        while(x!=0):
            a=x%10
            b.append(a)
            x=int(x/10)
        c=b.copy()
        c.reverse()
        for k in range(0,len(b)):
            if b[k]!=c[k]:
                return False
        return True

            
   
            
    