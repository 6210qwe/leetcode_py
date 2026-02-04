# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000227
标题: 主题空间
难度: medium
链接: https://leetcode.cn/problems/YesdPw/
题目类型: 深度优先搜索、广度优先搜索、并查集、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCS 03. 主题空间 - 「以扣会友」线下活动所在场地由若干主题空间与走廊组成，场地的地图记作由一维字符串型数组 `grid`，字符串中仅包含 `"0"～"5"` 这 6 个字符。地图上每一个字符代表面积为 1 的区域，其中 `"0"` 表示走廊，其他字符表示主题空间。相同且连续（连续指上、下、左、右四个方向连接）的字符组成同一个主题空间。 假如整个 `grid` 区域的外侧均为走廊。请问，不与走廊直接相邻的主题空间的最大面积是多少？如果不存在这样的空间请返回 `0`。 **示例 1：** >输入：`grid = ["110","231","221"]` > >输出：`1` > >解释：4 个主题空间中，只有 1 个不与走廊相邻，面积为 1。 >![image.png](https://pic.leetcode.cn/1613708145-rscctN-image.png) **示例 2：** >输入：`grid = ["11111100000","21243101111","21224101221","11111101111"]` > >输出：`3` > >解释：8 个主题空间中，有 5 个不与走廊相邻，面积分别为 3、1、1、1、2，最大面积为 3。 >![image.png](https://pic.leetcode.cn/1613707985-KJyiXJ-image.png) **提示：** - `1 <= grid.length <= 500` - `1 <= grid[i].length <= 500` - `grid[i][j]` 仅可能为 `"0"～"5"`
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来遍历每个主题空间，并记录其面积。在遍历过程中，如果发现该主题空间与走廊相邻，则标记为无效。

算法步骤:
1. 初始化一个二维布尔数组 `visited`，用于记录每个位置是否被访问过。
2. 定义一个递归函数 `dfs`，用于计算从某个位置出发的主题空间的面积，并标记是否与走廊相邻。
3. 遍历整个 `grid`，对于每个未访问过的非走廊位置，调用 `dfs` 计算其面积，并更新最大面积。
4. 返回最大面积。

关键点:
- 使用 `visited` 数组避免重复访问。
- 在 `dfs` 中，如果遇到走廊或边界，则标记当前主题空间为无效。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 和 n 分别是 `grid` 的行数和列数。每个位置最多被访问一次。
空间复杂度: O(m * n)，用于存储 `visited` 数组和递归调用栈。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def dfs(grid, visited, i, j, char):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0' or visited[i][j]:
        return 0, False
    visited[i][j] = True
    area, is_valid = 1, True
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i + di, j + dj
        sub_area, sub_is_valid = dfs(grid, visited, ni, nj, char)
        area += sub_area
        if not sub_is_valid:
            is_valid = False
    return area, is_valid

def solution_function_name(grid: List[str]) -> int:
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    max_area = 0
    
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and grid[i][j] != '0':
                area, is_valid = dfs(grid, visited, i, j, grid[i][j])
                if is_valid:
                    max_area = max(max_area, area)
    
    return max_area

Solution = create_solution(solution_function_name)