# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3474
标题: Better Compression of String
难度: medium
链接: https://leetcode.cn/problems/better-compression-of-string/
题目类型: 哈希表、字符串、计数、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3167. 字符串的更好压缩 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表统计每个字符及其出现次数，然后按字符出现次数从大到小排序，最后构建压缩后的字符串。

算法步骤:
1. 统计每个字符及其出现次数。
2. 按字符出现次数从大到小排序。
3. 构建压缩后的字符串。

关键点:
- 使用哈希表统计字符出现次数。
- 按字符出现次数排序。
- 构建压缩后的字符串时，先输出字符再输出其出现次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是字符串的长度。统计字符出现次数的时间复杂度为 O(n)，排序的时间复杂度为 O(n log n)。
空间复杂度: O(n)，哈希表和排序所需的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(s: str) -> str:
    """
    函数式接口 - 实现字符串的更好压缩
    """
    # 统计每个字符及其出现次数
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # 按字符出现次数从大到小排序
    sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
    
    # 构建压缩后的字符串
    compressed_string = ""
    for char, count in sorted_chars:
        compressed_string += f"{char}{count}"
    
    return compressed_string


Solution = create_solution(solution_function_name)