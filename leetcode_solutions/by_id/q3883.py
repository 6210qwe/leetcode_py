# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3883
标题: Multiply Two Polynomials
难度: hard
链接: https://leetcode.cn/problems/multiply-two-polynomials/
题目类型: 数组、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3549. 两个多项式相乘 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用快速傅里叶变换 (FFT) 来实现多项式乘法。

算法步骤:
1. 将多项式的系数表示转换为点值表示（使用 FFT）。
2. 计算两个多项式的点值表示的逐点乘积。
3. 将结果从点值表示转换回系数表示（使用逆 FFT）。

关键点:
- FFT 和逆 FFT 的实现。
- 确保多项式的长度是 2 的幂次，以便进行 FFT。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是多项式的长度。
空间复杂度: O(n)，需要存储多项式的系数和点值表示。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
import cmath

def fft(a: List[complex], inverse: bool = False) -> List[complex]:
    """快速傅里叶变换 (FFT) 或逆 FFT"""
    n = len(a)
    if n == 1:
        return a
    w_n = cmath.exp((2j if inverse else -2j) * cmath.pi / n)
    even = fft(a[0::2], inverse)
    odd = fft(a[1::2], inverse)
    w = 1
    y = [0] * n
    for k in range(n // 2):
        t = w * odd[k]
        y[k] = even[k] + t
        y[k + n // 2] = even[k] - t
        w *= w_n
    return y

def multiply_polynomials(poly1: List[int], poly2: List[int]) -> List[int]:
    """
    多项式乘法
    """
    # 确保多项式的长度是 2 的幂次
    n = 1
    while n < len(poly1) + len(poly2) - 1:
        n <<= 1
    
    # 填充零以达到所需长度
    poly1 += [0] * (n - len(poly1))
    poly2 += [0] * (n - len(poly2))
    
    # 转换为复数列表
    poly1_complex = [complex(x, 0) for x in poly1]
    poly2_complex = [complex(x, 0) for x in poly2]
    
    # 进行 FFT
    fft_poly1 = fft(poly1_complex)
    fft_poly2 = fft(poly2_complex)
    
    # 计算点值表示的逐点乘积
    pointwise_product = [a * b for a, b in zip(fft_poly1, fft_poly2)]
    
    # 进行逆 FFT
    result_complex = fft(pointwise_product, inverse=True)
    
    # 转换回整数并四舍五入
    result = [round(x.real / n) for x in result_complex]
    
    # 去除多余的零
    while result and result[-1] == 0:
        result.pop()
    
    return result

Solution = create_solution(multiply_polynomials)