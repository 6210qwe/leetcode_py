# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1230
标题: Maximum of Absolute Value Expression
难度: medium
链接: https://leetcode.cn/problems/maximum-of-absolute-value-expression/
题目类型: 数组、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1131. 绝对值表达式的最大值 - 给你两个长度相等的整数数组，返回下面表达式的最大值： |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j| 其中下标 i，j 满足 0 <= i, j < arr1.length。 示例 1： 输入：arr1 = [1,2,3,4], arr2 = [-1,4,5,6] 输出：13 示例 2： 输入：arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4] 输出：20 提示： * 2 <= arr1.length == arr2.length <= 40000 * -10^6 <= arr1[i], arr2[i] <= 10^6
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过将绝对值表达式拆分为四个可能的情况，分别计算每种情况下的最大值和最小值，然后取差值的最大值。

算法步骤:
1. 定义四个数组，分别存储 arr1[i] + arr2[i] + i, arr1[i] + arr2[i] - i, arr1[i] - arr2[i] + i, arr1[i] - arr2[i] - i。
2. 遍历输入数组，填充这四个数组。
3. 对于每个数组，计算其最大值和最小值，并计算它们的差值。
4. 返回这些差值中的最大值。

关键点:
- 通过拆分绝对值表达式，将其转化为四个线性表达式，从而简化计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_abs_val_expr(arr1: List[int], arr2: List[int]) -> int:
    """
    函数式接口 - 计算绝对值表达式的最大值
    """
    n = len(arr1)
    a1, a2, a3, a4 = [], [], [], []
    
    for i in range(n):
        a1.append(arr1[i] + arr2[i] + i)
        a2.append(arr1[i] + arr2[i] - i)
        a3.append(arr1[i] - arr2[i] + i)
        a4.append(arr1[i] - arr2[i] - i)
    
    max_diff = 0
    for a in [a1, a2, a3, a4]:
        max_val = max(a)
        min_val = min(a)
        max_diff = max(max_diff, max_val - min_val)
    
    return max_diff


Solution = create_solution(max_abs_val_expr)