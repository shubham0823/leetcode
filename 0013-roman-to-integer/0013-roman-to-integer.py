class Solution:
    def romanToInt(self, s: str) -> int:
               
        roman={
               "I":1,
               "IV":4,
               "V":5,
               "IX":9,
               "X":10,
               "XL":40,
               "L":50,
               "XC":90,
               "C":100,
               "CD":400,
               "D":500,
               "CM":900,
               "M":1000
                          } 
        x=False
        num=0
        
        for i in range(len(s)):
            if (x==True):
                x=False
                continue
            if i+1<len(s) and s[i]+s[i+1] in roman:
                x=True
                num = num+ roman[s[i]+s[i+1]] 
            elif s[i] in roman:
                num=num+roman[s[i]]
                    
                    
        return num
                    
                
                    
                    
                    
                    # 3649
                    # f="M",3649-1000=2649
                    # f="MM", 2649-1000=1649
                    # f ="MMM",1649-1000=649
                    # f="MMMD",649-500=149
                    # f="MMMDC",149-100=49
                    # f="MMMDCXL"49-40=9
                    # f="MMMDCXLIX"9-9=0
                    
        
