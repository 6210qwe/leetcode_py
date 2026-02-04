# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1959
标题: Minimum Path Cost in a Hidden Grid
难度: medium
链接: https://leetcode.cn/problems/minimum-path-cost-in-a-hidden-grid/
题目类型: 深度优先搜索、广度优先搜索、图、数组、交互、矩阵、最短路、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1810. 隐藏网格下的最小消耗路径 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 A* 算法来找到从起点到终点的最小路径成本。

算法步骤:
1. 初始化 A* 算法所需的开放列表和关闭列表。
2. 定义启发式函数（例如曼哈顿距离）来估计从当前节点到目标节点的成本。
3. 从起点开始，将起点加入开放列表。
4. 进入主循环，直到开放列表为空：
   - 从开放列表中选择 f 值（g + h）最小的节点。
   - 如果该节点是目标节点，则返回路径成本。
   - 将该节点从开放列表移除，并加入关闭列表。
   - 对于该节点的所有邻居节点，计算其 g 值和 h 值，更新其 f 值。
   - 如果邻居节点不在关闭列表中且不在开放列表中，则将其加入开放列表。
5. 如果开放列表为空且未找到目标节点，则返回 -1。

关键点:
- 使用 A* 算法结合启发式函数来优化搜索过程。
- 通过维护开放列表和关闭列表来避免重复访问节点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m * log(n * m))，其中 n 和 m 分别是网格的行数和列数。A* 算法在最坏情况下可能需要遍历所有节点，每次操作的时间复杂度为 O(log(n * m))。
空间复杂度: O(n * m)，存储开放列表和关闭列表所需的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class Node:
    def __init__(self, x, y, g, h):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

def heuristic(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def solution_function_name(grid: List[List[int]], start: List[int], target: List[int]) -> int:
    """
    函数式接口 - 使用 A* 算法找到从起点到终点的最小路径成本
    """
    n, m = len(grid), len(grid[0])
    start_node = Node(start[0], start[1], 0, heuristic(start[0], start[1], target[0], target[1]))
    open_list = [start_node]
    closed_list = set()

    while open_list:
        current_node = min(open_list)
        open_list.remove(current_node)

        if (current_node.x, current_node.y) == (target[0], target[1]):
            return current_node.g

        closed_list.add((current_node.x, current_node.y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = current_node.x + dx, current_node.y + dy
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in closed_list:
                next_node = Node(nx, ny, current_node.g + grid[nx][ny], heuristic(nx, ny, target[0], target[1]))
                if (nx, ny) not in {node.x, node.y} for node in open_list}:
                    open_list.append(next_node)
                else:
                    for node in open_list:
                        if (node.x, node.y) == (nx, ny) and node.g > next_node.g:
                            open_list.remove(node)
                            open_list.append(next_node)
                            break

    return -1

Solution = create_solution(solution_function_name)