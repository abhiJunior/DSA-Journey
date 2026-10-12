class Solution:

    def check_exist(self, hm, hm_s):
        for char in hm:
            if hm_s.get(char, 0) == 0:
                return False 
            if hm_s[char] < hm[char]:
                return False
        
        return True 

    def minWindow(self, s: str, t: str) -> str:
        hm = {}
        for char in t:
            if char in hm:
                hm[char] += 1
            else:
                hm[char] = 1
        
        hm_s = {}
        l = 0; h = 0; min_length = float("inf")
        st = -1; e = -1

        while h < len(s):
            if s[h] in hm_s:
                hm_s[s[h]] += 1
            else:
                hm_s[s[h]] = 1
            
            while self.check_exist(hm, hm_s):
                if min_length > h - l + 1:
                    min_length = h - l + 1
                    st = l; e = h; 
                
                hm_s[s[l]] -= 1
                if hm_s[s[l]] == 0:
                    del hm_s[s[l]]
                
                l += 1

            h += 1
        if min_length == float("inf"):
            return ""
        ans = ""
        for i in range(st, e+1):
            ans += s[i]
    
        return ans

        