class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s_list = list(s)
        i = 0
        j = len(s) - 1

        while i < j:
            if not s_list[i].isalpha():
                i += 1
            elif not s_list[j].isalpha():
                j -= 1
            else:
                s_list[j], s_list[i] = s_list[i], s_list[j]
                i += 1
                j -= 1

        return "".join(s_list)
        