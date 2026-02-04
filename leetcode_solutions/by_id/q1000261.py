# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000261
标题: 两数相加 II
难度: medium
链接: https://leetcode.cn/problems/lMSNwu/
题目类型: 栈、链表、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 025. 两数相加 II - 给定两个 非空链表 l1和 l2 来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。 可以假设除了数字 0 之外，这两个数字都不会以零开头。 示例 1： [https://pic.leetcode.cn/1626420025-fZfzMX-image.png] 输入：l1 = [7,2,4,3], l2 = [5,6,4] 输出：[7,8,0,7] 示例 2： 输入：l1 = [2,4,3], l2 = [5,6,4] 输出：[8,0,7] 示例 3： 输入：l1 = [0], l2 = [0] 输出：[0] 提示： * 链表的长度范围为 [1, 100] * 0 <= node.val <= 9 * 输入数据保证链表代表的数字无前导 0 进阶：如果输入链表不能修改该如何处理？换句话说，不能对列表中的节点进行翻转。 注意：本题与主站 445 题相同：https://leetcode.cn/problems/add-two-numbers-ii/ [https://leetcode.cn/problems/add-two-numbers-ii/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用栈来存储链表的节点值，然后从栈顶开始逐位相加，处理进位。

算法步骤:
1. 将两个链表的节点值分别压入两个栈中。
2. 从栈顶开始逐位相加，处理进位，并创建新的链表节点。
3. 最后处理剩余的进位。

关键点:
- 使用栈来逆序处理链表节点值。
- 逐位相加并处理进位。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 和 m 分别是两个链表的长度。
空间复杂度: O(n + m)，用于存储两个栈。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    函数式接口 - 实现两数相加 II
    """
    # 将链表节点值压入栈中
    stack1, stack2 = [], []
    while l1:
        stack1.append(l1.val)
        l1 = l1.next
    while l2:
        stack2.append(l2.val)
        l2 = l2.next
    
    # 初始化结果链表和进位
    carry = 0
    head = None
    
    # 从栈顶开始逐位相加
    while stack1 or stack2 or carry:
        val1 = stack1.pop() if stack1 else 0
        val2 = stack2.pop() if stack2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        new_node = ListNode(total % 10)
        new_node.next = head
        head = new_node
    
    return head

Solution = create_solution(addTwoNumbers)