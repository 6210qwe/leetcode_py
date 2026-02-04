# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1257
标题: Rank Transform of a Matrix
难度: hard
链接: https://leetcode.cn/problems/rank-transform-of-a-matrix/
题目类型: 并查集、图、拓扑排序、数组、矩阵、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1632. 矩阵转换后的排名 - 给你一个 m x n 的矩阵 matrix ，请你返回一个新的矩阵 answer ，其中 answer[row][col] 是 matrix[row][col] 的排名。 每个元素的 排名 是一个整数，表示这个元素相对于其他元素的大小关系，它按照如下规则计算： * 排名是从 1 开始的一个整数。 * 如果两个元素 p 和 q 在 同一行 或者 同一列 ，那么： * 如果 p < q ，那么 rank(p) < rank(q) * 如果 p == q ，那么 rank(p) == rank(q) * 如果 p > q ，那么 rank(p) > rank(q) * 排名 需要越 小 越好。 题目保证按照上面规则 answer 数组是唯一的。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/10/25/rank1.jpg] 输入：matrix = [[1,2],[3,4]] 输出：[[1,2],[2,3]] 解释： matrix[0][0] 的排名为 1 ，因为它是所在行和列的最小整数。 matrix[0][1] 的排名为 2 ，因为 matrix[0][1] > matrix[0][0] 且 matrix[0][0] 的排名为 1 。 matrix[1][0] 的排名为 2 ，因为 matrix[1][0] > matrix[0][0] 且 matrix[0][0] 的排名为 1 。 matrix[1][1] 的排名为 3 ，因为 matrix[1][1] > matrix[0][1]， matrix[1][1] > matrix[1][0] 且 matrix[0][1] 和 matrix[1][0] 的排名都为 2 。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/10/25/rank2.jpg] 输入：matrix = [[7,7],[7,7]] 输出：[[1,1],[1,1]] 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/10/25/rank3.jpg] 输入：matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]] 输出：[[4,2,3],[1,3,4],[5,1,6],[1,3,4]] 提示： * m == matrix.length * n == matrix[i].length * 1 <= m, n <= 500 * -109 <= matrix[row][col] <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来处理同一行或同一列中相同值的连通性，并使用拓扑排序来确定每个元素的排名。

算法步骤:
1. 构建一个二维数组 `values` 来存储每个位置的值及其坐标。
2. 对 `values` 进行排序，按值从小到大排序。
3. 使用并查集来处理同一行或同一列中相同值的连通性。
4. 构建一个有向图，表示节点之间的相对大小关系。
5. 使用拓扑排序来确定每个元素的排名。

关键点:
- 使用并查集来处理同一行或同一列中相同值的连通性。
- 使用拓扑排序来确定每个元素的排名。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n * log(m * n))，其中 m 和 n 分别是矩阵的行数和列数。排序操作的时间复杂度为 O(m * n * log(m * n))，并查集和拓扑排序的时间复杂度为 O(m * n)。
空间复杂度: O(m * n)，用于存储并查集、图和队列等数据结构。
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


def solution_function_name(matrix: List[List[int]]) -> List[List[int]]:
    """
    函数式接口 - 返回矩阵转换后的排名
    """
    m, n = len(matrix), len(matrix[0])
    values = [(val, i, j) for i, row in enumerate(matrix) for j, val in enumerate(row)]
    values.sort()

    uf = UnionFind(m * n)
    graph = [[] for _ in range(m * n)]
    in_degree = [0] * (m * n)

    for k in range(len(values)):
        val, i, j = values[k]
        index = i * n + j
        if k > 0 and val == values[k - 1][0]:
            prev_val, prev_i, prev_j = values[k - 1]
            prev_index = prev_i * n + prev_j
            if i == prev_i or j == prev_j:
                uf.union(index, prev_index)

    for k in range(len(values)):
        val, i, j = values[k]
        index = i * n + j
        if k > 0 and val != values[k - 1][0]:
            for l in range(k):
                prev_val, prev_i, prev_j = values[l]
                prev_index = prev_i * n + prev_j
                if i == prev_i or j == prev_j:
                    root_index = uf.find(index)
                    root_prev_index = uf.find(prev_index)
                    if root_index != root_prev_index:
                        graph[root_prev_index].append(root_index)
                        in_degree[root_index] += 1

    queue = [i for i in range(m * n) if in_degree[i] == 0]
    ranks = [0] * (m * n)
    rank = 1

    while queue:
        new_queue = []
        for node in queue:
            ranks[node] = rank
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    new_queue.append(neighbor)
        queue = new_queue
        rank += 1

    result = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            index = i * n + j
            result[i][j] = ranks[uf.find(index)]

    return result


Solution = create_solution(solution_function_name)