class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        index = 0
        length = len(s)

        group_counts = []

        while index < length:
            current_count = 1
            while index + 1 < length and s[index + 1] == s[index]:
                current_count += 1
                index += 1
            group_counts.append(current_count)
            index += 1

        results = 0
        result = 0
        for i in range(1, len(group_counts)):
            result += min(group_counts[i - 1], group_counts[i])

        return result