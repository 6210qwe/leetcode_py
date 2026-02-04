# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3113
标题: Beautiful Towers II
难度: medium
链接: https://leetcode.cn/problems/beautiful-towers-ii/
题目类型: 栈、数组、单调栈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2866. 美丽塔 II - 给你一个长度为 n 下标从 0 开始的整数数组 maxHeights 。 你的任务是在坐标轴上建 n 座塔。第 i 座塔的下标为 i ，高度为 heights[i] 。 如果以下条件满足，我们称这些塔是 美丽 的： 1. 1 <= heights[i] <= maxHeights[i] 2. heights 是一个 山脉 数组。 如果存在下标 i 满足以下条件，那么我们称数组 heights 是一个 山脉 数组： * 对于所有 0 < j <= i ，都有 heights[j - 1] <= heights[j] * 对于所有 i <= k < n - 1 ，都有 heights[k + 1] <= heights[k] 请你返回满足 美丽塔 要求的方案中，高度和的最大值 。 示例 1： 输入：maxHeights = [5,3,4,1,1] 输出：13 解释：和最大的美丽塔方案为 heights = [5,3,3,1,1] ，这是一个美丽塔方案，因为： - 1 <= heights[i] <= maxHeights[i] - heights 是个山脉数组，峰值在 i = 0 处。 13 是所有美丽塔方案中的最大高度和。 示例 2： 输入：maxHeights = [6,5,3,9,2,7] 输出：22 解释： 和最大的美丽塔方案为 heights = [3,3,3,9,2,2] ，这是一个美丽塔方案，因为： - 1 <= heights[i] <= maxHeights[i] - heights 是个山脉数组，峰值在 i = 3 处。 22 是所有美丽塔方案中的最大高度和。 示例 3： 输入：maxHeights = [3,2,5,5,2,3] 输出：18 解释：和最大的美丽塔方案为 heights = [2,2,5,5,2,2] ，这是一个美丽塔方案，因为： - 1 <= heights[i] <= maxHeights[i] - heights 是个山脉数组，最大值在 i = 2 处。 注意，在这个方案中，i = 3 也是一个峰值。 18 是所有美丽塔方案中的最大高度和。 提示： * 1 <= n == maxHeights <= 105 * 1 <= maxHeights[i] <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用单调栈来计算每个位置作为峰值时的高度和。

算法步骤:
1. 计算每个位置作为峰值时，左侧和右侧的高度和。
2. 使用单调栈来维护左侧和右侧的高度和。
3. 遍历每个位置，计算其作为峰值时的高度和，并更新最大值。

关键点:
- 使用单调栈来高效计算每个位置作为峰值时的高度和。
- 通过两次遍历分别计算左侧和右侧的高度和。
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


def beautiful_towers_ii(max_heights: List[int]) -> int:
    n = len(max_heights)
    left_sum = [0] * n
    right_sum = [0] * n
    stack = []

    # 计算左侧高度和
    for i in range(n):
        while stack and max_heights[stack[-1]] > max_heights[i]:
            stack.pop()
        if stack:
            left_sum[i] = left_sum[stack[-1]] + (i - stack[-1]) * max_heights[i]
        else:
            left_sum[i] = (i + 1) * max_heights[i]
        stack.append(i)

    stack.clear()

    # 计算右侧高度和
    for i in range(n - 1, -1, -1):
        while stack and max_heights[stack[-1]] > max_heights[i]:
            stack.pop()
        if stack:
            right_sum[i] = right_sum[stack[-1]] + (stack[-1] - i) * max_heights[i]
        else:
            right_sum[i] = (n - i) * max_heights[i]
        stack.append(i)

    # 计算最大高度和
    max_sum = 0
    for i in range(n):
        max_sum = max(max_sum, left_sum[i] + right_sum[i] - max_heights[i])

    return max_sum


Solution = create_solution(beautiful_towers_ii)