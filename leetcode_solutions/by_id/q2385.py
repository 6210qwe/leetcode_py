# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2385
标题: Count Positions on Street With Required Brightness
难度: medium
链接: https://leetcode.cn/problems/count-positions-on-street-with-required-brightness/
题目类型: 数组、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2237. 计算街道上满足所需亮度的位置数量 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和来计算每个位置的亮度，并统计满足条件的位置数量。

算法步骤:
1. 初始化一个长度为 n+1 的前缀和数组 `brightness`，用于存储每个位置的亮度。
2. 遍历所有灯泡，更新 `brightness` 数组。对于每个灯泡，其影响范围为 [max(0, i - r), min(n-1, i + r)]。
3. 计算前缀和数组的累积和，得到每个位置的实际亮度。
4. 遍历 `brightness` 数组，统计亮度大于等于 `t` 的位置数量。

关键点:
- 使用前缀和数组来高效计算每个位置的亮度。
- 注意灯泡的影响范围，确保不越界。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是街道的长度，m 是灯泡的数量。
空间复杂度: O(n)，用于存储前缀和数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_positions_with_brightness(n: int, lights: List[List[int]], t: int) -> int:
    """
    函数式接口 - 计算街道上满足所需亮度的位置数量
    """
    # 初始化前缀和数组
    brightness = [0] * (n + 1)
    
    # 更新前缀和数组
    for pos, range_ in lights:
        left = max(0, pos - range_)
        right = min(n - 1, pos + range_)
        brightness[left] += 1
        brightness[right + 1] -= 1
    
    # 计算累积和
    for i in range(1, n):
        brightness[i] += brightness[i - 1]
    
    # 统计满足条件的位置数量
    return sum(b >= t for b in brightness[:n])


Solution = create_solution(count_positions_with_brightness)