class Solution:
    def countAndSay(self,n):
        num = "1"
        while n != 1:
            num = self.next_state(num)
            n -= 1
        return num

    def next_state(self,number):
        lst = list(str(number))[::-1]
        last = None
        temp = ""
        res = []
        while lst:
            current = lst.pop()
            if current == last or not last:
                last = current
                temp += current
            else:
                res.append(temp)
                temp = current
                last = current
        if temp:
            res.append(temp)

        res = [str(len(s)) + s[0] for s in res]
        return "".join(res)


s = Solution()
print(s.countAndSay(4))
