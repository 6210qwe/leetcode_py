# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2747
标题: Apply Transform Over Each Element in Array
难度: easy
链接: https://leetcode.cn/problems/apply-transform-over-each-element-in-array/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2635. 转换数组中的每个元素 - 编写一个函数，这个函数接收一个整数数组 arr 和一个映射函数 fn ，通过该映射函数返回一个新的数组。 返回数组的创建语句应为 returnedArray[i] = fn(arr[i], i) 。 请你在不使用内置方法 Array.map 的前提下解决这个问题。 示例 1: 输入：arr = [1,2,3], fn = function plusone(n) { return n + 1; } 输出：[2,3,4] 解释： const newArray = map(arr, plusone); // [2,3,4] 此映射函数返回值是将数组中每个元素的值加 1。 示例 2: 输入：arr = [1,2,3], fn = function plusI(n, i) { return n + i; } 输出：[1,3,5] 解释：此映射函数返回值根据输入数组索引增加每个值。 示例 3: 输入：arr = [10,20,30], fn = function constant() { return 42; } 输出：[42,42,42] 解释：此映射函数返回值恒为 42。 提示： * 0 <= arr.length <= 1000 * -109 <= arr[i] <= 109 * fn 返回一个整数。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个简单的循环来遍历数组，并应用映射函数。

算法步骤:
1. 初始化一个空的结果数组 `result`。
2. 遍历输入数组 `arr`，对于每个元素 `arr[i]`，调用映射函数 `fn(arr[i], i)` 并将结果添加到 `result` 中。
3. 返回结果数组 `result`。

关键点:
- 不使用内置方法 `Array.map`，而是使用简单的循环来实现。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组 `arr` 的长度。我们需要遍历整个数组一次。
空间复杂度: O(n)，结果数组 `result` 的空间复杂度为 O(n)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(arr: List[int], fn):
    """
    函数式接口 - 实现转换数组中的每个元素
    """
    result = []
    for i in range(len(arr)):
        result.append(fn(arr[i], i))
    return result


Solution = create_solution(solution_function_name)