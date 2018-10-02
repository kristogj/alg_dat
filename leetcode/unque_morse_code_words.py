def uniqueMorseRepresentations(words):
    """
    :type words: List[str]
    :rtype: int
    """
    # a is in pos 0 etc...
    signs = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
             "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
             "..-", "...-", ".--", "-..-", "-.--", "--.."]
    res = set()
    for word in words:
        temp = ""
        for x in range(len(word)):
            pos = ord(word[x]) - 97
            temp += signs[pos]
        res.add(temp)

    return len(res)


"""
Example
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
"""

print(uniqueMorseRepresentations(["gin","zen","gig","msg"]))