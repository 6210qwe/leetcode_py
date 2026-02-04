# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2914
标题: Find the Safest Path in a Grid
难度: medium
链接: https://leetcode.cn/problems/find-the-safest-path-in-a-grid/
题目类型: 广度优先搜索、并查集、数组、二分查找、矩阵、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2812. 找出最安全路径 - 给你一个下标从 0 开始、大小为 n x n 的二维矩阵 grid ，其中 (r, c) 表示： * 如果 grid[r][c] = 1 ，则表示一个存在小偷的单元格 * 如果 grid[r][c] = 0 ，则表示一个空单元格 你最开始位于单元格 (0, 0) 。在一步移动中，你可以移动到矩阵中的任一相邻单元格，包括存在小偷的单元格。 矩阵中路径的 安全系数 定义为：从路径中任一单元格到矩阵中任一小偷所在单元格的 最小 曼哈顿距离。 返回所有通向单元格 (n - 1, n - 1) 的路径中的 最大安全系数 。 单元格 (r, c) 的某个 相邻 单元格，是指在矩阵中存在的 (r, c + 1)、(r, c - 1)、(r + 1, c) 和 (r - 1, c) 之一。 两个单元格 (a, b) 和 (x, y) 之间的 曼哈顿距离 等于 | a - x | + | b - y | ，其中 |val| 表示 val 的绝对值。 示例 1： [https://assets.leetcode.com/uploads/2023/07/02/example1.png] 输入：grid = [[1,0,0],[0,0,0],[0,0,1]] 输出：0 解释：从 (0, 0) 到 (n - 1, n - 1) 的每条路径都经过存在小偷的单元格 (0, 0) 和 (n - 1, n - 1) 。 示例 2： [https://assets.leetcode.com/uploads/2023/07/02/example2.png] 输入：grid = [[0,0,1],[0,0,0],[0,0,0]] 输出：2 解释： 上图所示路径的安全系数为 2： - 该路径上距离小偷所在单元格（0，2）最近的单元格是（0，0）。它们之间的曼哈顿距离为 | 0 - 0 | + | 0 - 2 | = 2 。 可以证明，不存在安全系数更高的其他路径。 示例 3： [https://assets.leetcode.com/uploads/2023/07/02/example3.png] 输入：grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]] 输出：2 解释： 上图所示路径的安全系数为 2： - 该路径上距离小偷所在单元格（0，3）最近的单元格是（1，2）。它们之间的曼哈顿距离为 | 0 - 1 | + | 3 - 2 | = 2 。 - 该路径上距离小偷所在单元格（3，0）最近的单元格是（3，2）。它们之间的曼哈顿距离为 | 3 - 3 | + | 0 - 2 | = 2 。 可以证明，不存在安全系数更高的其他路径。 提示： * 1 <= grid.length == n <= 400 * grid[i].length == n * grid[i][j] 为 0 或 1 * grid 至少存在一个小偷
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索 (BFS) 计算每个单元格到最近的小偷的距离，然后使用二分查找和并查集来找到最大安全系数。

算法步骤:
1. 使用 BFS 计算每个单元格到最近的小偷的距离。
2. 使用二分查找确定最大安全系数的可能值。
3. 对于每个可能的安全系数，使用并查集检查是否存在一条路径满足条件。

关键点:
- 使用 BFS 计算每个单元格到最近的小偷的距离。
- 使用二分查找和并查集来找到最大安全系数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 log n)，其中 n 是网格的边长。BFS 的时间复杂度是 O(n^2)，二分查找的时间复杂度是 O(log n)，每次并查集操作的时间复杂度是 O(n^2)。
空间复杂度: O(n^2)，用于存储每个单元格到最近的小偷的距离以及并查集的数据结构。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
from collections import deque
from typing import Tuple

def find_safest_path(grid: List[List[int]]) -> int:
    n = len(grid)
    distances = [[float('inf')] * n for _ in range(n)]
    
    # Step 1: Calculate the distance to the nearest thief using BFS
    queue = deque()
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                distances[r][c] = 0
                queue.append((r, c))
    
    while queue:
        r, c = queue.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and distances[nr][nc] > distances[r][c] + 1:
                distances[nr][nc] = distances[r][c] + 1
                queue.append((nr, nc))
    
    # Step 2: Use binary search to find the maximum safety factor
    def can_reach_end(safety_factor: int) -> bool:
        parent = list(range(n * n))
        
        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x: int, y: int) -> None:
            parent[find(x)] = find(y)
        
        for r in range(n):
            for c in range(n):
                if distances[r][c] >= safety_factor:
                    index = r * n + c
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and distances[nr][nc] >= safety_factor:
                            neighbor_index = nr * n + nc
                            union(index, neighbor_index)
        
        return find(0) == find(n * n - 1)
    
    left, right = 0, n * 2
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if can_reach_end(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result

Solution = create_solution(find_safest_path)