# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 367
标题: Valid Perfect Square
难度: easy
链接: https://leetcode.cn/problems/valid-perfect-square/
题目类型: 数学、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
367. 有效的完全平方数 - 给你一个正整数 num 。如果 num 是一个完全平方数，则返回 true ，否则返回 false 。 完全平方数 是一个可以写成某个整数的平方的整数。换句话说，它可以写成某个整数和自身的乘积。 不能使用任何内置的库函数，如 sqrt 。 示例 1： 输入：num = 16 输出：true 解释：返回 true ，因为 4 * 4 = 16 且 4 是一个整数。 示例 2： 输入：num = 14 输出：false 解释：返回 false ，因为 3.742 * 3.742 = 14 但 3.742 不是一个整数。 提示： * 1 <= num <= 231 - 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 二分查找

算法步骤:
1. 在[1, num]范围内使用二分查找
2. 计算mid的平方，与num比较
3. 如果mid*mid == num，返回True
4. 如果mid*mid < num，搜索右半部分
5. 如果mid*mid > num，搜索左半部分

关键点:
- 使用二分查找避免溢出
- 注意整数溢出问题
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(logn) - 二分查找
空间复杂度: O(1) - 只使用常数空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def is_perfect_square(num: int) -> bool:
    """
    函数式接口 - 有效的完全平方数
    
    实现思路:
    使用二分查找在[1, num]范围内查找平方根。
    
    Args:
        num: 正整数
        
    Returns:
        是否为完全平方数
        
    Example:
        >>> is_perfect_square(16)
        True
    """
    if num < 2:
        return True
    
    left, right = 1, num // 2
    
    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid
        
        if square == num:
            return True
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1
    
    return False


# 自动生成Solution类（无需手动编写）
Solution = create_solution(is_perfect_square)
