class Solution:
    def isValid(self, s: str) -> bool:

        if s.count('(') != s.count(')') or s.count('[') != s.count(']') or s.count('{') != s.count('}'):
            return False

        open = ('(', '[', '{')
        close = (')', ']', '}')



if __name__ == '__main__':
    print(Solution().isValid("[()]"))
