class Solution(object):
    def numberOfLines(self, widths, S):
        """
        Max width of a line is 100, if the last letter on the line makes the line width bigger then a 100
        you have to put it on the next line
        :type widths: List[int] -> where widths[0] is the width of letter 'a' and widths[1] is the width of 'b'
        :type S: str -> the string to write
        :rtype: List[int]
        """
        lst = map(lambda s: widths[ord(s) - 97], S)
        lines = 1
        current_line = 0
        for n in lst:
            if current_line + n > 100:
                lines += 1
                current_line = 0
            current_line += n
        return [lines, current_line]

