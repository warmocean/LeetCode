class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        """
        方法1：（煞笔做法）
        initial_len = len(nums)
        final_len = 0
        i = 0
        while i < initial_len:        
            num = nums[i]
            if num == val:
                if i == initial_len - 1:
                    break
                if nums[i+1] != val:
                    nums[final_len] = nums[i+1]
                    final_len += 1
                    i += 1
            else:
                nums[final_len] = nums[i]
                final_len += 1
            i += 1
        return final_len
        
        
        方法1：（正确做法）
        final_len = 0
        for i, num in enumerate(nums):        
            if num != val:
                nums[final_len] = num
                final_len +=1

        return final_len       
        
        """
        
        """
        方法2：
        initial_len = len(nums)
        idx_start = 0
        idx_end = initial_len - 1
        final_len = 0
        while idx_start <= idx_end:
            start = nums[idx_start]
            end = nums[idx_end]
            if start != val:
                idx_start += 1
                final_len += 1
            else:
                if end != val:
                    nums[idx_start] = end
                    idx_start += 1
                    final_len += 1
                idx_end -= 1
        return final_len
        """
        
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start +=1
        return start
        """
