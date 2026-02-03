# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 859
标题: Design Circular Deque
难度: medium
链接: https://leetcode.cn/problems/design-circular-deque/
题目类型: 设计、队列、数组、链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
641. 设计循环双端队列 - 设计实现双端队列。 实现 MyCircularDeque 类: * MyCircularDeque(int k) ：构造函数,双端队列最大为 k 。 * boolean insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true ，否则返回 false 。 * boolean insertLast() ：将一个元素添加到双端队列尾部。如果操作成功返回 true ，否则返回 false 。 * boolean deleteFront() ：从双端队列头部删除一个元素。 如果操作成功返回 true ，否则返回 false 。 * boolean deleteLast() ：从双端队列尾部删除一个元素。如果操作成功返回 true ，否则返回 false 。 * int getFront() )：从双端队列头部获得一个元素。如果双端队列为空，返回 -1 。 * int getRear() ：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1 。 * boolean isEmpty() ：若双端队列为空，则返回 true ，否则返回 false 。 * boolean isFull() ：若双端队列满了，则返回 true ，否则返回 false 。 示例 1： 输入 ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"] [[3], [1], [2], [3], [4], [], [], [], [4], []] 输出 [null, true, true, true, false, 2, true, true, true, 4] 解释 MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3 circularDeque.insertLast(1); // 返回 true circularDeque.insertLast(2); // 返回 true circularDeque.insertFront(3); // 返回 true circularDeque.insertFront(4); // 已经满了，返回 false circularDeque.getRear(); // 返回 2 circularDeque.isFull(); // 返回 true circularDeque.deleteLast(); // 返回 true circularDeque.insertFront(4); // 返回 true circularDeque.getFront(); // 返回 4 提示： * 1 <= k <= 1000 * 0 <= value <= 1000 * insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull 调用次数不大于 2000 次
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
