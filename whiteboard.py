"""
Lucky Numbers
Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.
Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.
Example 1:
Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
Example 2:
Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
"""
nums = [1, 2, 2, 3, 3, 3]
nums2 = [2, 2, 3, 4]
nums3 = [3, 2, 3]


def lucky(nums):
    lucky_num = 0
    for num in nums:
        if nums.count(num) == num and num > lucky_num:
            lucky_num = num
    return lucky_num if lucky_num > 0 else -1


print(lucky(nums))
print(lucky(nums2))
print(lucky(nums3))


def lucky_comp(nums):
    return max([num for num in nums if num == nums.count(num)])


def lucky_zip(nums):
    return max(map(lambda x: x[0], set(list(filter(lambda x: x[0] == x[1], list(zip(nums, map(lambda x: nums.count(x), nums))))))))


def lucky_zip2(nums):
    return max(map(lambda x: x[0], filter(lambda x: x[0] == x[1], zip(nums, map(lambda x: nums.count(x), nums)))))


def lucky_dict(nums):
    hash_map = {}
    for num in nums:
        hash_map[num] = hash_map.get(num, 0)+1
    lucky = [key for key in hash_map if hash_map[key] == key]
    most = max(lucky)
    return max(key for key in hash_map if hash_map[key] == most) if lucky else -1
