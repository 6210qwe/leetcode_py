# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 159
标题: Longest Substring with At Most Two Distinct Characters
难度: medium
链接: https://leetcode.cn/problems/longest-substring-with-at-most-two-distinct-characters/
题目类型: 哈希表、字符串、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
159. 至多包含两个不同字符的最长子串 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口，维护窗口内最多两个不同字符

算法步骤:
1. 使用左右指针维护滑动窗口
2. 使用哈希表记录字符出现次数
3. 当窗口内不同字符数超过2时，移动左指针
4. 更新最大长度

关键点:
- 滑动窗口维护最多两个不同字符
- 时间复杂度O(n)，空间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要遍历字符串一次
空间复杂度: O(1) - 哈希表最多存储2个字符
"""

# ============================================================================
# 代码实现
# ============================================================================

from collections import defaultdict
from leetcode_solutions.utils.solution import create_solution


def longest_substring_with_at_most_two_distinct_characters(s: str) -> int:
    """
    函数式接口 - 至多包含两个不同字符的最长子串
    
    实现思路:
    使用滑动窗口，维护窗口内最多两个不同字符。
    
    Args:
        s: 输入字符串
        
    Returns:
        最长子串的长度
        
    Example:
        >>> longest_substring_with_at_most_two_distinct_characters("eceba")
        3
    """
    if not s:
        return 0
    
    left = 0
    char_count = defaultdict(int)
    max_len = 0
    
    for right in range(len(s)):
        char_count[s[right]] += 1
        
        while len(char_count) > 2:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len


# 自动生成Solution类（无需手动编写）
Solution = create_solution(longest_substring_with_at_most_two_distinct_characters)
