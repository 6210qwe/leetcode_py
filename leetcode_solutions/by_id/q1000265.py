# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000265
标题: 循环有序列表的插入
难度: medium
链接: https://leetcode.cn/problems/4ueAj6/
题目类型: 链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 029. 循环有序列表的插入 - 给定循环单调非递减列表中的一个点，写一个函数向这个列表中插入一个新元素 insertVal ，使这个列表仍然是循环升序的。 给定的可以是这个列表中任意一个顶点的指针，并不一定是这个列表中最小元素的指针。 如果有多个满足条件的插入位置，可以选择任意一个位置插入新的值，插入后整个列表仍然保持有序。 如果列表为空（给定的节点是 null），需要创建一个循环有序列表并返回这个节点。否则。请返回原先给定的节点。 示例 1： [https://assets.leetcode.com/uploads/2019/01/19/example_1_before_65p.jpg] 输入：head = [3,4,1], insertVal = 2 输出：[3,4,1,2] 解释：在上图中，有一个包含三个元素的循环有序列表，你获得值为 3 的节点的指针，我们需要向表中插入元素 2 。新插入的节点应该在 1 和 3 之间，插入之后，整个列表如上图所示，最后返回节点 3 。 [https://assets.leetcode.com/uploads/2019/01/19/example_1_after_65p.jpg] 示例 2： 输入：head = [], insertVal = 1 输出：[1] 解释：列表为空（给定的节点是 null），创建一个循环有序列表并返回这个节点。 示例 3： 输入：head = [1], insertVal = 0 输出：[1,0] 提示： * 0 <= Number of Nodes <= 5 * 10^4 * -10^6 <= Node.val <= 10^6 * -10^6 <= insertVal <= 10^6 注意：本题与主站 708 题相同： https://leetcode.cn/problems/insert-into-a-sorted-circular-linked-list/ [https://leetcode.cn/problems/insert-into-a-sorted-circular-linked-list/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
- 在循环链表中找到合适的插入位置，使得插入后链表仍然保持循环升序。
- 处理特殊情况：链表为空、所有节点值相同、插入值大于或小于所有节点值。

算法步骤:
1. 如果链表为空，创建一个新节点并指向自己，返回该节点。
2. 使用双指针遍历链表，找到合适的插入位置。
3. 插入新节点并调整指针。

关键点:
- 处理链表为空的情况。
- 处理所有节点值相同的情况。
- 找到合适的插入位置。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是链表的长度。最坏情况下需要遍历整个链表。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.solution import create_solution

class Solution:
    def insert(self, head: 'Optional[ListNode]', insertVal: int) -> 'ListNode':
        if not head:
            # 链表为空，创建一个新节点并指向自己
            new_node = ListNode(insertVal)
            new_node.next = new_node
            return new_node
        
        prev, curr = head, head.next
        to_insert = False
        
        while True:
            if prev.val <= insertVal <= curr.val:
                # 找到合适的插入位置
                to_insert = True
            elif prev.val > curr.val:
                # 处理跨越最大值和最小值的情况
                if insertVal >= prev.val or insertVal <= curr.val:
                    to_insert = True
            
            if to_insert:
                # 插入新节点
                prev.next = ListNode(insertVal, curr)
                return head
            
            prev, curr = curr, curr.next
            if prev == head:
                # 遍历完整个链表
                break
        
        # 插入值大于或小于所有节点值，插入到链表末尾
        prev.next = ListNode(insertVal, curr)
        return head

Solution = create_solution(Solution)