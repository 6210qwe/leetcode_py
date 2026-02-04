# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100173
标题: Sort of Stacks LCCI
难度: medium
链接: https://leetcode.cn/problems/sort-of-stacks-lcci/
题目类型: 栈、设计、单调栈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 03.05. 栈排序 - 栈排序。 编写程序，对栈进行排序使最小元素位于栈顶。最多只能使用一个其他的临时栈存放数据，但不得将元素复制到别的数据结构（如数组）中。该栈支持如下操作：push、pop、peek 和 isEmpty。当栈为空时，peek 返回 -1。 示例 1： 输入： ["SortedStack", "push", "push", "peek", "pop", "peek"] [[], [1], [2], [], [], []] 输出： [null,null,null,1,null,2] 示例 2： 输入： ["SortedStack", "pop", "pop", "push", "pop", "isEmpty"] [[], [], [], [1], [], []] 输出： [null,null,null,null,null,true] 提示： 1. 栈中的元素数目在[0, 5000]范围内。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个栈来实现排序，主栈用于存储排序后的元素，辅助栈用于暂存元素。

算法步骤:
1. push 操作：将新元素与主栈的栈顶元素比较，如果新元素大于或等于栈顶元素，则直接入栈；否则，将主栈中所有小于新元素的元素依次弹出并压入辅助栈，然后将新元素压入主栈，最后再将辅助栈中的元素依次弹出并压回主栈。
2. pop 操作：直接弹出主栈的栈顶元素。
3. peek 操作：返回主栈的栈顶元素，如果主栈为空则返回 -1。
4. isEmpty 操作：检查主栈是否为空。

关键点:
- 使用辅助栈来保持主栈的有序性。
- 在 push 操作中，通过比较和移动元素来维持主栈的有序性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 最坏情况下，push 操作需要将所有元素从主栈移到辅助栈再移回来。
空间复杂度: O(n) - 使用了一个额外的辅助栈来暂存元素。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class SortedStack:

    def __init__(self):
        self.stack = []
        self.temp_stack = []

    def push(self, val: int) -> None:
        # 将主栈中小于 val 的元素移到辅助栈
        while self.stack and self.stack[-1] < val:
            self.temp_stack.append(self.stack.pop())
        # 将 val 压入主栈
        self.stack.append(val)
        # 将辅助栈中的元素移回主栈
        while self.temp_stack:
            self.stack.append(self.temp_stack.pop())

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1] if self.stack else -1

    def isEmpty(self) -> bool:
        return not self.stack


Solution = create_solution(SortedStack)