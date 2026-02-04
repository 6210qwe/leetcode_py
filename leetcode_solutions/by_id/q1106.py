# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1106
标题: Escape a Large Maze
难度: hard
链接: https://leetcode.cn/problems/escape-a-large-maze/
题目类型: 深度优先搜索、广度优先搜索、数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1036. 逃离大迷宫 - 在一个 106 x 106 的网格中，每个网格上方格的坐标为 (x, y) 。 现在从源方格 source = [sx, sy] 开始出发，意图赶往目标方格 target = [tx, ty] 。数组 blocked 是封锁的方格列表，其中每个 blocked[i] = [xi, yi] 表示坐标为 (xi, yi) 的方格是禁止通行的。 每次移动，都可以走到网格中在四个方向上相邻的方格，只要该方格 不 在给出的封锁列表 blocked 上。同时，不允许走出网格。 只有在可以通过一系列的移动从源方格 source 到达目标方格 target 时才返回 true。否则，返回 false。 示例 1： 输入：blocked = [[0,1],[1,0]], source = [0,0], target = [0,2] 输出：false 解释： 从源方格无法到达目标方格，因为我们无法在网格中移动。 无法向北或者向东移动是因为方格禁止通行。 无法向南或者向西移动是因为不能走出网格。 示例 2： 输入：blocked = [], source = [0,0], target = [999999,999999] 输出：true 解释： 因为没有方格被封锁，所以一定可以到达目标方格。 提示： * 0 <= blocked.length <= 200 * blocked[i].length == 2 * 0 <= xi, yi < 106 * source.length == target.length == 2 * 0 <= sx, sy, tx, ty < 106 * source != target * 题目数据保证 source 和 target 不在封锁列表内
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）来判断是否可以从起点到达终点，并且通过检查最大可能的封锁区域来优化搜索。

算法步骤:
1. 初始化一个集合 `blocked_set` 来存储所有被封锁的方格。
2. 定义一个函数 `is_reachable` 来使用 BFS 检查从起点到终点是否可达。
3. 如果起点和终点都在最大可能的封锁区域内，则分别从起点和终点开始进行 BFS，检查是否可以逃脱封锁区域。
4. 如果起点或终点不在最大可能的封锁区域内，则直接返回 True。

关键点:
- 最大可能的封锁区域大小为 `len(blocked) * (len(blocked) - 1) // 2`。
- 通过 BFS 检查是否可以逃脱封锁区域。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(B^2)，其中 B 是 blocked 的长度。最坏情况下，BFS 需要遍历最大可能的封锁区域。
空间复杂度: O(B^2)，用于存储 BFS 中的队列和访问过的节点。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def is_reachable(source: List[int], target: List[int], blocked: set, max_area: int) -> bool:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    queue = [source]
    visited.add(tuple(source))

    while queue:
        x, y = queue.pop(0)
        if [x, y] == target:
            return True
        if len(visited) > max_area:
            return True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 10**6 and 0 <= ny < 10**6 and (nx, ny) not in visited and (nx, ny) not in blocked:
                queue.append((nx, ny))
                visited.add((nx, ny))

    return False


def solution_function_name(blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
    """
    函数式接口 - 判断是否可以从起点到达终点
    """
    if not blocked:
        return True

    blocked_set = {tuple(b) for b in blocked}
    max_area = len(blocked) * (len(blocked) - 1) // 2

    if is_reachable(source, target, blocked_set, max_area):
        return True

    if is_reachable(target, source, blocked_set, max_area):
        return True

    return False


Solution = create_solution(solution_function_name)