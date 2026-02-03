# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100302
标题: 最小栈
难度: easy
链接: https://leetcode.cn/problems/bao-han-minhan-shu-de-zhan-lcof/
题目类型: 栈、设计
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 147. 最小栈 - 请你设计一个 最小栈 。它提供 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。 实现 MinStack 类: * MinStack() 初始化堆栈对象。 * void push(int val) 将元素val推入堆栈。 * void pop() 删除堆栈顶部的元素。 * int top() 获取堆栈顶部的元素。 * int getMin() 获取堆栈中的最小元素。 示例 1： 输入： ["MinStack","push","push","push","getMin","pop","top","getMin"] [[],[-2],[0],[-3],[],[],[],[]] 输出： [null,null,null,null,-3,null,0,-2] 解释： MinStack minStack = new MinStack(); minStack.push(-2); minStack.push(0); minStack.push(-3); minStack.getMin(); --> 返回 -3. minStack.pop(); minStack.top(); --> 返回 0. minStack.getMin(); --> 返回 -2. 提示： * -231 <= val <= 231 - 1 * pop、top 和 getMin 操作总是在 非空栈 上调用 * push、pop、top 和 getMin 最多被调用 3 * 104 次 注意：本题与主站 155 题相同：https://leetcode.cn/problems/min-stack/ [https://leetcode.cn/problems/min-stack/]
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
