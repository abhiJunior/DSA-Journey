class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:

        line = 0 ; summ = 0 ; flag = False
        for i in range(len(s)):

            score = ord(s[i]) - 97
            summ += widths[score]
            if summ > 100:
                line += 1
                flag = True
                summ = widths[score]

        if summ <= 100 and flag:
            line += 1
        elif summ <= 100 and flag == False:
            line += 1

        return [line ,summ]
        