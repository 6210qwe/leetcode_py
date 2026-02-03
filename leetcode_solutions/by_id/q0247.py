# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 247
标题: Strobogrammatic Number II
难度: medium
链接: https://leetcode.cn/problems/strobogrammatic-number-ii/
题目类型: 递归、数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
247. 中心对称数 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 递归构造，中心对称数的特点

算法步骤:
1. 定义中心对称数字对：0-0, 1-1, 6-9, 8-8, 9-6
2. 递归构造：从中间向两边扩展
3. 注意：0不能作为开头（除非n==1）

关键点:
- 递归构造
- 处理奇偶长度
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(5^(n/2)) - 每个位置有5种选择
空间复杂度: O(n) - 递归栈空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_strobogrammatic(n: int) -> List[str]:
    """
    函数式接口 - 中心对称数 II
    
    实现思路:
    递归构造中心对称数。
    
    Args:
        n: 数字长度
        
    Returns:
        所有长度为n的中心对称数
        
    Example:
        >>> find_strobogrammatic(2)
        ['11', '69', '88', '96']
    """
    pairs = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]
    
    def build(length: int) -> List[str]:
        """递归构造"""
        if length == 0:
            return ['']
        if length == 1:
            return ['0', '1', '8']
        
        result = []
        for left, right in pairs:
            if length == n and left == '0':  # 不能以0开头
                continue
            for mid in build(length - 2):
                result.append(left + mid + right)
        
        return result
    
    return build(n)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(find_strobogrammatic)
