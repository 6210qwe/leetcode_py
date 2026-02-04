# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1696
标题: Strange Printer II
难度: hard
链接: https://leetcode.cn/problems/strange-printer-ii/
题目类型: 图、拓扑排序、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1591. 奇怪的打印机 II - 给你一个奇怪的打印机，它有如下两个特殊的打印规则： * 每一次操作时，打印机会用同一种颜色打印一个矩形的形状，每次打印会覆盖矩形对应格子里原本的颜色。 * 一旦矩形根据上面的规则使用了一种颜色，那么 相同的颜色不能再被使用 。 给你一个初始没有颜色的 m x n 的矩形 targetGrid ，其中 targetGrid[row][col] 是位置 (row, col) 的颜色。 如果你能按照上述规则打印出矩形 targetGrid ，请你返回 true ，否则返回 false 。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/09/19/sample_1_1929.png] 输入：targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]] 输出：true 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/09/19/sample_2_1929.png] 输入：targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]] 输出：true 示例 3： 输入：targetGrid = [[1,2,1],[2,1,2],[1,2,1]] 输出：false 解释：没有办法得到 targetGrid ，因为每一轮操作使用的颜色互不相同。 示例 4： 输入：targetGrid = [[1,1,1],[3,1,3]] 输出：false 提示： * m == targetGrid.length * n == targetGrid[i].length * 1 <= m, n <= 60 * 1 <= targetGrid[row][col] <= 60
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用拓扑排序来判断是否可以按要求打印目标网格。

算法步骤:
1. 构建每个颜色的边界矩形。
2. 构建颜色之间的依赖关系图。
3. 使用拓扑排序检查是否存在环，如果存在环则无法打印。

关键点:
- 通过构建颜色的边界矩形来确定颜色的覆盖范围。
- 通过颜色之间的依赖关系图来判断是否可以按顺序打印。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n + C^2)，其中 m 和 n 分别是网格的行数和列数，C 是颜色的数量。
空间复杂度: O(C^2)，用于存储颜色之间的依赖关系图。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def isPrintable(targetGrid: List[List[int]]) -> bool:
    """
    判断是否可以按要求打印目标网格。
    """
    m, n = len(targetGrid), len(targetGrid[0])
    color_bounds = {}
    
    # 构建每个颜色的边界矩形
    for i in range(m):
        for j in range(n):
            color = targetGrid[i][j]
            if color not in color_bounds:
                color_bounds[color] = [i, j, i, j]
            else:
                color_bounds[color][0] = min(color_bounds[color][0], i)
                color_bounds[color][1] = min(color_bounds[color][1], j)
                color_bounds[color][2] = max(color_bounds[color][2], i)
                color_bounds[color][3] = max(color_bounds[color][3], j)
    
    # 构建颜色之间的依赖关系图
    graph = {color: set() for color in color_bounds}
    in_degree = {color: 0 for color in color_bounds}
    
    for i in range(m):
        for j in range(n):
            color = targetGrid[i][j]
            for c, (top, left, bottom, right) in color_bounds.items():
                if top <= i <= bottom and left <= j <= right and c != color:
                    if color not in graph[c]:
                        graph[c].add(color)
                        in_degree[color] += 1
    
    # 使用拓扑排序检查是否存在环
    queue = [color for color in in_degree if in_degree[color] == 0]
    visited_count = 0
    
    while queue:
        color = queue.pop(0)
        visited_count += 1
        for next_color in graph[color]:
            in_degree[next_color] -= 1
            if in_degree[next_color] == 0:
                queue.append(next_color)
    
    return visited_count == len(color_bounds)


Solution = create_solution(isPrintable)