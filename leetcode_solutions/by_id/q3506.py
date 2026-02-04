# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3506
标题: Count Triplets with Even XOR Set Bits I
难度: easy
链接: https://leetcode.cn/problems/count-triplets-with-even-xor-set-bits-i/
题目类型: 位运算、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3199. 用偶数异或设置位计数三元组 I - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用位运算和组合数学来计算满足条件的三元组数量。

算法步骤:
1. 计算每个元素的二进制表示中1的个数。
2. 统计每个1的个数出现的频率。
3. 根据组合数学公式计算满足条件的三元组数量。

关键点:
- 使用位运算快速计算每个元素的1的个数。
- 利用组合数学公式减少计算量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_triplets(arr: List[int]) -> int:
    """
    函数式接口 - 计算满足条件的三元组数量
    """
    # 计算每个元素的二进制表示中1的个数
    bit_counts = [bin(num).count('1') for num in arr]
    
    # 统计每个1的个数出现的频率
    freq = [0] * 32
    for count in bit_counts:
        freq[count] += 1
    
    # 计算满足条件的三元组数量
    result = 0
    for i in range(32):
        for j in range(i, 32):
            k = 31 - (i + j)
            if k >= 0 and k <= 31:
                if i == j and j == k:
                    result += freq[i] * (freq[i] - 1) * (freq[i] - 2) // 6
                elif i == j:
                    result += freq[i] * (freq[i] - 1) // 2 * freq[k]
                elif j == k:
                    result += freq[j] * (freq[j] - 1) // 2 * freq[i]
                else:
                    result += freq[i] * freq[j] * freq[k]
    
    return result


Solution = create_solution(count_triplets)