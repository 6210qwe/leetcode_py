# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 254
标题: Factor Combinations
难度: medium
链接: https://leetcode.cn/problems/factor-combinations/
题目类型: 回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
254. 因子的组合 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 回溯算法，枚举所有因子组合

算法步骤:
1. 从start开始枚举因子
2. 如果n能被i整除，将i加入组合
3. 递归处理n//i，从i开始（保证非递减）
4. 当n==1且组合长度>1时，加入结果

关键点:
- 回溯枚举因子
- 保证因子非递减
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(sqrt(n) * k) - k为组合数
空间复杂度: O(log n) - 递归栈空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def get_factors(n: int) -> List[List[int]]:
    """
    函数式接口 - 因子的组合
    
    实现思路:
    回溯算法：枚举所有因子组合。
    
    Args:
        n: 目标数字
        
    Returns:
        所有因子组合
        
    Example:
        >>> get_factors(12)
        [[2, 6], [2, 2, 3], [3, 4]]
    """
    result = []
    
    def backtrack(start: int, n: int, path: List[int]):
        """回溯函数"""
        if n == 1:
            if len(path) > 1:
                result.append(path[:])
            return
        
        for i in range(start, int(n**0.5) + 1):
            if n % i == 0:
                path.append(i)
                backtrack(i, n // i, path)
                path.pop()
        
        # 添加n本身作为因子
        if n >= start:
            path.append(n)
            backtrack(n, 1, path)
            path.pop()
    
    backtrack(2, n, [])
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(get_factors)
