# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 248
标题: Strobogrammatic Number III
难度: hard
链接: https://leetcode.cn/problems/strobogrammatic-number-iii/
题目类型: 递归、数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
248. 中心对称数 III - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 递归构造所有中心对称数，统计在范围内的数量

算法步骤:
1. 递归构造所有可能的中心对称数
2. 检查每个数是否在[low, high]范围内
3. 统计数量

关键点:
- 递归构造
- 字符串比较判断范围
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(5^(n/2)) - n为数字长度
空间复杂度: O(n) - 递归栈空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def strobogrammatic_in_range(low: str, high: str) -> int:
    """
    函数式接口 - 中心对称数 III
    
    实现思路:
    递归构造所有中心对称数，统计在范围内的数量。
    
    Args:
        low: 下界
        high: 上界
        
    Returns:
        范围内的中心对称数数量
        
    Example:
        >>> strobogrammatic_in_range("50", "100")
        3
    """
    pairs = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]
    count = 0
    
    def build(length: int, current: str = '') -> None:
        """递归构造"""
        nonlocal count
        
        if length == 0:
            if len(current) >= len(low) and len(current) <= len(high):
                if (len(current) > len(low) or current >= low) and \
                   (len(current) < len(high) or current <= high):
                    count += 1
            return
        
        if length == 1:
            for mid in ['0', '1', '8']:
                num = current[:len(current)//2] + mid + current[len(current)//2:]
                if len(num) >= len(low) and len(num) <= len(high):
                    if (len(num) > len(low) or num >= low) and \
                       (len(num) < len(high) or num <= high):
                        count += 1
            return
        
        for left, right in pairs:
            if not current and left == '0':  # 不能以0开头
                continue
            build(length - 2, left + current + right)
    
    low_len, high_len = len(low), len(high)
    for length in range(low_len, high_len + 1):
        build(length)
    
    return count


# 自动生成Solution类（无需手动编写）
Solution = create_solution(strobogrammatic_in_range)
