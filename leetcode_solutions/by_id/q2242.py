# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2242
标题: Subsequence of Size K With the Largest Even Sum
难度: medium
链接: https://leetcode.cn/problems/subsequence-of-size-k-with-the-largest-even-sum/
题目类型: 贪心、数组、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2098. 长度为 K 的最大偶数和子序列 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过贪心算法选择最大的 k 个元素，并在必要时调整以确保总和为偶数。

算法步骤:
1. 对数组进行降序排序。
2. 选择前 k 个元素。
3. 如果这 k 个元素的和是偶数，直接返回这个和。
4. 否则，尝试用一个较小的偶数替换一个较大的奇数，或者用一个较小的奇数替换一个较大的偶数，以使总和变为偶数。

关键点:
- 通过排序和贪心选择最大的 k 个元素。
- 在必要时调整元素以确保总和为偶数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n) - 排序操作的时间复杂度。
空间复杂度: O(1) - 只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def solution_function_name(nums: List[int], k: int) -> int:
    """
    函数式接口 - 实现长度为 K 的最大偶数和子序列
    """
    # 对数组进行降序排序
    nums.sort(reverse=True)
    
    # 选择前 k 个元素
    selected = nums[:k]
    
    # 计算前 k 个元素的和
    total_sum = sum(selected)
    
    # 如果总和已经是偶数，直接返回
    if total_sum % 2 == 0:
        return total_sum
    
    # 否则，尝试调整元素以使总和为偶数
    first_odd = first_even = None
    for num in nums[k:]:
        if num % 2 == 0 and (first_even is None or num < first_even):
            first_even = num
        elif num % 2 != 0 and (first_odd is None or num < first_odd):
            first_odd = num
    
    # 尝试用一个较小的偶数替换一个较大的奇数
    if first_even is not None and first_odd is not None:
        for i in range(k):
            if selected[i] % 2 != 0:
                new_sum = total_sum - selected[i] + first_even
                if new_sum % 2 == 0:
                    return new_sum
                break
    
    # 尝试用一个较小的奇数替换一个较大的偶数
    if first_even is not None and first_odd is not None:
        for i in range(k):
            if selected[i] % 2 == 0:
                new_sum = total_sum - selected[i] + first_odd
                if new_sum % 2 == 0:
                    return new_sum
                break
    
    # 如果无法调整，则返回 -1
    return -1

Solution = create_solution(solution_function_name)