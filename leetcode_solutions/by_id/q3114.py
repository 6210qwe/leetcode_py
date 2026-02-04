# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3114
标题: Beautiful Towers I
难度: medium
链接: https://leetcode.cn/problems/beautiful-towers-i/
题目类型: 栈、数组、单调栈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2865. 美丽塔 I - 给定一个包含 n 个整数的数组 heights 表示 n 座连续的塔中砖块的数量。你的任务是移除一些砖块来形成一个 山脉状 的塔排列。在这种布置中，塔高度先是非递减，有一个或多个连续塔达到最大峰值，然后非递增排列。 返回满足山脉状塔排列的方案中，高度和的最大值 。 示例 1： 输入：maxHeights = [5,3,4,1,1] 输出：13 解释：我们移除一些砖块来形成 heights = [5,3,3,1,1]，峰值位于下标 0。 示例 2： 输入：maxHeights = [6,5,3,9,2,7] 输出：22 解释：我们移除一些砖块来形成 heights = [3,3,3,9,2,2]，峰值位于下标 3。 示例 3： 输入：maxHeights = [3,2,5,5,2,3] 输出：18 解释：我们移除一些砖块来形成 heights = [2,2,5,5,2,2]，峰值位于下标 2 或 3。 提示： * 1 <= n == heights.length <= 103 * 1 <= heights[i] <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用单调栈来计算每个位置作为峰值时的高度和。

算法步骤:
1. 计算每个位置作为峰值时左侧和右侧的高度和。
2. 使用单调栈分别从左到右和从右到左遍历数组，计算每个位置左侧和右侧的高度和。
3. 对于每个位置，计算其作为峰值时的高度和，并更新最大值。

关键点:
- 使用单调栈来维护左侧和右侧的高度和。
- 通过两次遍历来计算每个位置作为峰值时的高度和。
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


def solution_function_name(maxHeights: List[int]) -> int:
    """
    函数式接口 - 计算满足山脉状塔排列的高度和的最大值
    """
    n = len(maxHeights)
    left_sum = [0] * n
    right_sum = [0] * n
    stack = []

    # Calculate left sums
    for i in range(n):
        while stack and maxHeights[stack[-1]] > maxHeights[i]:
            stack.pop()
        if stack:
            left_sum[i] = left_sum[stack[-1]] + maxHeights[i] * (i - stack[-1])
        else:
            left_sum[i] = maxHeights[i] * (i + 1)
        stack.append(i)

    stack.clear()

    # Calculate right sums
    for i in range(n - 1, -1, -1):
        while stack and maxHeights[stack[-1]] > maxHeights[i]:
            stack.pop()
        if stack:
            right_sum[i] = right_sum[stack[-1]] + maxHeights[i] * (stack[-1] - i)
        else:
            right_sum[i] = maxHeights[i] * (n - i)
        stack.append(i)

    # Find the maximum sum
    max_sum = 0
    for i in range(n):
        max_sum = max(max_sum, left_sum[i] + right_sum[i] - maxHeights[i])

    return max_sum


Solution = create_solution(solution_function_name)