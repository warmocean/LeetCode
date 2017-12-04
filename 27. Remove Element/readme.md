* 目标：给定一个array和一个值v，删除array中所有v，并返回新array的长度。
* 要求：
  * 不允许分配额外的空间，空间复杂度O(1)
  * 新array中元素顺序可以变化

* 思路1：
  * 遍历时，若发现v，则将v后面的值往前挪动1格，挪动后再从当前值继续遍历，直到遍历完毕。
  * 效率：Runtime: 42 ms。 Your runtime beats 25.51 % of python submissions.
  
  * 代码：
  `
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
  `

* 思路2：
  * 采用双指针遍历，遍历时，若前指针发现v，则判断后指针的值是否为v，若是，则两个指针都挪动，继续遍历，若否，则将后指针的值挪动至前指针处，继续遍历，直到两个指针交叉。
  * 效率：Runtime: 38 ms。 Your runtime beats 57.50 % of python submissions.
  
  * 代码：
  `
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
  `
