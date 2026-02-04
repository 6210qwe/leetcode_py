# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 912
标题: Random Pick with Weight
难度: medium
链接: https://leetcode.cn/problems/random-pick-with-weight/
题目类型: 数组、数学、二分查找、前缀和、随机化
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
528. 按权重随机选择 - 给你一个 下标从 0 开始 的正整数数组 w ，其中 w[i] 代表第 i 个下标的权重。 请你实现一个函数 pickIndex ，它可以 随机地 从范围 [0, w.length - 1] 内（含 0 和 w.length - 1）选出并返回一个下标。选取下标 i 的 概率 为 w[i] / sum(w) 。 * 例如，对于 w = [1, 3]，挑选下标 0 的概率为 1 / (1 + 3) = 0.25 （即，25%），而选取下标 1 的概率为 3 / (1 + 3) = 0.75（即，75%）。 示例 1： 输入： ["Solution","pickIndex"] [[[1]],[]] 输出： [null,0] 解释： Solution solution = new Solution([1]); solution.pickIndex(); // 返回 0，因为数组中只有一个元素，所以唯一的选择是返回下标 0。 示例 2： 输入： ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"] [[[1,3]],[],[],[],[],[]] 输出： [null,1,1,1,1,0] 解释： Solution solution = new Solution([1, 3]); solution.pickIndex(); // 返回 1，返回下标 1，返回该下标概率为 3/4 。 solution.pickIndex(); // 返回 1 solution.pickIndex(); // 返回 1 solution.pickIndex(); // 返回 1 solution.pickIndex(); // 返回 0，返回下标 0，返回该下标概率为 1/4 。 由于这是一个随机问题，允许多个答案，因此下列输出都可以被认为是正确的: [null,1,1,1,1,0] [null,1,1,1,1,1] [null,1,1,1,0,0] [null,1,1,1,0,1] [null,1,0,1,0,0] ...... 诸若此类。 提示： * 1 <= w.length <= 104 * 1 <= w[i] <= 105 * pickIndex 将被调用不超过 104 次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和数组存储权重的累积和，并使用二分查找来找到随机数对应的下标。

算法步骤:
1. 计算权重数组 w 的前缀和数组 prefix_sum。
2. 在 pickIndex 方法中，生成一个在 [1, total_weight] 范围内的随机数。
3. 使用二分查找在前缀和数组中找到第一个大于等于该随机数的位置，返回其下标。

关键点:
- 前缀和数组用于快速计算累积权重。
- 二分查找用于高效地找到随机数对应的位置。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) 初始化，O(log n) 每次 pickIndex
空间复杂度: O(n) 存储前缀和数组
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import random
from leetcode_solutions.utils.solution import create_solution


class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sum.append(total)
        self.total_weight = total

    def pickIndex(self) -> int:
        target = random.randint(1, self.total_weight)
        left, right = 0, len(self.prefix_sum) - 1
        while left < right:
            mid = (left + right) // 2
            if self.prefix_sum[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


Solution = create_solution(Solution)