class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # Number of 1s here is the hamming distance, bin() returns a string
        return bin(x^y).count('1')


s = Solution()
print(s.hammingDistance(1,4))
