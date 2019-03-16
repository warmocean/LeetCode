'''
    思路1：暴力遍历——遍历每个元素x并判断是否存在target-x
        复杂度：时间O(n^2)，空间O(1)
    思路2：思路1的问题是查找元素的时间长，那就想办法减少查找时间，用哈希表/字典dict（搜索时间为常数级）
        扫描时计算每个数字a的对应差值b，并将a与下标n存入字典{a:n}，
        复杂度：时间O(n)，空间O(n)
    出现的错误：
        1、没有考虑target=2*num的情况，例如[1,2,3],6，此时会返回两个一样位置的数组；
        2、修改错误1后，没有考虑target=2*num且有两个数的情况，例如[3,3],6，此时会返回null。
'''

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for idx, num in enumerate(nums):
            pair = target - num
            if pair in d and idx != d[pair]:
                return [d[pair], idx]
            d[num] = idx
        return None


#        nums_dict = {}
#        for i in range(len(nums)):
#            if target - nums[i] in nums_dict:
#                return [nums_dict[target - nums[i]], i]
#            else:
#                nums_dict[nums[i]] = i
#        return None
