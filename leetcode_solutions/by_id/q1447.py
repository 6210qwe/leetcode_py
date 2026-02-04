# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1447
标题: Jump Game IV
难度: hard
链接: https://leetcode.cn/problems/jump-game-iv/
题目类型: 广度优先搜索、数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1345. 跳跃游戏 IV - 给你一个整数数组 arr ，你一开始在数组的第一个元素处（下标为 0）。 每一步，你可以从下标 i 跳到下标 i + 1 、i - 1 或者 j ： * i + 1 需满足：i + 1 < arr.length * i - 1 需满足：i - 1 >= 0 * j 需满足：arr[i] == arr[j] 且 i != j 请你返回到达数组最后一个元素的下标处所需的 最少操作次数 。 注意：任何时候你都不能跳到数组外面。 示例 1： 输入：arr = [100,-23,-23,404,100,23,23,23,3,404] 输出：3 解释：那你需要跳跃 3 次，下标依次为 0 --> 4 --> 3 --> 9 。下标 9 为数组的最后一个元素的下标。 示例 2： 输入：arr = [7] 输出：0 解释：一开始就在最后一个元素处，所以你不需要跳跃。 示例 3： 输入：arr = [7,6,9,6,9,6,9,7] 输出：1 解释：你可以直接从下标 0 处跳到下标 7 处，也就是数组的最后一个元素处。 提示： * 1 <= arr.length <= 5 * 104 * -108 <= arr[i] <= 108
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索 (BFS) 来找到从起始位置到目标位置的最短路径。

算法步骤:
1. 构建一个图，其中每个节点表示数组中的一个索引，边表示可以进行的跳跃。
2. 使用一个队列来进行 BFS，初始时将起始位置 (0) 放入队列。
3. 使用一个集合来记录已经访问过的节点，避免重复访问。
4. 对于队列中的每个节点，检查其所有可能的跳跃位置，如果到达目标位置则返回当前步数。
5. 如果队列为空且未到达目标位置，则返回 -1（但根据题目要求，这种情况不会发生）。

关键点:
- 使用字典来存储相同值的索引，以便快速查找可以跳跃的位置。
- 使用 BFS 确保找到的是最短路径。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组的长度。每个节点最多被访问一次。
空间复杂度: O(n)，用于存储图和队列。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_jumps(arr: List[int]) -> int:
    """
    函数式接口 - 返回到达数组最后一个元素的下标处所需的最少操作次数
    """
    if len(arr) <= 1:
        return 0

    # 构建图
    graph = {}
    for i, value in enumerate(arr):
        if value not in graph:
            graph[value] = []
        graph[value].append(i)

    # 初始化 BFS
    queue = [(0, 0)]  # (index, steps)
    visited = set([0])
    target = len(arr) - 1

    while queue:
        index, steps = queue.pop(0)
        if index == target:
            return steps

        # 跳到相邻位置
        for next_index in [index - 1, index + 1]:
            if 0 <= next_index < len(arr) and next_index not in visited:
                visited.add(next_index)
                queue.append((next_index, steps + 1))

        # 跳到相同值的位置
        if arr[index] in graph:
            for next_index in graph[arr[index]]:
                if next_index not in visited:
                    visited.add(next_index)
                    queue.append((next_index, steps + 1))

        # 清除已访问的值，避免重复处理
        graph[arr[index]] = []

    return -1  # 根据题目要求，这种情况不会发生


Solution = create_solution(min_jumps)