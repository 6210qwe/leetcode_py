# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1931
标题: Shortest Path in a Hidden Grid
难度: medium
链接: https://leetcode.cn/problems/shortest-path-in-a-hidden-grid/
题目类型: 深度优先搜索、广度优先搜索、数组、交互、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1778. 未知网格中的最短路径 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索 (BFS) 来找到从起点到终点的最短路径。

算法步骤:
1. 初始化一个队列，将起点加入队列，并标记为已访问。
2. 使用一个集合来记录已经访问过的节点，避免重复访问。
3. 进行 BFS 遍历：
   - 从队列中取出一个节点。
   - 如果该节点是终点，返回当前路径长度。
   - 否则，尝试向四个方向移动（上、下、左、右），如果新位置未被访问且在网格范围内，则将其加入队列并标记为已访问。
4. 如果遍历完所有可能的路径仍未找到终点，返回 -1。

关键点:
- 使用 BFS 保证找到的路径是最短路径。
- 使用集合记录已访问节点，避免重复访问。
- 通过与隐藏网格的交互来确定每个节点的状态。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 和 n 分别是网格的行数和列数。在最坏情况下，需要访问网格中的每个节点一次。
空间复杂度: O(m * n)，队列和访问集合的空间复杂度均为 O(m * n)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class Solution:
    def findShortestPath(self, grid: 'Grid') -> int:
        """
        使用广度优先搜索 (BFS) 来找到从起点到终点的最短路径。
        """
        from collections import deque

        # 方向数组，表示上下左右四个方向
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # 获取起点
        start_x, start_y = grid.getStart()
        if grid.isGoal(start_x, start_y):
            return 0

        # 初始化队列和访问集合
        queue = deque([(start_x, start_y, 0)])  # (x, y, steps)
        visited = set([(start_x, start_y)])

        while queue:
            x, y, steps = queue.popleft()

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy

                # 检查新位置是否在网格范围内
                if 0 <= new_x < grid.height and 0 <= new_y < grid.width:
                    # 检查新位置是否已被访问
                    if (new_x, new_y) not in visited:
                        # 检查新位置的状态
                        cell = grid.get(new_x, new_y)
                        if cell == 2:  # 墙
                            continue
                        elif cell == 3:  # 目标
                            return steps + 1
                        else:  # 空地
                            queue.append((new_x, new_y, steps + 1))
                            visited.add((new_x, new_y))

        return -1  # 无法到达目标

Solution = create_solution(Solution)