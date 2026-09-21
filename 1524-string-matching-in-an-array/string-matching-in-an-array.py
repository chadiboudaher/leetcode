class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        results = []

        for i in words:
            for j in words:
                if i != j and i in j:
                    results.append(i)

        return list(set(results))