# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000021
标题: Smallest K LCCI
难度: medium
链接: https://leetcode.cn/problems/smallest-k-lcci/
题目类型: 数组、分治、快速选择、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 17.14. 最小K个数 - 设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。 示例： 输入： arr = [1,3,5,7,2,4,6,8], k = 4 输出： [1,2,3,4] 提示： * 0 <= len(arr) <= 100000 * 0 <= k <= min(100000, len(arr))
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用快速选择算法来找到第 k 小的元素，然后返回前 k 个元素。

算法步骤:
1. 使用快速选择算法对数组进行部分排序，使得前 k 个元素是数组中最小的 k 个元素。
2. 返回前 k 个元素。

关键点:
- 快速选择算法的时间复杂度在平均情况下为 O(n)，最坏情况下为 O(n^2)，但可以通过随机化来避免最坏情况。
- 快速选择算法的空间复杂度为 O(1)。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) 平均情况，O(n^2) 最坏情况
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(arr: List[int], k: int) -> List[int]:
    """
    函数式接口 - 使用快速选择算法找到数组中最小的 k 个数
    """
    if k == 0 or not arr:
        return []

    def partition(left: int, right: int) -> int:
        pivot_index = left + (right - left) // 2
        pivot = arr[pivot_index]
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        store_index = left
        for i in range(left, right):
            if arr[i] < pivot:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1
        arr[store_index], arr[right] = arr[right], arr[store_index]
        return store_index

    def quick_select(left: int, right: int, k: int) -> None:
        if left >= right:
            return
        pivot_index = partition(left, right)
        if pivot_index == k:
            return
        elif pivot_index < k:
            quick_select(pivot_index + 1, right, k)
        else:
            quick_select(left, pivot_index - 1, k)

    quick_select(0, len(arr) - 1, k - 1)
    return arr[:k]


Solution = create_solution(solution_function_name)