# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 978
标题: Valid Mountain Array
难度: easy
链接: https://leetcode.cn/problems/valid-mountain-array/
题目类型: 数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
941. 有效的山脉数组 - 给定一个整数数组 arr，如果它是有效的山脉数组就返回 true，否则返回 false。 让我们回顾一下，如果 arr 满足下述条件，那么它是一个山脉数组： * arr.length >= 3 * 在 0 < i < arr.length - 1 条件下，存在 i 使得： * arr[0] < arr[1] < ... arr[i-1] < arr[i] * arr[i] > arr[i+1] > ... > arr[arr.length - 1] [https://assets.leetcode.com/uploads/2019/10/20/hint_valid_mountain_array.png] 示例 1： 输入：arr = [2,1] 输出：false 示例 2： 输入：arr = [3,5,5] 输出：false 示例 3： 输入：arr = [0,3,2,1] 输出：true 提示： * 1 <= arr.length <= 104 * 0 <= arr[i] <= 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
