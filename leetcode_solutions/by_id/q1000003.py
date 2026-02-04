# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000003
标题: Contiguous Sequence LCCI
难度: easy
链接: https://leetcode.cn/problems/contiguous-sequence-lcci/
题目类型: 数组、分治、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 16.17. 连续数列 - 给定一个整数数组，找出总和最大的连续数列，并返回总和。 示例： 输入： [-2,1,-3,4,-1,2,1,-5,4] 输出： 6 解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。 进阶： 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划（Kadane's Algorithm）来找到最大子数组和。

算法步骤:
1. 初始化两个变量 `current_sum` 和 `max_sum`，分别表示当前子数组的和以及最大子数组的和。
2. 遍历数组中的每个元素：
   - 更新 `current_sum` 为当前元素与 `current_sum + 当前元素` 中的较大值。
   - 更新 `max_sum` 为 `max_sum` 与 `current_sum` 中的较大值。
3. 返回 `max_sum`。

关键点:
- 动态规划的状态转移方程是 `current_sum = max(nums[i], current_sum + nums[i])`。
- 通过一次遍历即可找到最大子数组和。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组的长度，因为只需要遍历数组一次。
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
    函数式接口 - 使用动态规划（Kadane's Algorithm）来找到最大子数组和。
    """
    if not nums:
        return 0

    current_sum = max_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


Solution = create_solution(solution_function_name)