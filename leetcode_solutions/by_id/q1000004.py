# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000004
标题: Pattern Matching LCCI
难度: medium
链接: https://leetcode.cn/problems/pattern-matching-lcci/
题目类型: 数学、字符串、回溯、枚举
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 16.18. 模式匹配 - 你有两个字符串，即pattern和value。 pattern字符串由字母"a"和"b"组成，用于描述字符串中的模式。例如，字符串"catcatgocatgo"匹配模式"aabab"（其中"cat"是"a"，"go"是"b"），该字符串也匹配像"a"、"ab"和"b"这样的模式。但需注意"a"和"b"不能同时表示相同的字符串。编写一个方法判断value字符串是否匹配pattern字符串。 示例 1： 输入： pattern = "abba", value = "dogcatcatdog" 输出： true 示例 2： 输入： pattern = "abba", value = "dogcatcatfish" 输出： false 示例 3： 输入： pattern = "aaaa", value = "dogcatcatdog" 输出： false 示例 4： 输入： pattern = "abba", value = "dogdogdogdog" 输出： true 解释： "a"="dogdog",b=""，反之也符合规则 提示： * 1 <= len(pattern) <= 1000 * 0 <= len(value) <= 1000 * 你可以假设pattern只包含字母"a"和"b"，value仅包含小写字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用回溯法尝试所有可能的分段方式，检查是否满足条件。

算法步骤:
1. 统计 pattern 中 'a' 和 'b' 的数量。
2. 尝试不同的长度组合，分别表示 'a' 和 'b' 对应的子串。
3. 对每种组合，检查 value 是否可以被分割成对应的子串，并且这些子串是否满足 pattern 的要求。
4. 如果找到一种满足条件的组合，则返回 True；否则返回 False。

关键点:
- 回溯法尝试所有可能的分段方式。
- 通过预处理减少不必要的尝试。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 * m)，其中 n 是 value 的长度，m 是 pattern 的长度。
空间复杂度: O(m + n)，用于存储递归调用栈和临时变量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def match_pattern(pattern: str, value: str) -> bool:
    def backtrack(a_count: int, b_count: int, a_len: int, b_len: int, index: int) -> bool:
        if a_count == 0 and b_count == 0:
            return index == len(value)
        
        if index >= len(value):
            return False
        
        if a_count > 0:
            if (index + a_len <= len(value) and 
                (not a or value[index:index + a_len] == a) and 
                backtrack(a_count - 1, b_count, a_len, b_len, index + a_len)):
                return True
            if not a:
                a = value[index:index + a_len]
        
        if b_count > 0:
            if (index + b_len <= len(value) and 
                (not b or value[index:index + b_len] == b) and 
                backtrack(a_count, b_count - 1, a_len, b_len, index + b_len)):
                return True
            if not b:
                b = value[index:index + b_len]
        
        return False
    
    a_count = pattern.count('a')
    b_count = pattern.count('b')
    
    for a_len in range(0, len(value) // max(a_count, 1) + 1):
        for b_len in range(0, len(value) // max(b_count, 1) + 1):
            a, b = None, None
            if backtrack(a_count, b_count, a_len, b_len, 0) and a != b:
                return True
    
    return False

Solution = create_solution(match_pattern)