# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3393
标题: Make String Anti-palindrome
难度: hard
链接: https://leetcode.cn/problems/make-string-anti-palindrome/
题目类型: 贪心、字符串、计数排序、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3088. 使字符串反回文 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过贪心算法和字符计数来确保字符串不是回文。

算法步骤:
1. 统计每个字符的出现次数。
2. 将字符按出现次数从大到小排序。
3. 构建新的字符串，确保相邻字符不相同。
4. 如果无法构建非回文字符串，返回空字符串。

关键点:
- 使用计数器统计字符频率。
- 通过贪心算法构建新字符串，确保相邻字符不同。
- 检查是否可以构建非回文字符串。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是字符串的长度。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(n)，用于存储字符计数和构建新字符串。
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
    函数式接口 - 使字符串反回文
    """
    from collections import Counter

    # 统计每个字符的出现次数
    char_count = Counter(s)

    # 将字符按出现次数从大到小排序
    sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))

    # 构建新的字符串
    new_str = []
    for char, count in sorted_chars:
        new_str.extend([char] * count)

    # 确保相邻字符不相同
    result = []
    for char in new_str:
        if not result or result[-1] != char:
            result.append(char)
        else:
            break
    else:
        return ''.join(result)

    # 如果无法构建非回文字符串，返回空字符串
    return ''


Solution = create_solution(solution_function_name)