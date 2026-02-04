# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1141
标题: How Many Apples Can You Put into the Basket
难度: easy
链接: https://leetcode.cn/problems/how-many-apples-can-you-put-into-the-basket/
题目类型: 贪心、数组、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1196. 最多可以买到的苹果数量 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过贪心算法选择尽可能多的不同类型的苹果。

算法步骤:
1. 统计每种苹果的数量，并按数量从大到小排序。
2. 依次选择最多 k 种不同类型的苹果，直到不能再选择为止。

关键点:
- 优先选择数量最多的苹果种类。
- 使用贪心策略确保选择的苹果种类数最多。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是数组的长度。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(1)，除了输入和输出外，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def maxNumberOfApples(arr: List[int], k: int) -> int:
    """
    函数式接口 - 计算最多可以放入篮子中的苹果数量
    """
    # 统计每种苹果的数量
    apple_count = {}
    for apple in arr:
        if apple in apple_count:
            apple_count[apple] += 1
        else:
            apple_count[apple] = 1
    
    # 按数量从大到小排序
    sorted_apples = sorted(apple_count.items(), key=lambda x: x[1], reverse=True)
    
    total_apples = 0
    selected_types = 0
    
    # 依次选择最多 k 种不同类型的苹果
    for apple, count in sorted_apples:
        if selected_types < k:
            total_apples += count
            selected_types += 1
        else:
            break
    
    return total_apples


Solution = create_solution(maxNumberOfApples)