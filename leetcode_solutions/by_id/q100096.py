# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100096
标题: Programmable Robot
难度: medium
链接: https://leetcode.cn/problems/programmable-robot/
题目类型: 数组、哈希表、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 03. 机器人大冒险 - 力扣团队买了一个可编程机器人，机器人初始位置在原点(0, 0)。小伙伴事先给机器人输入一串指令command，机器人就会无限循环这条指令的步骤进行移动。指令有两种： 1. U: 向y轴正方向移动一格 2. R: 向x轴正方向移动一格。 不幸的是，在 xy 平面上还有一些障碍物，他们的坐标用obstacles表示。机器人一旦碰到障碍物就会被损毁。 给定终点坐标(x, y)，返回机器人能否完好地到达终点。如果能，返回true；否则返回false。 示例 1： 输入：command = "URR", obstacles = [], x = 3, y = 2 输出：true 解释：U(0, 1) -> R(1, 1) -> R(2, 1) -> U(2, 2) -> R(3, 2)。 示例 2： 输入：command = "URR", obstacles = [[2, 2]], x = 3, y = 2 输出：false 解释：机器人在到达终点前会碰到(2, 2)的障碍物。 示例 3： 输入：command = "URR", obstacles = [[4, 2]], x = 3, y = 2 输出：true 解释：到达终点后，再碰到障碍物也不影响返回结果。 限制： 1. 2 <= command的长度 <= 1000 2. command由U，R构成，且至少有一个U，至少有一个R 3. 0 <= x <= 1e9, 0 <= y <= 1e9 4. 0 <= obstacles的长度 <= 1000 5. obstacles[i]不为原点或者终点
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过模拟机器人在一个周期内的路径，判断终点和障碍物是否在路径上。

算法步骤:
1. 模拟一个周期内的路径，并记录每个位置。
2. 判断终点是否在路径上。
3. 判断所有障碍物是否在路径上，如果在路径上且在终点之前，则返回 False。

关键点:
- 通过模运算来确定一个周期内的相对位置。
- 使用集合来存储路径上的所有位置，以便快速查找。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 command 的长度，m 是 obstacles 的长度。
空间复杂度: O(n)，用于存储一个周期内的路径。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
    """
    函数式接口 - 判断机器人能否完好地到达终点
    """
    # 模拟一个周期内的路径
    path = set()
    px, py = 0, 0
    for c in command:
        if c == 'U':
            py += 1
        elif c == 'R':
            px += 1
        path.add((px, py))
    
    # 判断终点是否在路径上
    def is_in_path(tx, ty):
        if tx < 0 or ty < 0:
            return False
        cycle_x, cycle_y = tx % (px + 1), ty % (py + 1)
        return (cycle_x, cycle_y) in path
    
    # 判断终点
    if not is_in_path(x, y):
        return False
    
    # 判断障碍物
    for ox, oy in obstacles:
        if ox <= x and oy <= y and is_in_path(ox, oy):
            return False
    
    return True


Solution = create_solution(solution_function_name)