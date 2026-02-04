# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 555
标题: Split Concatenated Strings
难度: medium
链接: https://leetcode.cn/problems/split-concatenated-strings/
题目类型: 贪心、数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
555. 分割连接字符串 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和字典来存储可能的前缀，然后逐个字符地构建字符串。

算法步骤:
1. 初始化一个字典 `prefixes` 来存储所有可能的前缀。
2. 遍历输入字符串 `s`，逐个字符地构建当前字符串 `current`。
3. 如果 `current` 在 `prefixes` 中且 `current` 不是某个更长字符串的前缀，则将其加入结果列表，并重置 `current`。
4. 更新 `prefixes` 字典，移除已经找到的字符串。

关键点:
- 使用字典来快速查找和更新前缀。
- 逐个字符地构建字符串，确保每个字符串都是尽可能短的有效字符串。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是输入字符串 s 的长度。我们只需要遍历一次字符串。
空间复杂度: O(m)，其中 m 是 words 数组中所有字符串的总长度。我们需要存储所有可能的前缀。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def split_concatenated_strings(s: str, words: List[str]) -> List[str]:
    """
    函数式接口 - 实现分割连接字符串
    """
    # 初始化前缀字典
    prefixes = {word[:i] for word in words for i in range(1, len(word) + 1)}
    
    result = []
    current = ""
    
    for char in s:
        current += char
        if current in prefixes and (len(current) == 1 or current[:-1] not in prefixes):
            result.append(current)
            current = ""
    
    return result


Solution = create_solution(split_concatenated_strings)