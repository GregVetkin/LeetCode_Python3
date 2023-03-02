class Solution:
    def romanToInt_1(self, s: str) -> int:
        roman_number = {'I': 1,
                        'V': 5,
                        'X': 10,
                        'L': 50,
                        'C': 100,
                        'D': 500,
                        'M': 1000}
        length = len(s)
        number = 0
        int_numbers = []
        for letter in s:
            int_numbers.append(roman_number[letter])
        int_numbers.append(0)

        i = 0
        while i < length:

            if int_numbers[i+1] > int_numbers[i]:
                number += int_numbers[i+1] - int_numbers[i]
                i += 2

            else:
                number += int_numbers[i]
                i += 1

        return number

    def romanToInt_2(self, s: str) -> int:
        roman_number = {'I': 1,
                        'V': 5,
                        'X': 10,
                        'L': 50,
                        'C': 100,
                        'D': 500,
                        'M': 1000}

        number = 0
        i = 0

        while i < len(s) - 1:

            if roman_number[s[i]] < roman_number[s[i+1]]:
                number += roman_number[s[i+1]] - roman_number[s[i]]
                i += 2

            else:
                number += roman_number[s[i]]
                i += 1

        if not i >= len(s):
            number += roman_number[s[-1]]

        return number


    def romanToInt_3_sol(self, s: str) -> int:
        roman_number = {'I': 1,
                        'V': 5,
                        'X': 10,
                        'L': 50,
                        'C': 100,
                        'D': 500,
                        'M': 1000}

        number = 0
        for i in range(len(s)-1):
            if roman_number[s[i+1]] > roman_number[s[i]]:
                number -= roman_number[s[i]]
            else:
                number += roman_number[s[i]]

        number += roman_number[s[-1]]
        return number


if __name__ == '__main__':
    print(Solution().romanToInt_3_sol('CIX'))