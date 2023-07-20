def lengthOfLastWord(s: str) -> int:
        k = 0

        while s[-1] == ' ':
            s = s[:len(s) - 1]

        while s[0] == ' ':
            s = s[1:]

        if len(s) <= 1:
            return 1

        for i in range(1, len(s) + 1):

            if s[-i] != ' ':
                k += 1

            else:
                return k 
        return k

s = "   day"

print(lengthOfLastWord(s))