# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000320
标题: 最长连续序列
难度: medium
链接: https://leetcode.cn/problems/WhsWhI/
题目类型: 并查集、数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 119. 最长连续序列 - 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。 示例 1： 输入：nums = [100,4,200,1,3,2] 输出：4 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。 示例 2： 输入：nums = [0,3,7,2,5,8,4,6,0,1] 输出：9 提示： * 0 <= nums.length <= 104 * -109 <= nums[i] <= 109 进阶：可以设计并实现时间复杂度为 O(n) 的解决方案吗？ 注意：本题与主站 128 题相同： https://leetcode.cn/problems/longest-consecutive-sequence/ [https://leetcode.cn/problems/longest-consecutive-sequence/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希集合来存储数组中的所有元素，然后遍历数组中的每个元素，检查该元素是否是一个序列的起点。如果是，则通过递增查找序列的终点，并记录最长序列的长度。

算法步骤:
1. 将数组中的所有元素存入哈希集合。
2. 遍历数组中的每个元素，检查该元素是否是一个序列的起点（即该元素减一不在集合中）。
3. 如果是序列的起点，则通过递增查找序列的终点，并记录最长序列的长度。

关键点:
- 使用哈希集合来快速查找元素是否存在。
- 只有当元素是序列的起点时才进行递增查找，避免重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def longest_consecutive(nums: List[int]) -> int:
    """
    函数式接口 - 找出数字连续的最长序列的长度
    """
    if not nums:
        return 0

    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


Solution = create_solution(longest_consecutive)