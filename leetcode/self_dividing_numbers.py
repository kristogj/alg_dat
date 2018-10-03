class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for x in range(left, right + 1):
            if self.check(x):
                res.append(x)
        return res

    def check(self, x):
        s = set(str(x))
        if "0" in s:
            return False
        for num in s:
            if x % int(num) != 0:
                return False
        return True


print(Solution().selfDividingNumbers(47,85))
