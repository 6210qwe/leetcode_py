# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2796
标题: Allow One Function Call
难度: easy
链接: https://leetcode.cn/problems/allow-one-function-call/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2666. 只允许一次函数调用 - 给定一个函数 fn ，它返回一个新的函数，返回的函数与原始函数完全相同，只不过它确保 fn 最多被调用一次。 * 第一次调用返回的函数时，它应该返回与 fn 相同的结果。 * 第一次后的每次调用，它应该返回 undefined 。 示例 1： 输入：fn = (a,b,c) => (a + b + c), calls = [[1,2,3],[2,3,6]] 输出：[{"calls":1,"value":6}] 解释： const onceFn = once(fn); onceFn(1, 2, 3); // 6 onceFn(2, 3, 6); // undefined, fn 没有被调用 示例 2： 输入：fn = (a,b,c) => (a * b * c), calls = [[5,7,4],[2,3,6],[4,6,8]] 输出：[{"calls":1,"value":140}] 解释： const onceFn = once(fn); onceFn(5, 7, 4); // 140 onceFn(2, 3, 6); // undefined, fn 没有被调用 onceFn(4, 6, 8); // undefined, fn 没有被调用 提示： * calls 是一个有效的 JSON 数组 * 1 <= calls.length <= 10 * 1 <= calls[i].length <= 100 * 2 <= JSON.stringify(calls).length <= 1000
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
