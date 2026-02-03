# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 328
标题: Odd Even Linked List
难度: medium
链接: https://leetcode.cn/problems/odd-even-linked-list/
题目类型: 链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
328. 奇偶链表 - 给定单链表的头节点 head ，将所有索引为奇数的节点和索引为偶数的节点分别分组，保持它们原有的相对顺序，然后把偶数索引节点分组连接到奇数索引节点分组之后，返回重新排序的链表。 第一个节点的索引被认为是 奇数 ， 第二个节点的索引为 偶数 ，以此类推。 请注意，偶数组和奇数组内部的相对顺序应该与输入时保持一致。 你必须在 O(1) 的额外空间复杂度和 O(n) 的时间复杂度下解决这个问题。 示例 1: [https://assets.leetcode.com/uploads/2021/03/10/oddeven-linked-list.jpg] 输入: head = [1,2,3,4,5] 输出: [1,3,5,2,4] 示例 2: [https://assets.leetcode.com/uploads/2021/03/10/oddeven2-linked-list.jpg] 输入: head = [2,1,3,5,6,4,7] 输出: [2,3,6,7,1,5,4] 提示: * n == 链表中的节点数 * 0 <= n <= 104 * -106 <= Node.val <= 106
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 分离奇偶节点，然后连接

算法步骤:
1. 维护两个指针，分别指向奇数节点和偶数节点
2. 分离奇偶节点
3. 将偶数链表连接到奇数链表后面

关键点:
- 双指针
- 时间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 遍历链表一次
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def odd_even_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    函数式接口 - 奇偶链表
    
    实现思路:
    分离奇偶节点，然后连接。
    
    Args:
        head: 链表头节点
        
    Returns:
        重新排序后的链表头节点
        
    Example:
        >>> head = ListNode(1)
        >>> head.next = ListNode(2)
        >>> head.next.next = ListNode(3)
        >>> odd_even_list(head)
    """
    if not head or not head.next:
        return head
    
    odd = head
    even = head.next
    even_head = even
    
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    
    odd.next = even_head
    return head


# 自动生成Solution类（无需手动编写）
Solution = create_solution(odd_even_list)
