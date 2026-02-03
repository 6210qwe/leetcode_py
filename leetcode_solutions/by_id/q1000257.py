# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000257
标题: 删除链表的倒数第 N 个结点
难度: medium
链接: https://leetcode.cn/problems/SLwz0R/
题目类型: 链表、双指针
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 021. 删除链表的倒数第 N 个结点 - 给定一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。 示例 1： [https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg] 输入：head = [1,2,3,4,5], n = 2 输出：[1,2,3,5] 示例 2： 输入：head = [1], n = 1 输出：[] 示例 3： 输入：head = [1,2], n = 1 输出：[1] 提示： * 链表中结点的数目为 sz * 1 <= sz <= 30 * 0 <= Node.val <= 100 * 1 <= n <= sz 进阶：能尝试使用一趟扫描实现吗？ 注意：本题与主站 19 题相同： https://leetcode.cn/problems/remove-nth-node-from-end-of-list/ [https://leetcode.cn/problems/remove-nth-node-from-end-of-list/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 快慢指针（双指针）一趟扫描

算法步骤:
1. 使用哑节点 dummy 指向 head，便于删除头节点
2. fast 指针先向前走 n 步
3. 然后 fast 和 slow 同时前进，直到 fast 到达链表末尾（fast.next 为 None）
4. 此时 slow.next 即为倒数第 n 个节点，将其删除：slow.next = slow.next.next
5. 返回 dummy.next

关键点:
- dummy 统一处理删除头节点的情况
- fast 先走 n 步保证 slow 停在待删节点的前一个位置
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(L) - L 为链表长度
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    函数式接口 - 删除链表的倒数第 N 个结点
    """
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy

    for _ in range(n):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    # 删除 slow.next
    slow.next = slow.next.next
    return dummy.next


Solution = create_solution(remove_nth_from_end)
