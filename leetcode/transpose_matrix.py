class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        index = 0
        while index < len(A[0]):
            temp = []
            for row in A:
                temp.append(row[index])
            res.append(temp)
            index += 1
        return res


print(Solution().transpose([[1,2,3],[4,5,6],[7,8,9]]))