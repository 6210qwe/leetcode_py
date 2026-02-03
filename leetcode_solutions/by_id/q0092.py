# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 92
标题: Reverse Linked List II
难度: medium
链接: https://leetcode.cn/problems/reverse-linked-list-ii/
题目类型: 链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
92. 反转链表 II - 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。 示例 1： [https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg] 输入：head = [1,2,3,4,5], left = 2, right = 4 输出：[1,4,3,2,5] 示例 2： 输入：head = [5], left = 1, right = 1 输出：[5] 提示： * 链表中节点数目为 n * 1 <= n <= 500 * -500 <= Node.val <= 500 * 1 <= left <= right <= n 进阶： 你可以使用一趟扫描完成反转吗？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 找到需要反转的区间，使用头插法反转

算法步骤:
1. 创建虚拟头节点，简化边界处理
2. 找到left位置的前一个节点prev
3. 使用头插法反转从left到right的节点：
   - 将current.next插入到prev.next之后
   - 重复直到反转完所有节点
4. 返回虚拟头节点的next

关键点:
- 使用虚拟头节点简化边界处理
- 头插法：每次将节点插入到prev.next之后
- 时间复杂度O(n)，空间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要遍历链表
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.solution import create_solution


def reverse_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    """
    函数式接口 - 头插法
    
    实现思路:
    使用虚拟头节点和头插法反转链表中从left到right的节点。
    
    Args:
        head: 链表头节点
        left: 反转区间的起始位置（从1开始）
        right: 反转区间的结束位置
        
    Returns:
        反转后的链表头节点
        
    Example:
        >>> head = ListNode.from_list([1,2,3,4,5])
        >>> reverse_between(head, 2, 4)
        # 返回[1,4,3,2,5]
    """
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    # 找到left位置的前一个节点
    for _ in range(left - 1):
        prev = prev.next
    
    # 头插法反转
    current = prev.next
    for _ in range(right - left):
        next_node = current.next
        current.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node
    
    return dummy.next


# 自动生成Solution类（无需手动编写）
Solution = create_solution(reverse_between)
