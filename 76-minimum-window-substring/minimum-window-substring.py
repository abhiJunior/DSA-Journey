class Solution:

    ## kaam ho rha hai ki nhi 
    def workDone(self,sFreq,tFreq):
        
        for i in range(len(tFreq)):
            if tFreq[i] > 0:
                if tFreq[i] > sFreq[i]:
                    return False 
        return True 

    def minWindow(self, s: str, t: str) -> str:

        ans = ""
        high = 0 ; low = 0 ; st = - 1 ; end = - 1
        res = float("inf") 
        sFreq = [0]*256 
        tFreq = [0]*256 
        print(s)
        n = len(s)

        for i in range(len(t)):
            idx = ord(t[i])
            tFreq[idx] += 1

        while high < n:
            idx = ord(s[high])
            sFreq[idx] += 1

            ## kaam ho rha hai or sahi jab tak shrink kr rhe hai 
            while self.workDone(sFreq,tFreq):
                if res > high - low + 1:
                    res = high - low + 1
                    st = low
                    end = high
                idx = ord(s[low])
                sFreq[idx] -= 1
                low += 1
            ## kaam nhi hora toh hiring kr rhe hai 
            high += 1

        if st == -1 and end == -1:
            return ""
        for i in range(st,end + 1):
            ans += s[i]
        return ans 
        
        
        
        