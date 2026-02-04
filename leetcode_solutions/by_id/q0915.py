# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 915
标题: Generate Random Point in a Circle
难度: medium
链接: https://leetcode.cn/problems/generate-random-point-in-a-circle/
题目类型: 几何、数学、拒绝采样、随机化
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
478. 在圆内随机生成点 - 给定圆的半径和圆心的位置，实现函数 randPoint ，在圆中产生均匀随机点。 实现 Solution 类: * Solution(double radius, double x_center, double y_center) 用圆的半径 radius 和圆心的位置 (x_center, y_center) 初始化对象 * randPoint() 返回圆内的一个随机点。圆周上的一点被认为在圆内。答案作为数组返回 [x, y] 。 示例 1： 输入: ["Solution","randPoint","randPoint","randPoint"] [[1.0, 0.0, 0.0], [], [], []] 输出: [null, [-0.02493, -0.38077], [0.82314, 0.38945], [0.36572, 0.17248]] 解释: Solution solution = new Solution(1.0, 0.0, 0.0); solution.randPoint ();//返回[-0.02493，-0.38077] solution.randPoint ();//返回[0.82314,0.38945] solution.randPoint ();//返回[0.36572,0.17248] 提示： * 0 < radius <= 108 * -107 <= x_center, y_center <= 107 * randPoint 最多被调用 3 * 104 次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用极坐标系生成随机点，然后转换为笛卡尔坐标系。

算法步骤:
1. 生成一个随机角度 theta，范围在 [0, 2π)。
2. 生成一个随机半径 r，范围在 [0, radius)，使用 sqrt(random()) 来保证均匀分布。
3. 将极坐标 (r, theta) 转换为笛卡尔坐标 (x, y)。
4. 将生成的点平移到圆心位置。

关键点:
- 使用 sqrt(random()) 生成随机半径以确保点在圆内均匀分布。
- 将极坐标转换为笛卡尔坐标。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
import random
import math


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        # 生成随机角度
        theta = random.uniform(0, 2 * math.pi)
        # 生成随机半径
        r = self.radius * math.sqrt(random.uniform(0, 1))
        # 计算笛卡尔坐标
        x = self.x_center + r * math.cos(theta)
        y = self.y_center + r * math.sin(theta)
        return [x, y]


# 工厂函数
def create_solution(radius: float, x_center: float, y_center: float) -> Solution:
    return Solution(radius, x_center, y_center)