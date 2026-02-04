# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1280
标题: Diet Plan Performance
难度: easy
链接: https://leetcode.cn/problems/diet-plan-performance/
题目类型: 数组、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1176. 健身计划评估 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口来计算每天的卡路里摄入量，并根据给定的下限和上限来判断健身计划的表现。

算法步骤:
1. 初始化一个变量 `total_calories` 来记录当前窗口内的总卡路里摄入量。
2. 初始化一个变量 `points` 来记录健身计划的得分。
3. 遍历每一天的卡路里摄入量：
   - 如果当前天数小于 `k`，则将当天的卡路里摄入量加到 `total_calories` 中。
   - 否则，从 `total_calories` 中减去 `k` 天前的卡路里摄入量，然后加上当天的卡路里摄入量。
   - 根据 `total_calories` 的值更新 `points`：
     - 如果 `total_calories` 小于 `lower`，则 `points` 减 1。
     - 如果 `total_calories` 大于 `upper`，则 `points` 加 1。
4. 返回 `points` 作为结果。

关键点:
- 使用滑动窗口来维护当前 `k` 天的卡路里摄入量。
- 根据 `total_calories` 的值动态更新 `points`。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 `calories` 的长度。我们只需要遍历一次数组。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def diet_plan_performance(calories: List[int], k: int, lower: int, upper: int) -> int:
    """
    计算健身计划的表现分数。

    :param calories: 每天的卡路里摄入量列表
    :param k: 连续天数
    :param lower: 卡路里摄入量的下限
    :param upper: 卡路里摄入量的上限
    :return: 健身计划的表现分数
    """
    total_calories = 0
    points = 0
    n = len(calories)

    for i in range(n):
        total_calories += calories[i]
        if i >= k:
            total_calories -= calories[i - k]
        if i >= k - 1:
            if total_calories < lower:
                points -= 1
            elif total_calories > upper:
                points += 1

    return points


Solution = create_solution(diet_plan_performance)