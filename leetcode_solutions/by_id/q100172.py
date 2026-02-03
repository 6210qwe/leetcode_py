# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100172
标题: Three in One LCCI
难度: easy
链接: https://leetcode.cn/problems/three-in-one-lcci/
题目类型: 栈、设计、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 03.01. 三合一 - 三合一。描述如何只用一个数组来实现三个栈。 你应该实现push(stackNum, value)、pop(stackNum)、isEmpty(stackNum)、peek(stackNum)方法。stackNum表示栈下标，value表示压入的值。 构造函数会传入一个stackSize参数，代表每个栈的大小。 示例 1： 输入： ["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"] [[1], [0, 1], [0, 2], [0], [0], [0], [0]] 输出： [null, null, null, 1, -1, -1, true] 说明：当栈为空时`pop, peek`返回-1，当栈满时`push`不压入元素。 示例 2： 输入： ["TripleInOne", "push", "push", "push", "pop", "pop", "pop", "peek"] [[2], [0, 1], [0, 2], [0, 3], [0], [0], [0], [0]] 输出： [null, null, null, null, 2, 1, -1, -1] 提示： * 0 <= stackNum <= 2
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
