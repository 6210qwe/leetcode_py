# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 353
标题: Design Snake Game
难度: medium
链接: https://leetcode.cn/problems/design-snake-game/
题目类型: 设计、队列、数组、哈希表、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
353. 贪吃蛇 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 设计一个按时间顺序移动的「蛇身队列」和位置集合，模拟贪吃蛇在网格中的移动与吃食物过程

算法步骤:
1. 使用 deque 存储蛇身每个格子的坐标，队首为蛇头，队尾为蛇尾；同时用 set 记录当前蛇身占用的位置以支持 O(1) 冲突检测。
2. 构造函数中记录棋盘宽高、食物列表以及当前得分和蛇头位置等信息。
3. 每次 move 操作根据方向计算新蛇头坐标：(r, c) → (nr, nc)，先检查是否越界；再在「去掉蛇尾之后」判断新头是否撞到蛇身。
4. 若新位置等于当前食物位置，则吃掉食物：只在队首添加新头（不弹出尾部），得分加 1，食物指针后移。
5. 否则正常移动：在队首加入新头，同时从队尾弹出尾部，并更新位置集合。

关键点:
- 注意在判断是否撞到自己时，允许新头落在原来的蛇尾位置（因为尾巴会在本次移动中离开）。
- 需要维护当前食物下标，而不是每次在食物数组中搜索。
- 所有操作都应在 O(1) 时间内完成，以满足多次 move 调用的效率要求。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 每次 move 操作只对蛇身队首队尾及集合做常数次更新。
空间复杂度: O(L) - L 为蛇身长度，使用队列和集合存储所有身体格子。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class SnakeGame:
    """
    设计贪吃蛇游戏：维护蛇身队列和占用集合，模拟移动与吃食物过程。
    """

    def __init__(self, width: int, height: int, food: list[list[int]]):
        self.w = width
        self.h = height
        self.food = food
        self.food_i = 0
        from collections import deque

        self.body = deque([(0, 0)])  # 头在左侧
        self.occupied = {(0, 0)}
        self.score = 0
        self.dir_map = {
            'U': (-1, 0),
            'D': (1, 0),
            'L': (0, -1),
            'R': (0, 1),
        }

    def move(self, direction: str) -> int:
        dr, dc = self.dir_map[direction]
        hr, hc = self.body[0]
        nr, nc = hr + dr, hc + dc

        # 撞墙
        if not (0 <= nr < self.h and 0 <= nc < self.w):
            return -1

        # 先移除尾巴，再判断是否撞到身体
        tail = self.body[-1]
        self.occupied.remove(tail)
        if (nr, nc) in self.occupied:
            return -1

        # 加入新头
        self.body.appendleft((nr, nc))
        self.occupied.add((nr, nc))

        # 吃到食物
        if self.food_i < len(self.food) and [nr, nc] == self.food[self.food_i]:
            self.food_i += 1
            self.score += 1
            # 吃到食物，尾巴不动（补回尾巴）
            self.body.append(tail)
            self.occupied.add(tail)
        else:
            # 正常移动，尾巴已经被移除
            self.body.pop()

        return self.score


def design_snake_game() -> SnakeGame:
    """
    函数式接口 - 返回 SnakeGame 实例，便于在测试中进行方法调用。
    """
    # 具体参数由评测环境传入构造函数，此处仅保留接口占位。
    raise NotImplementedError("请在评测环境中直接使用 SnakeGame 类")


# 自动生成Solution类（无需手动编写）
Solution = create_solution(design_snake_game)
