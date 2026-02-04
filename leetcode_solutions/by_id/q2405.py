# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2405
标题: Minimum Number of Keypresses
难度: medium
链接: https://leetcode.cn/problems/minimum-number-of-keypresses/
题目类型: 贪心、哈希表、字符串、计数、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2268. 最少按键次数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，优先使用频率最高的字符，以减少按键次数。

算法步骤:
1. 统计每个字符的出现频率。
2. 按照频率从高到低排序。
3. 计算每个字符的按键次数，并累加总按键次数。

关键点:
- 使用哈希表统计字符频率。
- 按频率排序后，分组计算按键次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + k log k)，其中 n 是字符串长度，k 是字符种类数。
空间复杂度: O(k)，用于存储字符频率和排序后的字符列表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_keypresses(s: str) -> int:
    """
    函数式接口 - 计算最少按键次数
    """
    # 统计每个字符的出现频率
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # 按频率从高到低排序
    sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    
    # 计算每个字符的按键次数，并累加总按键次数
    total_keypresses = 0
    for i, (char, count) in enumerate(sorted_chars):
        group = i // 9  # 每 9 个字符一组
        total_keypresses += (group + 1) * count
    
    return total_keypresses


Solution = create_solution(min_keypresses)