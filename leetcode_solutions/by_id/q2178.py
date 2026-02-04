# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2178
标题: Walking Robot Simulation II
难度: medium
链接: https://leetcode.cn/problems/walking-robot-simulation-ii/
题目类型: 设计、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2069. 模拟行走机器人 II - 给你一个在 XY 平面上的 width x height 的网格图，左下角 的格子为 (0, 0) ，右上角 的格子为 (width - 1, height - 1) 。网格图中相邻格子为四个基本方向之一（"North"，"East"，"South" 和 "West"）。一个机器人 初始 在格子 (0, 0) ，方向为 "East" 。 机器人可以根据指令移动指定的 步数 。每一步，它可以执行以下操作。 1. 沿着当前方向尝试 往前一步 。 2. 如果机器人下一步将到达的格子 超出了边界 ，机器人会 逆时针 转 90 度，然后再尝试往前一步。 如果机器人完成了指令要求的移动步数，它将停止移动并等待下一个指令。 请你实现 Robot 类： * Robot(int width, int height) 初始化一个 width x height 的网格图，机器人初始在 (0, 0) ，方向朝 "East" 。 * void step(int num) 给机器人下达前进 num 步的指令。 * int[] getPos() 返回机器人当前所处的格子位置，用一个长度为 2 的数组 [x, y] 表示。 * String getDir() 返回当前机器人的朝向，为 "North" ，"East" ，"South" 或者 "West" 。 示例 1： example-1 [https://assets.leetcode.com/uploads/2021/10/09/example-1.png] 输入： ["Robot", "step", "step", "getPos", "getDir", "step", "step", "step", "getPos", "getDir"] [[6, 3], [2], [2], [], [], [2], [1], [4], [], []] 输出： [null, null, null, [4, 0], "East", null, null, null, [1, 2], "West"] 解释： Robot robot = new Robot(6, 3); // 初始化网格图，机器人在 (0, 0) ，朝东。 robot.step(2); // 机器人朝东移动 2 步，到达 (2, 0) ，并朝东。 robot.step(2); // 机器人朝东移动 2 步，到达 (4, 0) ，并朝东。 robot.getPos(); // 返回 [4, 0] robot.getDir(); // 返回 "East" robot.step(2); // 朝东移动 1 步到达 (5, 0) ，并朝东。 // 下一步继续往东移动将出界，所以逆时针转变方向朝北。 // 然后，往北移动 1 步到达 (5, 1) ，并朝北。 robot.step(1); // 朝北移动 1 步到达 (5, 2) ，并朝 北 （不是朝西）。 robot.step(4); // 下一步继续往北移动将出界，所以逆时针转变方向朝西。 // 然后，移动 4 步到 (1, 2) ，并朝西。 robot.getPos(); // 返回 [1, 2] robot.getDir(); // 返回 "West" 提示： * 2 <= width, height <= 100 * 1 <= num <= 105 * step ，getPos 和 getDir 总共 调用次数不超过 104 次。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
- 使用一个循环来处理机器人的移动，并在每次移动时检查是否超出边界。如果超出边界，则改变方向。

算法步骤:
1. 初始化机器人的位置和方向。
2. 在 `step` 方法中，根据当前方向计算新的位置，并在必要时改变方向。
3. 在 `getPos` 和 `getDir` 方法中返回当前的位置和方向。

关键点:
- 使用一个方向数组来表示四个方向。
- 通过取模运算来处理大步数的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 每次移动操作的时间复杂度是常数级别的。
空间复杂度: O(1) - 只使用了常数级别的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.x, self.y = 0, 0
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # East, North, West, South
        self.dir_index = 0  # Initial direction is East

    def step(self, num: int):
        total_steps = (self.x + self.y + num) % ((self.width + self.height - 2) * 2)
        while total_steps > 0:
            dx, dy = self.directions[self.dir_index]
            if 0 <= self.x + dx < self.width and 0 <= self.y + dy < self.height:
                self.x += dx
                self.y += dy
                total_steps -= 1
            else:
                self.dir_index = (self.dir_index + 1) % 4

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        dir_names = ["East", "North", "West", "South"]
        return dir_names[self.dir_index]

# Example usage
# robot = Robot(6, 3)
# robot.step(2)
# print(robot.getPos())  # Output: [2, 0]
# print(robot.getDir())  # Output: "East"
# robot.step(2)
# print(robot.getPos())  # Output: [4, 0]
# print(robot.getDir())  # Output: "East"
# robot.step(2)
# print(robot.getPos())  # Output: [5, 1]
# print(robot.getDir())  # Output: "North"
# robot.step(1)
# print(robot.getPos())  # Output: [5, 2]
# print(robot.getDir())  # Output: "North"
# robot.step(4)
# print(robot.getPos())  # Output: [1, 2]
# print(robot.getDir())  # Output: "West"