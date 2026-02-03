# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 339
标题: Nested List Weight Sum
难度: medium
链接: https://leetcode.cn/problems/nested-list-weight-sum/
题目类型: 深度优先搜索、广度优先搜索
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
339. 嵌套列表加权和 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: DFS递归，深度加权

算法步骤:
1. DFS遍历嵌套列表
2. 如果当前元素是整数，累加depth * integer
3. 如果当前元素是列表，递归处理，depth+1

关键点:
- DFS递归
- 深度加权
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - n为所有元素总数
空间复杂度: O(d) - d为最大深度
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def depth_sum(nested_list: List) -> int:
    """
    函数式接口 - 嵌套列表加权和
    
    实现思路:
    DFS递归：深度加权。
    
    Args:
        nested_list: 嵌套列表
        
    Returns:
        加权和
        
    Example:
        >>> depth_sum([[1,1],2,[1,1]])
        10
    """
    def dfs(items: List, depth: int) -> int:
        """DFS递归"""
        total = 0
        for item in items:
            if isinstance(item, int):
                total += item * depth
            else:
                total += dfs(item, depth + 1)
        return total
    
    return dfs(nested_list, 1)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(depth_sum)
