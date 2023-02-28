from typing import List


class Solution:

    def two_sum_n2(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for fixed_index in range(0, length):
            for target_index in range(fixed_index+1, length):
                if nums[fixed_index] + nums[target_index] == target:
                    return [fixed_index, target_index]

    def two_sum_n1(self, nums: List[int], target: int) -> List[int]:
        storage = {}
        for index, number in enumerate(nums):
            difference = target - number
            if difference in storage:
                return [storage[difference], index]
            else:
                storage[number] = index


if __name__ == '__main__':
    s = Solution()

    result_1 = s.two_sum_n2([0, 2, 3, 4, 5, 6, 7], 12)
    print(result_1)

    result_2 = s.two_sum_n1([0, 2, 3, 4, 5, 6, 7], 12)
    print(result_2)
