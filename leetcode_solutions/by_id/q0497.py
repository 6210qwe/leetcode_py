# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 497
标题: 随机点名
难度: 中等
链接: https://leetcode.cn/problems/random-point-in-non-overlapping-rectangles/
题目类型: 设计
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
给你一个二维整数数组 rectangles ，其中 rectangles[i] = [xi1, yi1, xi2, yi2] 表示一个坐标轴对齐的矩形，四个顶点分别为 (xi1, yi1), (xi2, yi1), (xi1, yi2) 和 (xi2, yi2) 。这些矩形互不重叠。

矩形的面积是 (xi2 - xi1) * (yi2 - yi1) 。

选择一个矩形并返回其编号。每个矩形被选中的概率应该与其面积成正比。

实现 Solution 类：
- Solution(int[][] rects) 用给定的矩形数组 rects 初始化对象。
- int pick() 随机均匀地选择并返回一个位于任一矩形中的整数点。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和 + 二分查找

算法步骤:
1. 计算每个矩形的面积，并计算前缀和数组。
2. 在 pick 函数中，使用随机数生成器生成一个在总面积范围内的随机数。
3. 使用二分查找找到该随机数对应的矩形。
4. 在该矩形内随机选择一个点。

关键点:
- 使用前缀和数组来快速定位矩形。
- 使用二分查找来提高查找效率。
- 在选定的矩形内随机选择一个点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n) - 二分查找的时间复杂度
空间复杂度: O(n) - 存储前缀和数组
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import random
from leetcode_solutions.utils.solution import create_solution


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.areas = []
        total_area = 0
        for rect in rects:
            area = (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1)
            total_area += area
            self.areas.append(total_area)
        self.total_area = total_area

    def pick(self) -> List[int]:
        target = random.randint(1, self.total_area)
        left, right = 0, len(self.areas) - 1
        while left < right:
            mid = (left + right) // 2
            if self.areas[mid] < target:
                left = mid + 1
            else:
                right = mid
        rect = self.rects[left]
        x = random.randint(rect[0], rect[2])
        y = random.randint(rect[1], rect[3])
        return [x, y]


# 自动生成Solution类（无需手动编写）
Solution = create_solution(Solution)