class Solution:
    def isValid(self, s: str) -> bool:

        pair = {'(': ')',
                '{': '}',
                '[': ']'}
        stack = []

        for symbol in s:

            if symbol in '([{':
                stack.append(symbol)
            elif len(stack) == 0 or symbol != pair[stack.pop()]:
                return False

        return len(stack) == 0


if __name__ == '__main__':
    print(Solution().isValid("{[][][]}"))
    print(Solution().isValid("{[(][][]}"))
    print(Solution().isValid("(]"))
