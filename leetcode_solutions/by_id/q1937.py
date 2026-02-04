# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1937
标题: Maximize the Beauty of the Garden
难度: hard
链接: https://leetcode.cn/problems/maximize-the-beauty-of-the-garden/
题目类型: 贪心、数组、哈希表、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1788. 最大化花园的美观度 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和前缀和来最大化花园的美观度。

算法步骤:
1. 计算每个位置的前缀和，记录每种颜色在当前位置之前的数量。
2. 从右向左遍历数组，维护一个计数器来记录每种颜色的数量。
3. 对于每个位置，找到当前可以放置的最大颜色值，并更新答案。

关键点:
- 使用前缀和来快速计算每种颜色的数量。
- 从右向左遍历以确保每个位置都能选择到最大可能的颜色值。
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


def maximize_beauty(flowers: List[int]) -> int:
    """
    函数式接口 - 实现最大化花园的美观度
    """
    n = len(flowers)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + flowers[i]
    
    color_count = [0] * 50001
    max_beauty = 0
    current_beauty = 0
    
    for i in range(n - 1, -1, -1):
        current_beauty += color_count[flowers[i]]
        color_count[flowers[i]] += 1
        max_beauty = max(max_beauty, current_beauty)
    
    return max_beauty


Solution = create_solution(maximize_beauty)