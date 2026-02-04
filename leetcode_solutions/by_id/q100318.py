# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100318
标题: 交易逆序对的总数
难度: hard
链接: https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof/
题目类型: 树状数组、线段树、数组、二分查找、分治、有序集合、归并排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 170. 交易逆序对的总数 - 在股票交易中，如果前一天的股价高于后一天的股价，则可以认为存在一个「交易逆序对」。请设计一个程序，输入一段时间内的股票交易记录 record，返回其中存在的「交易逆序对」总数。 示例 1： 输入：record = [9, 7, 5, 4, 6] 输出：8 解释：交易中的逆序对为 (9, 7), (9, 5), (9, 4), (9, 6), (7, 5), (7, 4), (7, 6), (5, 4)。 提示： 0 <= record.length <= 50000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用归并排序来统计逆序对。归并排序在合并两个有序子数组时，可以通过比较和计数来统计逆序对。

算法步骤:
1. 将数组分成两半，递归地对每一半进行归并排序。
2. 在合并两个有序子数组时，统计逆序对的数量。
3. 合并两个有序子数组，并返回逆序对的总数。

关键点:
- 归并排序的时间复杂度为 O(n log n)，并且可以在合并过程中统计逆序对。
- 通过比较左右子数组的元素，可以高效地统计逆序对。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def merge_sort_and_count(nums, temp, left, right):
    if left >= right:
        return 0
    
    mid = (left + right) // 2
    count = merge_sort_and_count(nums, temp, left, mid) + merge_sort_and_count(nums, temp, mid + 1, right)
    
    i, j, pos = left, mid + 1, left
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            temp[pos] = nums[i]
            i += 1
        else:
            temp[pos] = nums[j]
            j += 1
            count += mid - i + 1
        pos += 1
    
    for k in range(i, mid + 1):
        temp[pos] = nums[k]
        pos += 1
    for k in range(j, right + 1):
        temp[pos] = nums[k]
        pos += 1
    
    nums[left:right+1] = temp[left:right+1]
    return count

def solution_function_name(record: List[int]) -> int:
    """
    函数式接口 - 使用归并排序统计逆序对
    """
    if not record:
        return 0
    temp = [0] * len(record)
    return merge_sort_and_count(record, temp, 0, len(record) - 1)

Solution = create_solution(solution_function_name)