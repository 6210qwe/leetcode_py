# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 249
标题: Group Shifted Strings
难度: medium
链接: https://leetcode.cn/problems/group-shifted-strings/
题目类型: 数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
249. 移位字符串分组 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 将字符串归一化，相同归一化结果的字符串为一组

算法步骤:
1. 对每个字符串，计算相对第一个字符的偏移量
2. 归一化：将第一个字符设为'a'，其他字符相应调整
3. 使用哈希表分组

关键点:
- 字符串归一化
- 哈希表分组
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n*k) - n为字符串数，k为平均长度
空间复杂度: O(n*k) - 存储分组
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from collections import defaultdict
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def group_strings(strings: List[str]) -> List[List[str]]:
    """
    函数式接口 - 移位字符串分组
    
    实现思路:
    将字符串归一化，相同归一化结果的字符串为一组。
    
    Args:
        strings: 字符串数组
        
    Returns:
        分组后的字符串数组
        
    Example:
        >>> group_strings(["abc","bcd","acef","xyz","az","ba","a","z"])
        [['abc', 'bcd', 'xyz'], ['acef'], ['az', 'ba'], ['a', 'z']]
    """
    def normalize(s: str) -> str:
        """归一化字符串"""
        if not s:
            return s
        shift = ord(s[0]) - ord('a')
        result = []
        for char in s:
            normalized = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            result.append(normalized)
        return ''.join(result)
    
    groups = defaultdict(list)
    for s in strings:
        key = normalize(s)
        groups[key].append(s)
    
    return list(groups.values())


# 自动生成Solution类（无需手动编写）
Solution = create_solution(group_strings)
