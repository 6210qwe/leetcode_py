# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1409
标题: Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
难度: hard
链接: https://leetcode.cn/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/
题目类型: 位运算、广度优先搜索、数组、哈希表、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1284. 转化为全零矩阵的最少反转次数 - 给你一个 m x n 的二进制矩阵 mat。每一步，你可以选择一个单元格并将它反转（反转表示 0 变 1 ，1 变 0 ）。如果存在和它相邻的单元格，那么这些相邻的单元格也会被反转。相邻的两个单元格共享同一条边。 请你返回将矩阵 mat 转化为全零矩阵的最少反转次数，如果无法转化为全零矩阵，请返回 -1 。 二进制矩阵 的每一个格子要么是 0 要么是 1 。 全零矩阵 是所有格子都为 0 的矩阵。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/12/13/matrix.png] 输入：mat = [[0,0],[0,1]] 输出：3 解释：一个可能的解是反转 (1, 0)，然后 (0, 1) ，最后是 (1, 1) 。 示例 2： 输入：mat = [[0]] 输出：0 解释：给出的矩阵是全零矩阵，所以你不需要改变它。 示例 3： 输入：mat = [[1,0,0],[1,0,0]] 输出：-1 解释：该矩阵无法转变成全零矩阵 提示： * m == mat.length * n == mat[0].length * 1 <= m <= 3 * 1 <= n <= 3 * mat[i][j] 是 0 或 1 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）来找到从初始状态到全零矩阵的最短路径。

算法步骤:
1. 将矩阵转换为一个整数表示的状态，以便在 BFS 中使用。
2. 初始化 BFS 队列，队列中的每个元素是一个元组 (state, steps)，其中 state 是当前矩阵的状态，steps 是到达该状态所需的步数。
3. 使用一个集合 visited 来记录已经访问过的状态，避免重复访问。
4. 在 BFS 过程中，对于每个状态，尝试翻转每个单元格及其相邻单元格，生成新的状态。
5. 如果新状态是全零矩阵，返回当前步数加一。
6. 如果 BFS 队列为空且没有找到全零矩阵，返回 -1。

关键点:
- 使用位运算来表示和操作矩阵状态。
- 使用 BFS 来找到最短路径。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^(m*n) * m * n)，其中 m 和 n 分别是矩阵的行数和列数。因为每个状态最多有 m * n 种翻转方式。
空间复杂度: O(2^(m*n))，用于存储 BFS 队列和 visited 集合。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_flips(mat: List[List[int]]) -> int:
    """
    函数式接口 - 返回将矩阵 mat 转化为全零矩阵的最少反转次数，如果无法转化为全零矩阵，返回 -1。
    """
    m, n = len(mat), len(mat[0])
    target = 0
    start = 0
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                start |= 1 << (i * n + j)
    
    def flip(state, i, j):
        new_state = state
        for di, dj in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n:
                pos = ni * n + nj
                new_state ^= 1 << pos
        return new_state
    
    from collections import deque
    queue = deque([(start, 0)])
    visited = set([start])
    
    while queue:
        state, steps = queue.popleft()
        if state == target:
            return steps
        for i in range(m):
            for j in range(n):
                new_state = flip(state, i, j)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, steps + 1))
    
    return -1


Solution = create_solution(min_flips)