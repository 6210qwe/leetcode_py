# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100301
标题: 库存管理 III
难度: easy
链接: https://leetcode.cn/problems/zui-xiao-de-kge-shu-lcof/
题目类型: 数组、分治、快速选择、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 159. 库存管理 III - 仓库管理员以数组 stock 形式记录商品库存表，其中 stock[i] 表示对应商品库存余量。请返回库存余量最少的 cnt 个商品余量，返回 顺序不限。 示例 1： 输入：stock = [2,5,7,4], cnt = 1 输出：[2] 示例 2： 输入：stock = [0,2,3,6], cnt = 2 输出：[0,2] 或 [2,0] 提示： * 0 <= cnt <= stock.length <= 10000 * 0 <= stock[i] <= 10000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用快速选择算法找到第 k 小的元素，然后返回前 k 个最小的元素。

算法步骤:
1. 使用快速选择算法在 O(n) 的期望时间复杂度内找到第 k 小的元素。
2. 返回数组中所有小于等于第 k 小的元素。

关键点:
- 快速选择算法的时间复杂度在期望情况下是 O(n)，最坏情况下是 O(n^2)。
- 通过随机化选择主元可以有效避免最坏情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) 期望时间复杂度
空间复杂度: O(1) 原地操作
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
import random

def partition(arr: List[int], low: int, high: int) -> int:
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr: List[int], low: int, high: int, k: int) -> int:
    if low == high:
        return arr[low]
    pivot_index = partition(arr, low, high)
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, low, pivot_index - 1, k)
    else:
        return quickselect(arr, pivot_index + 1, high, k)

def solution_function_name(stock: List[int], cnt: int) -> List[int]:
    """
    函数式接口 - 使用快速选择算法找到库存余量最少的 cnt 个商品余量
    """
    if cnt == 0:
        return []
    n = len(stock)
    kth_smallest = quickselect(stock, 0, n - 1, cnt - 1)
    return [num for num in stock if num <= kth_smallest]

Solution = create_solution(solution_function_name)