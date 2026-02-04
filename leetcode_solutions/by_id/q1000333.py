# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000333
标题: 山脉数组的峰顶索引
难度: easy
链接: https://leetcode.cn/problems/B1IidL/
题目类型: 数组、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 069. 山脉数组的峰顶索引 - 符合下列属性的数组 arr 称为 山峰数组（山脉数组） ： * arr.length >= 3 * 存在 i（0 < i < arr.length - 1）使得： * arr[0] < arr[1] < ... arr[i-1] < arr[i] * arr[i] > arr[i+1] > ... > arr[arr.length - 1] 给定由整数组成的山峰数组 arr ，返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 的下标 i ，即山峰顶部。 示例 1： 输入：arr = [0,1,0] 输出：1 示例 2： 输入：arr = [1,3,5,4,2] 输出：2 示例 3： 输入：arr = [0,10,5,2] 输出：1 示例 4： 输入：arr = [3,4,5,1] 输出：2 示例 5： 输入：arr = [24,69,100,99,79,78,67,36,26,19] 输出：2 提示： * 3 <= arr.length <= 104 * 0 <= arr[i] <= 106 * 题目数据保证 arr 是一个山脉数组 进阶：很容易想到时间复杂度 O(n) 的解决方案，你可以设计一个 O(log(n)) 的解决方案吗？ 注意：本题与主站 852 题相同：https://leetcode.cn/problems/peak-index-in-a-mountain-array/ [https://leetcode.cn/problems/peak-index-in-a-mountain-array/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找来找到山脉数组的峰顶索引。

算法步骤:
1. 初始化左右指针 left 和 right。
2. 在 while 循环中，计算中间位置 mid。
3. 比较 arr[mid] 和 arr[mid + 1]：
   - 如果 arr[mid] < arr[mid + 1]，说明峰顶在 mid 右侧，更新 left = mid + 1。
   - 否则，峰顶在 mid 或其左侧，更新 right = mid。
4. 当 left == right 时，返回 left 作为峰顶索引。

关键点:
- 通过二分查找，可以在 O(log n) 时间内找到峰顶索引。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(arr: List[int]) -> int:
    """
    函数式接口 - 使用二分查找找到山脉数组的峰顶索引
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return left


Solution = create_solution(solution_function_name)