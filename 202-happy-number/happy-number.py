class Solution:
    def isHappy(self, n: int) -> bool:

        s = 0 
        num = n 
        hmset = set()
        while num != 1:
            if s == 1:
                return True 
            if s > 0:
                if s in hmset:
                    return False 
                hmset.add(s)
                num = s 
                s = 0
            while num > 0:
                digit = num % 10
                s += (digit)**2 
                num = num // 10
        return True 
            

        