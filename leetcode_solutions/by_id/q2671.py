# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2671
标题: Shortest Cycle in a Graph
难度: hard
链接: https://leetcode.cn/problems/shortest-cycle-in-a-graph/
题目类型: 广度优先搜索、图
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2608. 图中的最短环 - 现有一个含 n 个顶点的 双向 图，每个顶点按从 0 到 n - 1 标记。图中的边由二维整数数组 edges 表示，其中 edges[i] = [ui, vi] 表示顶点 ui 和 vi 之间存在一条边。每对顶点最多通过一条边连接，并且不存在与自身相连的顶点。 返回图中 最短 环的长度。如果不存在环，则返回 -1 。 环 是指以同一节点开始和结束，并且路径中的每条边仅使用一次。 示例 1： [https://assets.leetcode.com/uploads/2023/01/04/cropped.png] 输入：n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]] 输出：3 解释：长度最小的循环是：0 -> 1 -> 2 -> 0 示例 2： [https://assets.leetcode.com/uploads/2023/01/04/croppedagin.png] 输入：n = 4, edges = [[0,1],[0,2]] 输出：-1 解释：图中不存在循环 提示： * 2 <= n <= 1000 * 1 <= edges.length <= 1000 * edges[i].length == 2 * 0 <= ui, vi < n * ui != vi * 不存在重复的边
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）从每个节点出发，寻找最短环。

算法步骤:
1. 构建邻接表表示图。
2. 对于每个节点，使用 BFS 寻找从该节点出发的最短环。
3. 记录并更新最短环的长度。
4. 如果所有节点都遍历完毕且没有找到环，返回 -1。

关键点:
- 使用一个队列进行 BFS 遍历。
- 使用一个集合记录访问过的节点，避免重复访问。
- 通过记录当前路径长度来判断是否形成环。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * (n + m))，其中 n 是节点数，m 是边数。每个节点都需要进行一次 BFS。
空间复杂度: O(n + m)，用于存储图的邻接表和 BFS 的辅助数据结构。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_shortest_cycle(n: int, edges: List[List[int]]) -> int:
    """
    函数式接口 - 寻找图中的最短环
    """
    # 构建邻接表
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def bfs(start: int) -> int:
        queue = [(start, -1, 0)]  # (当前节点, 父节点, 当前路径长度)
        visited = set()
        visited.add(start)
        
        while queue:
            node, parent, length = queue.pop(0)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, node, length + 1))
                elif neighbor != parent:
                    return length + 1
        return float('inf')

    min_cycle = float('inf')
    for i in range(n):
        min_cycle = min(min_cycle, bfs(i))

    return min_cycle if min_cycle != float('inf') else -1


Solution = create_solution(find_shortest_cycle)