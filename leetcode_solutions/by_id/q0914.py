# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 914
标题: Random Point in Non-overlapping Rectangles
难度: medium
链接: https://leetcode.cn/problems/random-point-in-non-overlapping-rectangles/
题目类型: 水塘抽样、数组、数学、二分查找、有序集合、前缀和、随机化
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
497. 非重叠矩形中的随机点 - 给定一个由非重叠的轴对齐矩形的数组 rects ，其中 rects[i] = [ai, bi, xi, yi] 表示 (ai, bi) 是第 i 个矩形的左下角点，(xi, yi) 是第 i 个矩形的右上角点。设计一个算法来随机挑选一个被某一矩形覆盖的整数点。矩形周长上的点也算做是被矩形覆盖。所有满足要求的点必须等概率被返回。 在给定的矩形覆盖的空间内的任何整数点都有可能被返回。 请注意 ，整数点是具有整数坐标的点。 实现 Solution 类: * Solution(int[][] rects) 用给定的矩形数组 rects 初始化对象。 * int[] pick() 返回一个随机的整数点 [u, v] 在给定的矩形所覆盖的空间内。 示例 1： [https://assets.leetcode.com/uploads/2021/07/24/lc-pickrandomrec.jpg] 输入: ["Solution", "pick", "pick", "pick", "pick", "pick"] [[[[-2, -2, 1, 1], [2, 2, 4, 6]]], [], [], [], [], []] 输出: [null, [1, -2], [1, -1], [-1, -2], [-2, -2], [0, 0]] 解释： Solution solution = new Solution([[-2, -2, 1, 1], [2, 2, 4, 6]]); solution.pick(); // 返回 [1, -2] solution.pick(); // 返回 [1, -1] solution.pick(); // 返回 [-1, -2] solution.pick(); // 返回 [-2, -2] solution.pick(); // 返回 [0, 0] 提示： * 1 <= rects.length <= 100 * rects[i].length == 4 * -109 <= ai < xi <= 109 * -109 <= bi < yi <= 109 * xi - ai <= 2000 * yi - bi <= 2000 * 所有的矩形不重叠。 * pick 最多被调用 104 次。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和与二分查找来实现随机选择。

算法步骤:
1. 计算每个矩形的面积，并计算前缀和。
2. 使用前缀和进行二分查找，找到对应的矩形。
3. 在选定的矩形中随机选择一个点。

关键点:
- 使用前缀和来快速确定矩形的概率分布。
- 使用二分查找来高效地找到目标矩形。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n) - 二分查找的时间复杂度。
空间复杂度: O(n) - 存储前缀和数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import random
from bisect import bisect_left

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.areas = []
        total_area = 0
        for rect in rects:
            x1, y1, x2, y2 = rect
            area = (x2 - x1 + 1) * (y2 - y1 + 1)
            total_area += area
            self.areas.append(total_area)

    def pick(self) -> List[int]:
        # 生成一个在 [1, total_area] 范围内的随机数
        target = random.randint(1, self.areas[-1])
        
        # 使用二分查找找到对应的矩形
        idx = bisect_left(self.areas, target)
        
        # 如果 idx 为 0 或者 target 不在当前区间内，减 1
        if idx > 0 and target > self.areas[idx - 1]:
            idx -= 1
        
        # 在选定的矩形中随机选择一个点
        x1, y1, x2, y2 = self.rects[idx]
        return [random.randint(x1, x2), random.randint(y1, y2)]


# 工厂函数
def create_solution(rects: List[List[int]]) -> Solution:
    return Solution(rects)