# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3111
标题: Smallest Number With Given Digit Product
难度: medium
链接: https://leetcode.cn/problems/smallest-number-with-given-digit-product/
题目类型: 贪心、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2847. 给定数字乘积的最小数字 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，从最大的因子开始构建最小的数字。

算法步骤:
1. 从 9 到 2 枚举每个因子，尽可能多地将 product 分解为这些因子。
2. 将这些因子按从小到大的顺序排列，形成最小的数字。
3. 如果 product 仍然大于 1，则将其放在最前面。

关键点:
- 从 9 到 2 枚举因子，确保生成的数字最小。
- 如果 product 仍然大于 1，说明 product 是一个质数或剩余部分是质数，直接放在最前面。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log(product))，因为每次循环都会将 product 除以一个因子。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def smallest_number_with_given_digit_product(product: int) -> str:
    """
    函数式接口 - 实现给定数字乘积的最小数字
    """
    if product == 0:
        return "10"
    
    factors = []
    for i in range(9, 1, -1):
        while product % i == 0:
            factors.append(i)
            product //= i
    
    if product > 1:
        factors.append(product)
    
    factors.sort()
    return ''.join(map(str, factors))


Solution = create_solution(smallest_number_with_given_digit_product)