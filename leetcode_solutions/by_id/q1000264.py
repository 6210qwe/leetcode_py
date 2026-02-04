# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000264
标题: 扁平化多级双向链表
难度: medium
链接: https://leetcode.cn/problems/Qv1Da2/
题目类型: 深度优先搜索、链表、双向链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 028. 扁平化多级双向链表 - 多级双向链表中，除了指向下一个节点和前一个节点指针之外，它还有一个子链表指针，可能指向单独的双向链表。这些子列表也可能会有一个或多个自己的子项，依此类推，生成多级数据结构，如下面的示例所示。 给定位于列表第一级的头节点，请扁平化列表，即将这样的多级双向链表展平成普通的双向链表，使所有结点出现在单级双链表中。 示例 1： 输入：head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12] 输出：[1,2,3,7,8,11,12,9,10,4,5,6] 解释： 输入的多级列表如下图所示： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/10/12/multilevellinkedlist.png] 扁平化后的链表如下图： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/10/12/multilevellinkedlistflattened.png] 示例 2： 输入：head = [1,2,null,3] 输出：[1,3,2] 解释： 输入的多级列表如下图所示： 1---2---NULL | 3---NULL 示例 3： 输入：head = [] 输出：[] 如何表示测试用例中的多级链表？ 以 示例 1 为例： 1---2---3---4---5---6--NULL | 7---8---9---10--NULL | 11--12--NULL 序列化其中的每一级之后： [1,2,3,4,5,6,null] [7,8,9,10,null] [11,12,null] 为了将每一级都序列化到一起，我们需要每一级中添加值为 null 的元素，以表示没有节点连接到上一级的上级节点。 [1,2,3,4,5,6,null] [null,null,7,8,9,10,null] [null,11,12,null] 合并所有序列化结果，并去除末尾的 null 。 [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12] 提示： * 节点数目不超过 1000 * 1 <= Node.val <= 10^5 注意：本题与主站 430 题相同： https://leetcode.cn/problems/flatten-a-multilevel-doubly-linked-list/ [https://leetcode.cn/problems/flatten-a-multilevel-doubly-linked-list/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）遍历多级双向链表，并在遍历过程中调整节点的 next 和 prev 指针，将子链表插入到当前节点的 next 位置。

算法步骤:
1. 定义一个递归函数 dfs(node) 来处理每个节点。
2. 如果当前节点有子节点，则先保存当前节点的 next 节点，然后递归处理子节点。
3. 将子节点插入到当前节点的 next 位置，并更新相关节点的 prev 和 next 指针。
4. 继续处理保存的 next 节点。
5. 返回扁平化后的链表头节点。

关键点:
- 通过递归处理每个节点及其子节点，确保所有节点都被正确地插入到单级双向链表中。
- 在插入子节点时，需要更新相关节点的 prev 和 next 指针，确保链表的双向性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是链表中的节点数。每个节点只会被访问一次。
空间复杂度: O(1)，除了递归调用栈外，不需要额外的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional


class Node:
    def __init__(self, val: int, prev: 'Node' = None, next: 'Node' = None, child: 'Node' = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def flatten(head: 'Node') -> 'Node':
    if not head:
        return head

    def dfs(node: 'Node') -> 'Node':
        cur = node
        while cur:
            next_node = cur.next
            if cur.child:
                cur.next = dfs(cur.child)
                cur.child.prev = cur
                cur.child = None
                if next_node:
                    while cur.next:
                        cur = cur.next
                    cur.next = next_node
                    next_node.prev = cur
            cur = next_node
        return node

    return dfs(head)


Solution = create_solution(flatten)