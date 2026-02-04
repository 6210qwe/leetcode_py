# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2056
标题: Jump Game VIII
难度: medium
链接: https://leetcode.cn/problems/jump-game-viii/
题目类型: 栈、图、数组、动态规划、最短路、单调栈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2297. 跳跃游戏 VIII - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）来找到从起点到终点的最短路径。

算法步骤:
1. 初始化一个队列，将起点加入队列，并标记为已访问。
2. 使用一个集合来记录已经访问过的节点，避免重复访问。
3. 开始广度优先搜索：
   - 从队列中取出一个节点。
   - 检查该节点是否是终点，如果是则返回 True。
   - 否则，遍历该节点的所有可能跳跃位置，如果未访问过且在数组范围内，则将其加入队列并标记为已访问。
4. 如果队列为空且未找到终点，则返回 False。

关键点:
- 使用 BFS 可以确保找到的路径是最短的。
- 使用集合来记录已访问的节点，避免重复访问。
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


def can_reach_end(arr: List[int]) -> bool:
    """
    判断是否可以从数组的第一个元素跳跃到最后一个元素。

    :param arr: 整数数组
    :return: 是否可以到达最后一个元素
    """
    n = len(arr)
    if n == 1:
        return True

    visited = set()
    queue = [0]
    visited.add(0)

    while queue:
        current = queue.pop(0)
        if current == n - 1:
            return True

        # 计算可以跳跃的位置
        jump_distance = arr[current]
        for next_pos in [current + jump_distance, current - jump_distance]:
            if 0 <= next_pos < n and next_pos not in visited:
                visited.add(next_pos)
                queue.append(next_pos)

    return False


Solution = create_solution(can_reach_end)