# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1767
标题: Design Front Middle Back Queue
难度: medium
链接: https://leetcode.cn/problems/design-front-middle-back-queue/
题目类型: 设计、队列、数组、链表、数据流、双向链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1670. 设计前中后队列 - 请你设计一个队列，支持在前，中，后三个位置的 push 和 pop 操作。 请你完成 FrontMiddleBack 类： * FrontMiddleBack() 初始化队列。 * void pushFront(int val) 将 val 添加到队列的 最前面 。 * void pushMiddle(int val) 将 val 添加到队列的 正中间 。 * void pushBack(int val) 将 val 添加到队里的 最后面 。 * int popFront() 将 最前面 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 -1 。 * int popMiddle() 将 正中间 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 -1 。 * int popBack() 将 最后面 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 -1 。 请注意当有 两个 中间位置的时候，选择靠前面的位置进行操作。比方说： * 将 6 添加到 [1, 2, 3, 4, 5] 的中间位置，结果数组为 [1, 2, 6, 3, 4, 5] 。 * 从 [1, 2, 3, 4, 5, 6] 的中间位置弹出元素，返回 3 ，数组变为 [1, 2, 4, 5, 6] 。 示例 1： 输入： ["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"] [[], [1], [2], [3], [4], [], [], [], [], []] 输出： [null, null, null, null, null, 1, 3, 4, 2, -1] 解释： FrontMiddleBackQueue q = new FrontMiddleBackQueue(); q.pushFront(1); // [1] q.pushBack(2); // [1, 2] q.pushMiddle(3); // [1, 3, 2] q.pushMiddle(4); // [1, 4, 3, 2] q.popFront(); // 返回 1 -> [4, 3, 2] q.popMiddle(); // 返回 3 -> [4, 2] q.popMiddle(); // 返回 4 -> [2] q.popBack(); // 返回 2 -> [] q.popFront(); // 返回 -1 -> [] （队列为空） 提示： * 1 <= val <= 109 * 最多调用 1000 次 pushFront， pushMiddle， pushBack， popFront， popMiddle 和 popBack 。
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
