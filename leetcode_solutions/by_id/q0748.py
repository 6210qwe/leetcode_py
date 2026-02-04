# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 748
标题: Largest Number At Least Twice of Others
难度: easy
链接: https://leetcode.cn/problems/largest-number-at-least-twice-of-others/
题目类型: 数组、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
747. 至少是其他数字两倍的最大数 - 给你一个整数数组 nums ，其中总是存在 唯一的 一个最大整数 。 请你找出数组中的最大元素并检查它是否 至少是数组中每个其他数字的两倍 。如果是，则返回 最大元素的下标 ，否则返回 -1 。 示例 1： 输入：nums = [3,6,1,0] 输出：1 解释：6 是最大的整数，对于数组中的其他整数，6 至少是数组中其他元素的两倍。6 的下标是 1 ，所以返回 1 。 示例 2： 输入：nums = [1,2,3,4] 输出：-1 解释：4 没有超过 3 的两倍大，所以返回 -1 。 提示： * 2 <= nums.length <= 50 * 0 <= nums[i] <= 100 * nums 中的最大元素是唯一的
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 找到数组中的最大值和次大值，并检查最大值是否至少是次大值的两倍。

算法步骤:
1. 初始化两个变量 `max_index` 和 `second_max`，分别记录最大值的索引和次大值。
2. 遍历数组，更新 `max_index` 和 `second_max`。
3. 检查最大值是否至少是次大值的两倍，如果是则返回 `max_index`，否则返回 -1。

关键点:
- 通过一次遍历找到最大值和次大值，确保时间复杂度为 O(n)。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组的长度。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(nums: List[int]) -> int:
    """
    函数式接口 - 找到数组中的最大元素并检查它是否至少是数组中每个其他数字的两倍。
    """
    if not nums:
        return -1

    max_index = 0
    second_max = float('-inf')

    for i in range(1, len(nums)):
        if nums[i] > nums[max_index]:
            second_max = nums[max_index]
            max_index = i
        elif nums[i] > second_max and nums[i] < nums[max_index]:
            second_max = nums[i]

    if nums[max_index] >= 2 * second_max:
        return max_index
    else:
        return -1


Solution = create_solution(solution_function_name)