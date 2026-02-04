# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1123
标题: Single-Row Keyboard
难度: easy
链接: https://leetcode.cn/problems/single-row-keyboard/
题目类型: 哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1165. 单行键盘 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表记录每个字符在键盘上的位置，然后遍历字符串计算相邻字符的距离。

算法步骤:
1. 构建一个哈希表，记录每个字符在键盘上的位置。
2. 遍历字符串，计算相邻字符的距离，并累加到总距离中。

关键点:
- 使用哈希表可以快速查找字符的位置。
- 计算相邻字符的距离时，注意处理第一个字符的特殊情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是字符串的长度，m 是键盘字符串的长度。
空间复杂度: O(m)，用于存储哈希表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(keyboard: str, word: str) -> int:
    """
    函数式接口 - 计算在单行键盘上输入给定单词所需的最小距离。
    """
    # 构建哈希表，记录每个字符在键盘上的位置
    char_positions = {char: idx for idx, char in enumerate(keyboard)}
    
    # 初始化总距离
    total_distance = 0
    
    # 遍历字符串，计算相邻字符的距离
    prev_position = char_positions[word[0]]
    for i in range(1, len(word)):
        current_position = char_positions[word[i]]
        total_distance += abs(current_position - prev_position)
        prev_position = current_position
    
    return total_distance


Solution = create_solution(solution_function_name)