# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2121
标题: Find if Path Exists in Graph
难度: easy
链接: https://leetcode.cn/problems/find-if-path-exists-in-graph/
题目类型: 深度优先搜索、广度优先搜索、并查集、图
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1971. 寻找图中是否存在路径 - 有一个具有 n 个顶点的 双向 图，其中每个顶点标记从 0 到 n - 1（包含 0 和 n - 1）。图中的边用一个二维整数数组 edges 表示，其中 edges[i] = [ui, vi] 表示顶点 ui 和顶点 vi 之间的双向边。 每个顶点对由 最多一条 边连接，并且没有顶点存在与自身相连的边。 请你确定是否存在从顶点 source 开始，到顶点 destination 结束的 有效路径 。 给你数组 edges 和整数 n、source 和 destination，如果从 source 到 destination 存在 有效路径 ，则返回 true，否则返回 false 。 示例 1： [https://assets.leetcode.com/uploads/2021/08/14/validpath-ex1.png] 输入：n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2 输出：true 解释：存在由顶点 0 到顶点 2 的路径: - 0 → 1 → 2 - 0 → 2 示例 2： [https://assets.leetcode.com/uploads/2021/08/14/validpath-ex2.png] 输入：n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5 输出：false 解释：不存在由顶点 0 到顶点 5 的路径. 提示： * 1 <= n <= 2 * 105 * 0 <= edges.length <= 2 * 105 * edges[i].length == 2 * 0 <= ui, vi <= n - 1 * ui != vi * 0 <= source, destination <= n - 1 * 不存在重复边 * 不存在指向顶点自身的边
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来判断两个顶点是否连通

算法步骤:
1. 初始化并查集
2. 遍历所有边，将每条边的两个顶点进行合并
3. 检查源顶点和目标顶点是否在同一个集合中

关键点:
- 并查集的路径压缩和按秩合并可以优化查询和合并操作的时间复杂度
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(E * α(n))，其中 E 是边的数量，α 是阿克曼函数的反函数，近似为常数
空间复杂度: O(n)，用于存储并查集的数据结构
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def solution_function_name(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    """
    函数式接口 - 使用并查集判断两个顶点是否连通
    """
    if source == destination:
        return True

    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)

    return uf.find(source) == uf.find(destination)

Solution = create_solution(solution_function_name)