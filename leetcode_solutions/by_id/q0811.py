# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 811
标题: Number of Subarrays with Bounded Maximum
难度: medium
链接: https://leetcode.cn/problems/number-of-subarrays-with-bounded-maximum/
题目类型: 数组、双指针
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
795. 区间子数组个数 - 给你一个整数数组 nums 和两个整数：left 及 right 。找出 nums 中连续、非空且其中最大元素在范围 [left, right] 内的子数组，并返回满足条件的子数组的个数。 生成的测试用例保证结果符合 32-bit 整数范围。 示例 1： 输入：nums = [2,1,4,3], left = 2, right = 3 输出：3 解释：满足条件的三个子数组：[2], [2, 1], [3] 示例 2： 输入：nums = [2,9,2,5,6], left = 2, right = 8 输出：7 提示： * 1 <= nums.length <= 105 * 0 <= nums[i] <= 109 * 0 <= left <= right <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针法来遍历数组，找到所有符合条件的子数组。

算法步骤:
1. 初始化两个指针 `start` 和 `end`，以及计数器 `count` 和 `prev_count`。
2. 遍历数组：
   - 如果当前元素大于 `right`，则重置 `start` 和 `end` 指针。
   - 如果当前元素小于 `left`，则更新 `prev_count`。
   - 如果当前元素在 `[left, right]` 范围内，则计算从 `start` 到当前元素的所有子数组数量，并更新 `prev_count`。
3. 返回 `count`。

关键点:
- 使用双指针法可以有效地找到所有符合条件的子数组。
- 通过维护 `prev_count` 来避免重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组的长度。我们只需要一次遍历数组。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_subarrays_with_bounded_max(nums: List[int], left: int, right: int) -> int:
    """
    函数式接口 - 计算满足条件的子数组数量
    """
    start, end = -1, -1
    count, prev_count = 0, 0

    for i, num in enumerate(nums):
        if num > right:
            start, end = i, i
            prev_count = 0
        elif num < left:
            count += prev_count
        else:
            end = i
            prev_count = end - start
            count += prev_count

    return count


Solution = create_solution(count_subarrays_with_bounded_max)