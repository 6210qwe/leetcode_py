# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1270
标题: Dinner Plate Stacks
难度: hard
链接: https://leetcode.cn/problems/dinner-plate-stacks/
题目类型: 栈、设计、哈希表、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1172. 餐盘栈 - 我们把无限数量 ∞ 的栈排成一行，按从左到右的次序从 0 开始编号。每个栈的的最大容量 capacity 都相同。 实现一个叫「餐盘」的类 DinnerPlates： * DinnerPlates(int capacity) - 给出栈的最大容量 capacity。 * void push(int val) - 将给出的正整数 val 推入 从左往右第一个 没有满的栈。 * int pop() - 返回 从右往左第一个 非空栈顶部的值，并将其从栈中删除；如果所有的栈都是空的，请返回 -1。 * int popAtStack(int index) - 返回编号 index 的栈顶部的值，并将其从栈中删除；如果编号 index 的栈是空的，请返回 -1。 示例： 输入： ["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"] [[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]] 输出： [null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1] 解释： DinnerPlates D = DinnerPlates(2); // 初始化，栈最大容量 capacity = 2 D.push(1); D.push(2); D.push(3); D.push(4); D.push(5); // 栈的现状为： 2 4 1 3 5 ﹈ ﹈ ﹈ D.popAtStack(0); // 返回 2。栈的现状为： 4 1 3 5 ﹈ ﹈ ﹈ D.push(20); // 栈的现状为： 20 4 1 3 5 ﹈ ﹈ ﹈ D.push(21); // 栈的现状为： 20 4 21 1 3 5 ﹈ ﹈ ﹈ D.popAtStack(0); // 返回 20。栈的现状为： 4 21 1 3 5 ﹈ ﹈ ﹈ D.popAtStack(2); // 返回 21。栈的现状为： 4 1 3 5 ﹈ ﹈ ﹈ D.pop() // 返回 5。栈的现状为： 4 1 3 ﹈ ﹈ D.pop() // 返回 4。栈的现状为： 1 3 ﹈ ﹈ D.pop() // 返回 3。栈的现状为： 1 ﹈ D.pop() // 返回 1。现在没有栈。 D.pop() // 返回 -1。仍然没有栈。 提示： * 1 <= capacity <= 20000 * 1 <= val <= 20000 * 0 <= index <= 100000 * 最多会对 push，pop，和 popAtStack 进行 200000 次调用。
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
