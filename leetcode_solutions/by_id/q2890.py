# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2890
标题: Count Substrings Without Repeating Character
难度: medium
链接: https://leetcode.cn/problems/count-substrings-without-repeating-character/
题目类型: 哈希表、字符串、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2743. 计算没有重复字符的子字符串数量 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口来找到所有不包含重复字符的子字符串。

算法步骤:
1. 初始化两个指针 left 和 right，以及一个哈希表 char_index_map 来记录字符的最新位置。
2. 移动右指针 right，扩展窗口。
3. 如果当前字符已经在哈希表中存在且其索引大于等于 left，则更新 left 为该字符的下一个位置。
4. 更新哈希表中的字符位置。
5. 计算当前窗口的长度，并累加到结果中。

关键点:
- 使用滑动窗口来维护不包含重复字符的子字符串。
- 通过哈希表记录字符的最新位置，以便快速更新左指针。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串的长度。每个字符最多被处理两次（一次由右指针，一次由左指针）。
空间复杂度: O(min(n, m))，其中 n 是字符串的长度，m 是字符集的大小。哈希表的大小最多为字符集的大小。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(s: str) -> int:
    """
    函数式接口 - 计算没有重复字符的子字符串数量
    """
    n = len(s)
    if n == 0:
        return 0

    left = 0
    result = 0
    char_index_map = {}

    for right in range(n):
        if s[right] in char_index_map and char_index_map[s[right]] >= left:
            left = char_index_map[s[right]] + 1
        char_index_map[s[right]] = right
        result += right - left + 1

    return result


Solution = create_solution(solution_function_name)