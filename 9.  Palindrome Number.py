class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reverse = 0
        origin = x

        while x > 0:
            reverse = reverse * 10 + x % 10
            x //= 10

        return origin == reverse


if __name__ == '__main__':
    s = Solution()
    result = s.isPalindrome(987654321123456789)
    print(result)
