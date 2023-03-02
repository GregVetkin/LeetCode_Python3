from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_len = len(strs[0])
        prefix = strs[0]

        for word in strs:
            if len(word) > prefix_len:
                word = word[0:prefix_len]

            elif len(word) < prefix_len:
                prefix = prefix[0:len(word)]
                prefix_len = len(prefix)

            for index, letter in enumerate(word):
                if letter != prefix[index]:
                    prefix = prefix[0: index]
                    prefix_len = index
                    break

            if prefix_len == 0:
                return ""

        return prefix


    def longestCommonPrefix_goodsolution(self, strs: List[str]) -> str:
        first_word, last_word = min(strs), max(strs)  # alphabetical sorting!
        prefix = ''
        for ind in range(min(len(first_word), len(last_word))):
            if first_word[ind] != last_word[ind]:
                break
            prefix += first_word[ind]

        return prefix


if __name__ == '__main__':

    print([Solution().longestCommonPrefix(["dog", "racecar", "car"])])
    print([Solution().longestCommonPrefix(["flower", "flow", "flight"])])
    print([Solution().longestCommonPrefix(["", "flower", "flow", "flight"])])
    print([Solution().longestCommonPrefix(["aaa", "aa", "aaa"])])

    print([Solution().longestCommonPrefix_goodsolution(["dog", "racecar", "car"])])
    print([Solution().longestCommonPrefix_goodsolution(["flower", "flow", "flight"])])
    print([Solution().longestCommonPrefix_goodsolution(["", "flower", "flow", "flight"])])
    print([Solution().longestCommonPrefix_goodsolution(["aaa", "aa", "aaa"])])
