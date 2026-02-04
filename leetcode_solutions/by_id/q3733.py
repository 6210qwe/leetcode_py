# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3733
标题: Length of Longest V-Shaped Diagonal Segment
难度: hard
链接: https://leetcode.cn/problems/length-of-longest-v-shaped-diagonal-segment/
题目类型: 记忆化搜索、数组、动态规划、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3459. 最长 V 形对角线段的长度 - 给你一个大小为 n x m 的二维整数矩阵 grid，其中每个元素的值为 0、1 或 2。 V 形对角线段 定义如下： * 线段从 1 开始。 * 后续元素按照以下无限序列的模式排列：2, 0, 2, 0, ...。 * 该线段： * 起始于某个对角方向（左上到右下、右下到左上、右上到左下或左下到右上）。 * 沿着相同的对角方向继续，保持 序列模式 。 * 在保持 序列模式 的前提下，最多允许 一次顺时针 90 度转向 另一个对角方向。 [https://pic.leetcode.cn/1739609732-jHpPma-length_of_longest3.jpg] 返回最长的 V 形对角线段 的 长度 。如果不存在有效的线段，则返回 0。 示例 1： 输入： grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]] 输出： 5 解释： [https://pic.leetcode.cn/1739609768-rhePxN-matrix_1-2.jpg] 最长的 V 形对角线段长度为 5，路径如下：(0,2) → (1,3) → (2,4)，在 (2,4) 处进行 顺时针 90 度转向 ，继续路径为 (3,3) → (4,2)。 示例 2： 输入： grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]] 输出： 4 解释： [https://pic.leetcode.cn/1739609774-nYJElV-matrix_2.jpg] 最长的 V 形对角线段长度为 4，路径如下：(2,3) → (3,2)，在 (3,2) 处进行 顺时针 90 度转向 ，继续路径为 (2,1) → (1,0)。 示例 3： 输入： grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]] 输出： 5 解释： [https://pic.leetcode.cn/1739609780-tlkdUW-matrix_3.jpg] 最长的 V 形对角线段长度为 5，路径如下：(0,0) → (1,1) → (2,2) → (3,3) → (4,4)。 示例 4： 输入： grid = [[1]] 输出： 1 解释： 最长的 V 形对角线段长度为 1，路径如下：(0,0)。 提示： * n == grid.length * m == grid[i].length * 1 <= n, m <= 500 * grid[i][j] 的值为 0、1 或 2。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用记忆化搜索来计算从每个起点出发的最长 V 形对角线段。

算法步骤:
1. 初始化一个记忆化表 `memo` 来存储从每个点出发的最长 V 形对角线段长度。
2. 定义一个递归函数 `dfs(x, y, direction)` 来计算从点 (x, y) 出发，沿着当前方向 `direction` 的最长 V 形对角线段长度。
3. 在递归函数中，检查当前点是否在边界内且满足 V 形对角线段的条件。如果满足，递归计算下一个点的长度，并更新最大长度。
4. 如果当前点是 1，可以尝试转向另一个方向，继续递归计算。
5. 遍历所有起点，调用递归函数并更新全局最大长度。

关键点:
- 使用记忆化搜索避免重复计算。
- 递归函数中处理边界条件和 V 形对角线段的模式。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)
空间复杂度: O(n * m)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def longest_v_shaped_diagonal(grid: List[List[int]]) -> int:
    if not grid or not grid[0]:
        return 0

    n, m = len(grid), len(grid[0])
    directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    memo = {}

    def dfs(x: int, y: int, direction: int) -> int:
        if (x, y, direction) in memo:
            return memo[(x, y, direction)]
        
        if x < 0 or x >= n or y < 0 or y >= m:
            return 0
        
        expected_value = 1 if (x + y) % 2 == 0 else 2
        if grid[x][y] != expected_value:
            return 0
        
        dx, dy = directions[direction]
        next_x, next_y = x + dx, y + dy
        length = 1 + dfs(next_x, next_y, direction)
        
        if grid[x][y] == 1:
            for new_direction in range(4):
                if new_direction != direction:
                    length = max(length, 1 + dfs(next_x, next_y, new_direction))
        
        memo[(x, y, direction)] = length
        return length

    max_length = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                for direction in range(4):
                    max_length = max(max_length, dfs(i, j, direction))
    
    return max_length

Solution = create_solution(longest_v_shaped_diagonal)