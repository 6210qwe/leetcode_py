# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2439
标题: Longest Cycle in a Graph
难度: hard
链接: https://leetcode.cn/problems/longest-cycle-in-a-graph/
题目类型: 深度优先搜索、广度优先搜索、图、拓扑排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2360. 图中的最长环 - 给你一个 n 个节点的 有向图 ，节点编号为 0 到 n - 1 ，其中每个节点 至多 有一条出边。 图用一个大小为 n 下标从 0 开始的数组 edges 表示，节点 i 到节点 edges[i] 之间有一条有向边。如果节点 i 没有出边，那么 edges[i] == -1 。 请你返回图中的 最长 环，如果没有任何环，请返回 -1 。 一个环指的是起点和终点是 同一个 节点的路径。 示例 1： [https://assets.leetcode.com/uploads/2022/06/08/graph4drawio-5.png] 输入：edges = [3,3,4,2,3] 输出去：3 解释：图中的最长环是：2 -> 4 -> 3 -> 2 。 这个环的长度为 3 ，所以返回 3 。 示例 2： [https://assets.leetcode.com/uploads/2022/06/07/graph4drawio-1.png] 输入：edges = [2,-1,3,1] 输出：-1 解释：图中没有任何环。 提示： * n == edges.length * 2 <= n <= 105 * -1 <= edges[i] < n * edges[i] != i
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）来检测图中的环，并记录最长的环。

算法步骤:
1. 初始化一个访问数组 `visited` 和一个递归栈数组 `rec_stack`。
2. 遍历每个节点，如果该节点未被访问过，则进行 DFS。
3. 在 DFS 中，标记当前节点为已访问，并将其加入递归栈。
4. 如果当前节点的下一个节点已经存在于递归栈中，则找到了一个环，更新最长环的长度。
5. 如果当前节点的下一个节点未被访问过，则继续进行 DFS。
6. 递归返回时，将当前节点从递归栈中移除。
7. 返回最长环的长度。

关键点:
- 使用递归栈来检测环。
- 记录并更新最长环的长度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 每个节点最多访问一次。
空间复杂度: O(n) - 用于存储访问数组和递归栈。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def longest_cycle(edges: List[int]) -> int:
    def dfs(node: int, visited: List[bool], rec_stack: List[bool], length: int) -> None:
        if visited[node]:
            return
        visited[node] = True
        rec_stack[node] = True
        next_node = edges[node]
        if next_node != -1:
            if rec_stack[next_node]:
                nonlocal max_length
                max_length = max(max_length, length)
            elif not visited[next_node]:
                dfs(next_node, visited, rec_stack, length + 1)
        rec_stack[node] = False

    n = len(edges)
    visited = [False] * n
    rec_stack = [False] * n
    max_length = -1

    for i in range(n):
        if not visited[i]:
            dfs(i, visited, rec_stack, 1)

    return max_length


Solution = create_solution(longest_cycle)