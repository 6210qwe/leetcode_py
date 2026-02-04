# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1276
标题: Closest Divisors
难度: medium
链接: https://leetcode.cn/problems/closest-divisors/
题目类型: 数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1362. 最接近的因数 - 给你一个整数 num，请你找出同时满足下面全部要求的两个整数： * 两数乘积等于 num + 1 或 num + 2 * 以绝对差进行度量，两数大小最接近 你可以按任意顺序返回这两个整数。 示例 1： 输入：num = 8 输出：[3,3] 解释：对于 num + 1 = 9，最接近的两个因数是 3 & 3；对于 num + 2 = 10, 最接近的两个因数是 2 & 5，因此返回 3 & 3 。 示例 2： 输入：num = 123 输出：[5,25] 示例 3： 输入：num = 999 输出：[40,25] 提示： * 1 <= num <= 10^9
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 找到 num + 1 和 num + 2 的所有因数对，并选择其中绝对差最小的一对。

算法步骤:
1. 计算 num + 1 和 num + 2。
2. 对于每个值，从 1 到 sqrt(value) 进行遍历，找到所有的因数对。
3. 选择绝对差最小的因数对。

关键点:
- 通过只遍历到 sqrt(value)，可以减少不必要的计算。
- 保持代码简洁和可读性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(sqrt(n))
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def closest_divisors(num: int) -> List[int]:
    """
    函数式接口 - 找到 num + 1 和 num + 2 的最接近因数对
    """
    def find_closest_factors(value: int) -> List[int]:
        for i in range(int(value ** 0.5), 0, -1):
            if value % i == 0:
                return [i, value // i]
        return [1, value]

    factors1 = find_closest_factors(num + 1)
    factors2 = find_closest_factors(num + 2)

    if abs(factors1[0] - factors1[1]) < abs(factors2[0] - factors2[1]):
        return factors1
    else:
        return factors2


Solution = create_solution(closest_divisors)