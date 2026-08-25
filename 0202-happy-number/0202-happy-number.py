class Solution(object):
    def isHappy(self, n):
        seen = set()
        while True:
            if n in seen:
                return False
            seen.add(n)
            num = list(map(int, str(n)))
            total = 0
            for i in range(len(num)):
                total += num[i] * num[i]
            if total == 1:
                return True
            n = total