class Solution:
    def totalMoney(self, n: int) -> int:
        money = 0
        dailyMoney = 1

        week = 7
        j = 1
        for i in range(n):
            if i == week * j:
                dailyMoney = j + 1
                j += 1
            money += dailyMoney
            dailyMoney += 1

        return money

        