# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 510
标题: Count Subarrays With More Ones Than Zeros
难度: medium
链接: https://leetcode.cn/problems/count-subarrays-with-more-ones-than-zeros/
题目类型: 树状数组、线段树、数组、哈希表、二分查找、分治、有序集合、归并排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2031. 1 比 0 多的子数组个数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和 + 哈希表来统计满足条件的子数组数量。

算法步骤:
1. 初始化一个哈希表 `prefix_count` 用于记录每个前缀和出现的次数，初始时 `prefix_count[0] = 1`。
2. 遍历数组，计算当前前缀和 `current_sum`，如果遇到 1 则加 1，遇到 0 则减 1。
3. 对于每个前缀和 `current_sum`，统计所有小于 `current_sum` 的前缀和的数量，并累加到结果中。
4. 更新哈希表 `prefix_count` 中当前前缀和 `current_sum` 的计数。

关键点:
- 使用哈希表记录前缀和的出现次数，可以快速统计满足条件的子数组数量。
- 通过前缀和的差值来判断子数组中 1 的数量是否大于 0 的数量。
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


def count_subarrays_with_more_ones_than_zeros(nums: List[int]) -> int:
    """
    统计数组中 1 比 0 多的子数组个数。
    """
    prefix_count = {0: 1}
    current_sum = 0
    result = 0
    
    for num in nums:
        if num == 1:
            current_sum += 1
        else:
            current_sum -= 1
        
        # 统计所有小于 current_sum 的前缀和的数量
        for key in prefix_count:
            if key < current_sum:
                result += prefix_count[key]
        
        # 更新当前前缀和的计数
        if current_sum in prefix_count:
            prefix_count[current_sum] += 1
        else:
            prefix_count[current_sum] = 1
    
    return result


Solution = create_solution(count_subarrays_with_more_ones_than_zeros)