# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2075
标题: Brightest Position on Street
难度: medium
链接: https://leetcode.cn/problems/brightest-position-on-street/
题目类型: 数组、有序集合、前缀和、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2021. 街上最亮的位置 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用差分数组来记录每个位置的亮度变化，然后通过前缀和计算每个位置的实际亮度。

算法步骤:
1. 初始化一个差分数组 `diff`，长度为 `max(positions) + 2`。
2. 遍历每个灯的位置范围 `[start, end]`，在 `diff[start]` 位置加 1，在 `diff[end + 1]` 位置减 1。
3. 计算前缀和数组 `brightness`，找到最大值及其对应的索引。

关键点:
- 使用差分数组可以高效地记录每个位置的亮度变化。
- 前缀和数组可以快速计算每个位置的实际亮度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是灯的数量，m 是所有灯的最大位置。
空间复杂度: O(m)，需要存储差分数组和前缀和数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(lights: List[List[int]]) -> int:
    """
    函数式接口 - 找到街上最亮的位置
    """
    if not lights:
        return 0

    # 找到所有灯的最大位置
    max_pos = max(max(light[1] for light in lights), max(light[0] for light in lights))

    # 初始化差分数组
    diff = [0] * (max_pos + 2)

    # 更新差分数组
    for start, end in lights:
        diff[start] += 1
        diff[end + 1] -= 1

    # 计算前缀和数组
    brightness = [0] * (max_pos + 2)
    current_brightness = 0
    brightest_pos = 0
    max_brightness = 0

    for i in range(1, max_pos + 2):
        current_brightness += diff[i - 1]
        if current_brightness > max_brightness:
            max_brightness = current_brightness
            brightest_pos = i - 1

    return brightest_pos


Solution = create_solution(solution_function_name)