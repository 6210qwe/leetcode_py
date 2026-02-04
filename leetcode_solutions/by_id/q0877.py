# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 877
标题: Shortest Path Visiting All Nodes
难度: hard
链接: https://leetcode.cn/problems/shortest-path-visiting-all-nodes/
题目类型: 位运算、广度优先搜索、图、动态规划、状态压缩
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
847. 访问所有节点的最短路径 - 存在一个由 n 个节点组成的无向连通图，图中的节点按从 0 到 n - 1 编号。 给你一个数组 graph 表示这个图。其中，graph[i] 是一个列表，由所有与节点 i 直接相连的节点组成。 返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。 示例 1： [https://assets.leetcode.com/uploads/2021/05/12/shortest1-graph.jpg] 输入：graph = [[1,2,3],[0],[0],[0]] 输出：4 解释：一种可能的路径为 [1,0,2,0,3] 示例 2： [https://assets.leetcode.com/uploads/2021/05/12/shortest2-graph.jpg] 输入：graph = [[1],[0,2,4],[1,3,4],[2],[1,2]] 输出：4 解释：一种可能的路径为 [0,1,4,2,3] 提示： * n == graph.length * 1 <= n <= 12 * 0 <= graph[i].length < n * graph[i] 不包含 i * 如果 graph[a] 包含 b ，那么 graph[b] 也包含 a * 输入的图总是连通图
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）结合状态压缩来找到最短路径。

算法步骤:
1. 初始化队列和访问集合，队列中存储 (当前节点, 当前状态, 当前步数)。
2. 状态使用位掩码表示，每个节点是否被访问过。
3. 对于每个节点，如果所有节点都被访问过，则返回当前步数。
4. 否则，将当前节点的所有邻居节点加入队列，并更新状态和步数。
5. 重复上述过程直到找到最短路径。

关键点:
- 使用位掩码来表示节点的访问状态。
- 使用 BFS 来确保找到的路径是最短的。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^n * n^2)，其中 n 是节点数。每个状态有 2^n 种可能，每种状态下最多需要处理 n 个节点。
空间复杂度: O(2^n * n)，用于存储状态和队列。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def shortest_path_length(graph: List[List[int]]) -> int:
    """
    函数式接口 - 返回能够访问所有节点的最短路径的长度
    """
    n = len(graph)
    all_visited = (1 << n) - 1  # 所有节点都访问过的状态
    queue = [(i, 1 << i, 0) for i in range(n)]  # (当前节点, 当前状态, 当前步数)
    visited = set(queue)

    while queue:
        node, state, steps = queue.pop(0)
        if state == all_visited:
            return steps
        for neighbor in graph[node]:
            new_state = state | (1 << neighbor)
            if (neighbor, new_state) not in visited:
                visited.add((neighbor, new_state))
                queue.append((neighbor, new_state, steps + 1))

Solution = create_solution(shortest_path_length)