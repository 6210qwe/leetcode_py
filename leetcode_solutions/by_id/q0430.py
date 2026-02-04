# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 430
标题: 扁平化多级双向链表
难度: 中等
链接: https://leetcode.cn/problems/flatten-a-multilevel-doubly-linked-list/
题目类型: 链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
给你一个头结点为 head 的多级双向链表，其中每个节点还包含指向子节点的指针 child。该链表是一个 形如 [a, null, b, null, c, d] 的扁平化表示。
请你将这个多级双向链表拉平，使所有结点出现在单级双向链表中。返回新的头结点。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）遍历多级双向链表，并在遍历过程中将其扁平化。

算法步骤:
1. 定义一个递归函数 `dfs` 来处理当前节点及其子节点。
2. 在 `dfs` 函数中，首先处理当前节点的下一个节点，如果存在子节点，则递归处理子节点。
3. 将子节点的尾节点连接到当前节点的下一个节点。
4. 更新节点的 `prev` 和 `next` 指针，确保双向链表的正确性。

关键点:
- 注意边界条件，特别是空节点和没有子节点的情况。
- 通过递归处理子节点，并将其连接到主链表中。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 其中 n 是链表中的节点数，每个节点只会被访问一次。
空间复杂度: O(1) - 除了递归栈的空间外，不需要额外的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def flatten(head: Optional[Node]) -> Optional[Node]:
    """
    函数式接口 - 扁平化多级双向链表
    
    实现思路:
    使用深度优先搜索（DFS）遍历多级双向链表，并在遍历过程中将其扁平化。
    
    Args:
        head: 多级双向链表的头节点
        
    Returns:
        返回扁平化后的单级双向链表的头节点
        
    Example:
        >>> head = Node(1, child=Node(2, child=Node(3), next=Node(4)))
        >>> flatten(head)
        Node(1, next=Node(2, next=Node(3, next=Node(4))))
    """

    def dfs(node: Node) -> Node:
        cur = node
        while cur:
            if cur.child:
                tail = dfs(cur.child)
                next_node = cur.next
                cur.next = cur.child
                cur.child.prev = cur
                if next_node:
                    tail.next = next_node
                    next_node.prev = tail
                cur.child = None
                cur = tail
            else:
                last = cur
                cur = cur.next
        return last

    if not head:
        return None
    dfs(head)
    return head


# 自动生成Solution类（无需手动编写）
Solution = create_solution(flatten)