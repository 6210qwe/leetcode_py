# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 288
标题: Unique Word Abbreviation
难度: medium
链接: https://leetcode.cn/problems/unique-word-abbreviation/
题目类型: 设计、数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
288. 单词的唯一缩写 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 哈希表存储缩写和对应的单词集合

算法步骤:
1. 计算每个单词的缩写
2. 使用哈希表存储缩写->单词集合
3. isUnique检查缩写是否唯一

关键点:
- 哈希表存储
- 时间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - n为单词数
空间复杂度: O(n) - 哈希表空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from collections import defaultdict
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def valid_word_abbr_class(dictionary: List[str]):
    """
    函数式接口 - 单词的唯一缩写
    
    实现思路:
    哈希表存储缩写和对应的单词集合。
    
    Args:
        dictionary: 单词字典
        
    Returns:
        ValidWordAbbr类
        
    Example:
        >>> vwa = valid_word_abbr_class(["deer", "door", "cake", "card"])
        >>> vwa.isUnique("dear")
        False
    """
    class ValidWordAbbr:
        def __init__(self, dictionary: List[str]):
            self.abbr_map = defaultdict(set)
            for word in dictionary:
                abbr = self.get_abbr(word)
                self.abbr_map[abbr].add(word)
        
        def get_abbr(self, word: str) -> str:
            """获取单词的缩写"""
            if len(word) <= 2:
                return word
            return word[0] + str(len(word) - 2) + word[-1]
        
        def isUnique(self, word: str) -> bool:
            """检查单词的缩写是否唯一"""
            abbr = self.get_abbr(word)
            words = self.abbr_map[abbr]
            # 如果缩写不存在，或者只对应当前单词
            return len(words) == 0 or (len(words) == 1 and word in words)
    
    return ValidWordAbbr(dictionary)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(valid_word_abbr_class)
