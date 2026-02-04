# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 716
标题: Max Stack
难度: hard
链接: https://leetcode.cn/problems/max-stack/
题目类型: 栈、设计、链表、双向链表、有序集合
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
716. 最大栈 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个双端队列来存储栈元素，并使用一个有序集合来维护当前栈中的最大值。

算法步骤:
1. 初始化一个双端队列和一个有序集合。
2. 对于 push 操作，将元素添加到双端队列的末尾，并在有序集合中添加该元素。
3. 对于 pop 操作，从双端队列的末尾移除元素，并从有序集合中移除该元素。
4. 对于 top 操作，返回双端队列的末尾元素。
5. 对于 peekMax 操作，返回有序集合中的最大值。
6. 对于 popMax 操作，从有序集合中移除最大值，并从双端队列中移除该值。

关键点:
- 使用有序集合来维护当前栈中的最大值，确保所有操作的时间复杂度尽可能低。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: 
- push 和 pop 操作的时间复杂度为 O(log n)，因为需要在有序集合中插入和删除元素。
- top 和 peekMax 操作的时间复杂度为 O(1)。
- popMax 操作的时间复杂度为 O(log n)，因为需要在有序集合中查找并删除最大值。

空间复杂度: O(n)，其中 n 是栈中元素的数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
import collections
import sortedcontainers

class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_stack = sortedcontainers.SortedList()

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.max_stack.add(x)

    def pop(self) -> int:
        if not self.stack:
            return None
        x = self.stack.pop()
        self.max_stack.remove(x)
        return x

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def peekMax(self) -> int:
        if not self.max_stack:
            return None
        return self.max_stack[-1]

    def popMax(self) -> int:
        if not self.max_stack:
            return None
        max_val = self.max_stack.pop()
        self.stack.remove(max_val)
        return max_val

Solution = create_solution(MaxStack)