# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 340
标题: Longest Substring with At Most K Distinct Characters
难度: medium
链接: https://leetcode.cn/problems/longest-substring-with-at-most-k-distinct-characters/
题目类型: 哈希表、字符串、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
340. 至多包含 K 个不同字符的最长子串 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 滑动窗口，维护窗口内不同字符数

算法步骤:
1. 使用滑动窗口
2. 使用哈希表统计字符频率
3. 当不同字符数>k时，缩小窗口

关键点:
- 滑动窗口
- 哈希表统计
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - n为字符串长度
空间复杂度: O(k) - 哈希表空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from collections import defaultdict
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    """
    函数式接口 - 至多包含 K 个不同字符的最长子串
    
    实现思路:
    滑动窗口：维护窗口内不同字符数。
    
    Args:
        s: 字符串
        k: 不同字符数限制
        
    Returns:
        最长子串长度
        
    Example:
        >>> length_of_longest_substring_k_distinct("eceba", 2)
        3
    """
    if k == 0:
        return 0
    
    char_count = defaultdict(int)
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        char_count[s[right]] += 1
        
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len


# 自动生成Solution类（无需手动编写）
Solution = create_solution(length_of_longest_substring_k_distinct)
