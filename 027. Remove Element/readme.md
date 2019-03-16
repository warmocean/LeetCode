* 目标：给定一个array和一个值v，删除array中所有v，并返回新array的长度。
* 要求：
  * 不允许分配额外的空间，空间复杂度O(1)
  * 新array中元素顺序可以变化

* 思路1：
  * 遍历时，若发现v，则将v后面的值往前挪动1格，挪动后再从当前值继续遍历，直到遍历完毕。（即设置两个指针，一个读，一个写，读指针挨个遍历，碰到非v元素写指针才写入并计数）
  * 效率：Runtime: 39 ms。 Your runtime beats 38.47 % of python submissions.

* 思路2：
  * 采用双指针遍历，一个从头到尾，一个从尾到头，遍历时，若前指针发现v，则判断后指针的值是否为v，若是，则两个指针都挪动，继续遍历，若否，则将后指针的值挪动至前指针处，继续遍历，直到两个指针交叉。
  * 效率：Runtime: 38 ms。 Your runtime beats 57.50 % of python submissions.
  * 优点：当元素移动不频繁时，相比第一种方法，效率更高。