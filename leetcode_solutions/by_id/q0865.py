# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 865
标题: Robot Room Cleaner
难度: hard
链接: https://leetcode.cn/problems/robot-room-cleaner/
题目类型: 回溯、交互
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
489. 扫地机器人 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用回溯法遍历所有房间，并在每个房间中使用深度优先搜索 (DFS) 清理。

算法步骤:
1. 初始化一个集合 `visited` 来记录已经访问过的房间。
2. 定义一个递归函数 `dfs` 来清理当前房间并递归清理相邻房间。
3. 在 `dfs` 函数中：
   - 如果当前房间已经被访问过，直接返回。
   - 标记当前房间为已访问。
   - 清理当前房间。
   - 尝试向四个方向移动，如果可以移动则递归调用 `dfs`。
   - 每次递归返回后，将机器人移回原位置并转向下一个方向。

关键点:
- 使用集合 `visited` 记录已访问的房间，避免重复清理。
- 使用回溯法确保机器人能够回到原位置并继续尝试其他方向。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是房间的数量。每个房间最多被访问一次。
空间复杂度: O(n)，最坏情况下递归栈的深度为房间的数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class Robot:
    def move(self) -> bool:
        pass

    def turnLeft(self) -> None:
        pass

    def turnRight(self) -> None:
        pass

    def clean(self) -> None:
        pass

def cleanRoom(robot: Robot):
    """
    使用回溯法和深度优先搜索 (DFS) 清理所有房间。
    """
    def dfs(x: int, y: int, d: int):
        robot.clean()
        visited.add((x, y))
        
        for i in range(4):
            new_d = (d + i) % 4
            new_x, new_y = x + directions[new_d][0], y + directions[new_d][1]
            
            if (new_x, new_y) not in visited and robot.move():
                dfs(new_x, new_y, new_d)
                # 回溯
                robot.turnLeft()
                robot.turnLeft()
                robot.move()
                robot.turnLeft()
                robot.turnLeft()
            robot.turnRight()
    
    # 方向数组：上、右、下、左
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()
    dfs(0, 0, 0)

Solution = create_solution(cleanRoom)