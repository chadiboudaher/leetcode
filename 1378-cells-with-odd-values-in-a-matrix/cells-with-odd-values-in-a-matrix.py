class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n

        for r, c in indices:
            rows[r] += 1
            cols[c] += 1

        odd_rows = sum(r % 2 == 1 for r in rows)
        odd_cols = sum(c % 2 == 1 for c in cols)

        return odd_rows * (n - odd_cols) + (m - odd_rows) * odd_cols


