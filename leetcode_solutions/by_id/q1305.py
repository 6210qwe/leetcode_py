# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1305
标题: Number of Visible People in a Queue
难度: hard
链接: https://leetcode.cn/problems/number-of-visible-people-in-a-queue/
题目类型: 栈、数组、单调栈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1944. 队列中可以看到的人数 - 有 n 个人排成一个队列，从左到右 编号为 0 到 n - 1 。给你以一个整数数组 heights ，每个整数 互不相同，heights[i] 表示第 i 个人的高度。 一个人能 看到 他右边另一个人的条件是这两人之间的所有人都比他们两人 矮 。更正式的，第 i 个人能看到第 j 个人的条件是 i < j 且 min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]) 。 请你返回一个长度为 n 的数组 answer ，其中 answer[i] 是第 i 个人在他右侧队列中能 看到 的 人数 。 示例 1： [https://assets.leetcode.com/uploads/2021/05/29/queue-plane.jpg] 输入：heights = [10,6,8,5,11,9] 输出：[3,1,2,1,1,0] 解释： 第 0 个人能看到编号为 1 ，2 和 4 的人。 第 1 个人能看到编号为 2 的人。 第 2 个人能看到编号为 3 和 4 的人。 第 3 个人能看到编号为 4 的人。 第 4 个人能看到编号为 5 的人。 第 5 个人谁也看不到因为他右边没人。 示例 2： 输入：heights = [5,1,2,3,10] 输出：[4,1,1,1,0] 提示： * n == heights.length * 1 <= n <= 105 * 1 <= heights[i] <= 105 * heights 中所有数 互不相同 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用单调栈来维护从右到左的递减高度序列。

算法步骤:
1. 初始化结果数组 `answer` 为全 0。
2. 从右向左遍历 `heights` 数组，使用一个栈 `stack` 来维护当前可见的递减高度序列。
3. 对于每个高度 `heights[i]`，弹出栈中所有小于 `heights[i]` 的高度，并记录弹出次数作为 `answer[i]` 的值。
4. 如果栈非空，则 `answer[i]` 再加 1（表示能看到栈顶元素）。
5. 将当前高度 `heights[i]` 压入栈中。

关键点:
- 使用单调栈来维护从右到左的递减高度序列，确保每次弹出的都是当前可见的最矮高度。
- 通过记录弹出次数来计算每个人能看到的人数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 heights 的长度。每个元素最多被压入和弹出栈一次。
空间复杂度: O(n)，栈的最大空间复杂度为 O(n)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def number_of_visible_people(heights: List[int]) -> List[int]:
    """
    返回一个长度为 n 的数组 answer，其中 answer[i] 是第 i 个人在他右侧队列中能看到的人数。
    """
    n = len(heights)
    answer = [0] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] < heights[i]:
            stack.pop()
            answer[i] += 1
        if stack:
            answer[i] += 1
        stack.append(heights[i])

    return answer


Solution = create_solution(number_of_visible_people)