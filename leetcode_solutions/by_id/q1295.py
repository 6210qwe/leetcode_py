# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1295
标题: Minimum Garden Perimeter to Collect Enough Apples
难度: medium
链接: https://leetcode.cn/problems/minimum-garden-perimeter-to-collect-enough-apples/
题目类型: 数学、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1954. 收集足够苹果的最小花园周长 - 给你一个用无限二维网格表示的花园，每一个 整数坐标处都有一棵苹果树。整数坐标 (i, j) 处的苹果树有 |i| + |j| 个苹果。 你将会买下正中心坐标是 (0, 0) 的一块 正方形土地 ，且每条边都与两条坐标轴之一平行。 给你一个整数 neededApples ，请你返回土地的 最小周长 ，使得 至少 有 neededApples 个苹果在土地 里面或者边缘上。 |x| 的值定义为： * 如果 x >= 0 ，那么值为 x * 如果 x < 0 ，那么值为 -x 示例 1： [https://pic.leetcode.cn/1627790803-qcBKFw-image.png] 输入：neededApples = 1 输出：8 解释：边长长度为 1 的正方形不包含任何苹果。 但是边长为 2 的正方形包含 12 个苹果（如上图所示）。 周长为 2 * 4 = 8 。 示例 2： 输入：neededApples = 13 输出：16 示例 3： 输入：neededApples = 1000000000 输出：5040 提示： * 1 <= neededApples <= 1015
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用数学公式计算正方形内的苹果总数，并通过二分查找找到满足条件的最小边长。

算法步骤:
1. 计算边长为 k 的正方形内的苹果总数。
2. 使用二分查找找到最小的 k，使得正方形内的苹果总数大于等于 neededApples。

关键点:
- 苹果总数的计算公式为 2 * k * (k + 1) * (2 * k + 1)。
- 二分查找的范围是从 1 到 100000。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log(neededApples))
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def minimum_perimeter(needed_apples: int) -> int:
    """
    函数式接口 - 计算收集足够苹果的最小花园周长
    """
    # 计算边长为 k 的正方形内的苹果总数
    def total_apples(k: int) -> int:
        return 2 * k * (k + 1) * (2 * k + 1)

    # 二分查找
    left, right = 1, 100000
    while left < right:
        mid = (left + right) // 2
        if total_apples(mid) < needed_apples:
            left = mid + 1
        else:
            right = mid
    return 8 * left


Solution = create_solution(minimum_perimeter)