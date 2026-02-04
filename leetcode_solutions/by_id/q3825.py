# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3825
标题: Apply Substitutions
难度: medium
链接: https://leetcode.cn/problems/apply-substitutions/
题目类型: 深度优先搜索、广度优先搜索、图、拓扑排序、数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3481. 应用替换 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用递归和记忆化搜索来处理字符串的替换。

算法步骤:
1. 构建一个字典，将每个模式映射到其对应的替换字符串。
2. 定义一个递归函数 `dfs`，该函数接受当前字符串作为参数，并返回替换后的结果。
3. 在递归函数中，遍历所有可能的模式匹配位置，如果找到匹配，则递归处理剩余部分。
4. 使用记忆化搜索来避免重复计算。

关键点:
- 使用字典快速查找模式及其替换字符串。
- 递归处理字符串的替换，确保所有可能的替换都被考虑。
- 使用记忆化搜索优化性能。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是字符串长度，m 是模式的数量。每个字符最多被处理一次。
空间复杂度: O(n * m)，记忆化搜索需要存储中间结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
from functools import lru_cache

def apply_substitutions(s: str, sub: List[List[str]]) -> str:
    """
    函数式接口 - 应用替换
    """
    # 构建模式到替换字符串的映射
    pattern_to_replacement = {pattern: replacement for pattern, replacement in sub}
    
    @lru_cache(maxsize=None)
    def dfs(current_s: str) -> str:
        if not current_s:
            return ""
        
        result = ""
        i = 0
        while i < len(current_s):
            found = False
            for pattern in pattern_to_replacement:
                if current_s.startswith(pattern, i):
                    result += pattern_to_replacement[pattern]
                    i += len(pattern)
                    found = True
                    break
            if not found:
                result += current_s[i]
                i += 1
        return result
    
    return dfs(s)

Solution = create_solution(apply_substitutions)