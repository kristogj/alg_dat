class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        m,n = {},{}
        for x in range(len(s)):
            if s[x] in m.keys():
                if m[s[x]] != t[x]:
                    return False
            elif t[x] in n.keys():
                if n[t[x]] != s[x]:
                    return False
            else:
                m[s[x]] = t[x]
                n[t[x]] = s[x]
        return True

    def isIsomorphic_easier(self,s,t):
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))



s = Solution()
print(s.isIsomorphic("ab","aa"))
print(s.isIsomorphic_easier("ab","aa"))

