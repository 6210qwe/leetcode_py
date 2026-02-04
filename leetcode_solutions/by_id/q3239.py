# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3239
标题: Minimum Number of Operations to Make X and Y Equal
难度: medium
链接: https://leetcode.cn/problems/minimum-number-of-operations-to-make-x-and-y-equal/
题目类型: 广度优先搜索、记忆化搜索、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2998. 使 X 和 Y 相等的最少操作次数 - 给你两个正整数 x 和 y 。 一次操作中，你可以执行以下四种操作之一： 1. 如果 x 是 11 的倍数，将 x 除以 11 。 2. 如果 x 是 5 的倍数，将 x 除以 5 。 3. 将 x 减 1 。 4. 将 x 加 1 。 请你返回让 x 和 y 相等的 最少 操作次数。 示例 1： 输入：x = 26, y = 1 输出：3 解释：我们可以通过以下操作将 26 变为 1 ： 1. 将 x 减 1 2. 将 x 除以 5 3. 将 x 除以 5 将 26 变为 1 最少需要 3 次操作。 示例 2： 输入：x = 54, y = 2 输出：4 解释：我们可以通过以下操作将 54 变为 2 ： 1. 将 x 加 1 2. 将 x 除以 11 3. 将 x 除以 5 4. 将 x 加 1 将 54 变为 2 最少需要 4 次操作。 示例 3： 输入：x = 25, y = 30 输出：5 解释：我们可以通过以下操作将 25 变为 30 ： 1. 将 x 加 1 2. 将 x 加 1 3. 将 x 加 1 4. 将 x 加 1 5. 将 x 加 1 将 25 变为 30 最少需要 5 次操作。 提示： * 1 <= x, y <= 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）来找到从 x 到 y 的最短路径。通过队列来存储当前状态和操作次数，并使用集合来避免重复计算。

算法步骤:
1. 初始化队列和访问集合。
2. 开始 BFS 循环：
   - 从队列中取出当前状态和操作次数。
   - 如果当前状态等于 y，返回操作次数。
   - 否则，生成所有可能的下一个状态并加入队列。
3. 返回操作次数。

关键点:
- 使用 BFS 来保证找到最短路径。
- 使用集合来避免重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 x 和 y 之间的差值。在最坏情况下，我们需要遍历所有可能的状态。
空间复杂度: O(n)，队列和访问集合的空间复杂度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_operations_to_make_equal(x: int, y: int) -> int:
    """
    函数式接口 - 返回使 x 和 y 相等的最少操作次数
    """
    from collections import deque

    # 初始化队列和访问集合
    queue = deque([(x, 0)])
    visited = set([x])

    while queue:
        current, steps = queue.popleft()

        if current == y:
            return steps

        # 生成所有可能的下一个状态
        next_states = [
            (current // 11, steps + 1) if current % 11 == 0 else (current, steps),
            (current // 5, steps + 1) if current % 5 == 0 else (current, steps),
            (current - 1, steps + 1),
            (current + 1, steps + 1)
        ]

        for next_state, next_steps in next_states:
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, next_steps))

    return -1  # 理论上不会到达这里


Solution = create_solution(min_operations_to_make_equal)