class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:

        login = int(loginTime[:2]) * 60 + int(loginTime[3:])
        logout = int(logoutTime[:2]) * 60 + int(logoutTime[3:])

        if logout < login:
            logout += 24 * 60

        while login % 15:
            login += 1

        while logout % 15:
            logout -= 1

        return max((logout - login) // 15, 0)

# Time:  O(1)
# Space: O(1)
