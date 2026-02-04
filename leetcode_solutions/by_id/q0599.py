# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 599
标题: Minimum Index Sum of Two Lists
难度: easy
链接: https://leetcode.cn/problems/minimum-index-sum-of-two-lists/
题目类型: 数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
599. 两个列表的最小索引总和 - 给定两个字符串数组 list1 和 list2，找到 索引和最小的公共字符串。 公共字符串 是同时出现在 list1 和 list2 中的字符串。 具有 最小索引和的公共字符串 是指，如果它在 list1[i] 和 list2[j] 中出现，那么 i + j 应该是所有其他 公共字符串 中的最小值。 返回所有 具有最小索引和的公共字符串。以 任何顺序 返回答案。 示例 1: 输入: list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]，list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"] 输出: ["Shogun"] 解释: 唯一的公共字符串是 “Shogun”。 示例 2: 输入:list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]，list2 = ["KFC", "Shogun", "Burger King"] 输出: ["Shogun"] 解释: 具有最小索引和的公共字符串是 “Shogun”，它有最小的索引和 = (0 + 1) = 1。 示例 3： 输入：list1 = ["happy","sad","good"], list2 = ["sad","happy","good"] 输出：["sad","happy"] 解释：有三个公共字符串： "happy" 索引和 = (0 + 1) = 1. "sad" 索引和 = (1 + 0) = 1. "good" 索引和 = (2 + 2) = 4. 最小索引和的字符串是 "sad" 和 "happy"。 提示: * 1 <= list1.length, list2.length <= 1000 * 1 <= list1[i].length, list2[i].length <= 30 * list1[i] 和 list2[i] 由空格 ' ' 和英文字母组成。 * list1 的所有字符串都是 唯一 的。 * list2 中的所有字符串都是 唯一 的。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表记录每个字符串在 list1 中的索引，然后遍历 list2，找到公共字符串并计算其索引和，记录最小索引和的公共字符串。

算法步骤:
1. 创建一个哈希表，记录 list1 中每个字符串及其索引。
2. 初始化一个变量来记录当前最小的索引和，以及一个列表来存储结果。
3. 遍历 list2，对于每个字符串，如果它在哈希表中存在，则计算其索引和。
4. 如果当前索引和小于已记录的最小索引和，则更新最小索引和，并清空结果列表，将当前字符串加入结果列表。
5. 如果当前索引和等于已记录的最小索引和，则将当前字符串加入结果列表。
6. 返回结果列表。

关键点:
- 使用哈希表可以快速查找公共字符串及其索引。
- 通过一次遍历 list2 即可找到所有具有最小索引和的公共字符串。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 list1 的长度，m 是 list2 的长度。
空间复杂度: O(n)，需要额外的空间来存储 list1 中每个字符串及其索引。
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
    函数式接口 - 找到两个列表中具有最小索引和的公共字符串
    """
    # 创建一个哈希表，记录 list1 中每个字符串及其索引
    index_map = {restaurant: i for i, restaurant in enumerate(list1)}
    
    # 初始化最小索引和为无穷大，结果列表为空
    min_index_sum = float('inf')
    result = []
    
    # 遍历 list2
    for j, restaurant in enumerate(list2):
        if restaurant in index_map:
            # 计算当前字符串的索引和
            index_sum = index_map[restaurant] + j
            if index_sum < min_index_sum:
                # 更新最小索引和，清空结果列表，添加当前字符串
                min_index_sum = index_sum
                result = [restaurant]
            elif index_sum == min_index_sum:
                # 如果当前索引和等于最小索引和，添加当前字符串到结果列表
                result.append(restaurant)
    
    return result


Solution = create_solution(find_restaurant)