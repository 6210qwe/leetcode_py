# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1118
标题: Divide Array Into Increasing Sequences
难度: hard
链接: https://leetcode.cn/problems/divide-array-into-increasing-sequences/
题目类型: 数组、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1121. 将数组分成几个递增序列 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和计数器来划分数组

算法步骤:
1. 统计每个元素的频率。
2. 按照元素值从小到大排序。
3. 从最小的元素开始，尽可能多地分配到各个子序列中。
4. 如果当前元素无法分配，则返回 False。

关键点:
- 使用计数器统计频率。
- 每次尽可能多地分配当前元素到各个子序列中。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是数组的长度。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(n)，用于存储计数器和排序后的数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
from collections import Counter


def can_divide_into_increasing_sequences(nums: List[int], k: int) -> bool:
    """
    判断是否可以将数组分成 k 个递增序列
    """
    # 统计每个元素的频率
    counter = Counter(nums)
    
    # 按元素值从小到大排序
    sorted_nums = sorted(counter.keys())
    
    # 初始化 k 个空的子序列
    subsequences = [[] for _ in range(k)]
    
    for num in sorted_nums:
        count = counter[num]
        if count > k:
            return False  # 如果某个元素的频率大于 k，则无法分成 k 个递增序列
        
        # 尽可能多地分配当前元素到各个子序列中
        for i in range(count):
            for j in range(k):
                if not subsequences[j] or subsequences[j][-1] < num:
                    subsequences[j].append(num)
                    break
            else:
                return False  # 无法分配当前元素
    
    return True


Solution = create_solution(can_divide_into_increasing_sequences)