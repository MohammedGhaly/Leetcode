class Solution:
    def multiply(self, num1: str, num2: str):
        if num1 == "0" or num2 == "0": return "0"
        num1, num2 = num1[::-1], num2[::-1]
        res = [0] * (len(num1)+len(num2))
        
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1+i2]+=digit
                res[i1+i2+1] += (res[i1+i2] // 10)
                res[i1+i2]=res[i1+i2]%10
        
        res = res[::-1]
        start = 0
        for i in range(len(res)):
            if res[i] == 0:
                continue
            start=i
            break
        
        res = map(str, res[start:])
        return "".join(res) 
            
sol = Solution()            
res = sol.multiply('11', '11')
print(res)
        
        
        
        
    
    
print("2")