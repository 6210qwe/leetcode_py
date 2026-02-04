# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 4050
标题: Minimum Index Sum of Common Elements
难度: medium
链接: https://leetcode.cn/problems/minimum-index-sum-of-common-elements/
题目类型: 数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3682. 公共元素的最小索引和 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个哈希表分别记录每个列表中元素的索引，然后遍历其中一个哈希表，找到共同元素并计算其索引和，最后返回索引和最小的元素。

算法步骤:
1. 创建两个哈希表，分别记录 list1 和 list2 中每个元素的索引。
2. 遍历第一个哈希表，找到在第二个哈希表中存在的元素，并计算其索引和。
3. 记录最小的索引和及其对应的元素。
4. 返回结果。

关键点:
- 使用哈希表可以快速查找元素的索引。
- 通过遍历一个哈希表来找到共同元素，避免了双重循环。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 和 m 分别是 list1 和 list2 的长度。
空间复杂度: O(n + m)，用于存储两个哈希表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_restaurant(list1: List[str], list2: List[str]) -> List[str]:
    """
    函数式接口 - 找到公共元素的最小索引和
    """
    # 创建两个哈希表，分别记录 list1 和 list2 中每个元素的索引
    index_map1 = {restaurant: i for i, restaurant in enumerate(list1)}
    index_map2 = {restaurant: i for i, restaurant in enumerate(list2)}

    # 用于存储最小索引和及其对应的元素
    min_sum = float('inf')
    result = []

    # 遍历第一个哈希表，找到在第二个哈希表中存在的元素，并计算其索引和
    for restaurant, i in index_map1.items():
        if restaurant in index_map2:
            j = index_map2[restaurant]
            index_sum = i + j
            if index_sum < min_sum:
                min_sum = index_sum
                result = [restaurant]
            elif index_sum == min_sum:
                result.append(restaurant)

    return result


Solution = create_solution(find_restaurant)