# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1663
标题: Detect Cycles in 2D Grid
难度: medium
链接: https://leetcode.cn/problems/detect-cycles-in-2d-grid/
题目类型: 深度优先搜索、广度优先搜索、并查集、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1559. 二维网格图中探测环 - 给你一个二维字符网格数组 grid ，大小为 m x n ，你需要检查 grid 中是否存在 相同值 形成的环。 一个环是一条开始和结束于同一个格子的长度 大于等于 4 的路径。对于一个给定的格子，你可以移动到它上、下、左、右四个方向相邻的格子之一，可以移动的前提是这两个格子有 相同的值 。 同时，你也不能回到上一次移动时所在的格子。比方说，环 (1, 1) -> (1, 2) -> (1, 1) 是不合法的，因为从 (1, 2) 移动到 (1, 1) 回到了上一次移动时的格子。 如果 grid 中有相同值形成的环，请你返回 true ，否则返回 false 。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/08/22/5482e1.png] 输入：grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]] 输出：true 解释：如下图所示，有 2 个用不同颜色标出来的环： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/08/22/5482e11.png] 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/08/22/5482e2.png] 输入：grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]] 输出：true 解释：如下图所示，只有高亮所示的一个合法环： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/08/22/5482e22.png] 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/08/22/5482e3.png] 输入：grid = [["a","b","b"],["b","z","b"],["b","b","a"]] 输出：false 提示： * m == grid.length * n == grid[i].length * 1 <= m <= 500 * 1 <= n <= 500 * grid 只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）来检测环。我们使用一个访问标记数组 `visited` 来记录每个节点的状态：0 表示未访问，1 表示正在访问，2 表示已访问。如果在 DFS 过程中遇到正在访问的节点，则说明存在环。

算法步骤:
1. 初始化一个与 `grid` 大小相同的 `visited` 数组，所有元素初始化为 0。
2. 遍历 `grid` 中的每个节点，如果该节点未被访问过，则调用 DFS 函数进行深度优先搜索。
3. 在 DFS 函数中，标记当前节点为正在访问（1），然后递归访问其四个方向的邻居节点。
4. 如果在递归过程中遇到正在访问的节点，则说明存在环，返回 `True`。
5. 如果递归结束后没有发现环，则将当前节点标记为已访问（2）。
6. 如果遍历完所有节点后没有发现环，则返回 `False`。

关键点:
- 使用 `visited` 数组来避免重复访问和检测环。
- 递归过程中需要传递前一个节点的位置，以避免回退到上一个节点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 和 n 分别是 `grid` 的行数和列数。每个节点最多访问两次。
空间复杂度: O(m * n)，最坏情况下递归栈的深度为 m * n。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def contains_cycle(grid: List[List[str]]) -> bool:
    def dfs(x: int, y: int, prev_x: int, prev_y: int) -> bool:
        if visited[x][y] == 1:
            return True
        if visited[x][y] == 2:
            return False
        
        visited[x][y] = 1
        for dx, dy in directions:
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < m and 0 <= next_y < n and grid[next_x][next_y] == grid[x][y] and (next_x, next_y) != (prev_x, prev_y):
                if dfs(next_x, next_y, x, y):
                    return True
        visited[x][y] = 2
        return False
    
    m, n = len(grid), len(grid[0])
    visited = [[0] * n for _ in range(m)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for i in range(m):
        for j in range(n):
            if visited[i][j] == 0:
                if dfs(i, j, -1, -1):
                    return True
    return False

Solution = create_solution(contains_cycle)