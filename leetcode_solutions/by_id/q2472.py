# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2472
标题: Build a Matrix With Conditions
难度: hard
链接: https://leetcode.cn/problems/build-a-matrix-with-conditions/
题目类型: 图、拓扑排序、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2392. 给定条件下构造矩阵 - 给你一个 正 整数 k ，同时给你： * 一个大小为 n 的二维整数数组 rowConditions ，其中 rowConditions[i] = [abovei, belowi] 和 * 一个大小为 m 的二维整数数组 colConditions ，其中 colConditions[i] = [lefti, righti] 。 两个数组里的整数都是 1 到 k 之间的数字。 你需要构造一个 k x k 的矩阵，1 到 k 每个数字需要 恰好出现一次 。剩余的数字都是 0 。 矩阵还需要满足以下条件： * 对于所有 0 到 n - 1 之间的下标 i ，数字 abovei 所在的 行 必须在数字 belowi 所在行的上面。 * 对于所有 0 到 m - 1 之间的下标 i ，数字 lefti 所在的 列 必须在数字 righti 所在列的左边。 返回满足上述要求的 任意 矩阵。如果不存在答案，返回一个空的矩阵。 示例 1： [https://assets.leetcode.com/uploads/2022/07/06/gridosdrawio.png] 输入：k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]] 输出：[[3,0,0],[0,0,1],[0,2,0]] 解释：上图为一个符合所有条件的矩阵。 行要求如下： - 数字 1 在第 1 行，数字 2 在第 2 行，1 在 2 的上面。 - 数字 3 在第 0 行，数字 2 在第 2 行，3 在 2 的上面。 列要求如下： - 数字 2 在第 1 列，数字 1 在第 2 列，2 在 1 的左边。 - 数字 3 在第 0 列，数字 2 在第 1 列，3 在 2 的左边。 注意，可能有多种正确的答案。 示例 2： 输入：k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]] 输出：[] 解释：由前两个条件可以得到 3 在 1 的下面，但第三个条件是 3 在 1 的上面。 没有符合条件的矩阵存在，所以我们返回空矩阵。 提示： * 2 <= k <= 400 * 1 <= rowConditions.length, colConditions.length <= 104 * rowConditions[i].length == colConditions[i].length == 2 * 1 <= abovei, belowi, lefti, righti <= k * abovei != belowi * lefti != righti
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用拓扑排序来确定行和列的顺序，然后根据这些顺序构建矩阵。

算法步骤:
1. 构建行和列的图，并计算每个节点的入度。
2. 使用拓扑排序确定行和列的顺序。
3. 如果拓扑排序失败（即存在环），则返回空矩阵。
4. 根据行和列的顺序构建矩阵。

关键点:
- 使用拓扑排序来确定行和列的顺序。
- 检查是否存在环。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(k + r + c)，其中 k 是矩阵的大小，r 是 rowConditions 的长度，c 是 colConditions 的长度。
空间复杂度: O(k + r + c)，用于存储图和入度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import defaultdict, deque

def build_matrix(k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
    def topological_sort(edges):
        graph = defaultdict(list)
        in_degree = [0] * (k + 1)
        
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        queue = deque([i for i in range(1, k + 1) if in_degree[i] == 0])
        order = []
        
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(order) < k:
            return []
        return order
    
    row_order = topological_sort(rowConditions)
    if not row_order:
        return []
    
    col_order = topological_sort(colConditions)
    if not col_order:
        return []
    
    matrix = [[0] * k for _ in range(k)]
    for num in range(1, k + 1):
        row_idx = row_order.index(num)
        col_idx = col_order.index(num)
        matrix[row_idx][col_idx] = num
    
    return matrix

Solution = create_solution(build_matrix)