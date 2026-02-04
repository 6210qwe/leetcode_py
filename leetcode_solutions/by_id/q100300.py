# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100300
标题: 随机链表的复制
难度: medium
链接: https://leetcode.cn/problems/fu-za-lian-biao-de-fu-zhi-lcof/
题目类型: 哈希表、链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 154. 复杂链表的复制 - 请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/09/e1.png] 输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]] 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]] 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/09/e2.png] 输入：head = [[1,1],[2,1]] 输出：[[1,1],[2,1]] 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/09/e3.png] 输入：head = [[3,null],[3,0],[3,null]] 输出：[[3,null],[3,0],[3,null]] 示例 4： 输入：head = [] 输出：[] 解释：给定的链表为空（空指针），因此返回 null。 提示： * -10000 <= Node.val <= 10000 * Node.random 为空（null）或指向链表中的节点。 * 节点数目不超过 1000 。 注意：本题与主站 138 题相同：https://leetcode.cn/problems/copy-list-with-random-pointer/ [https://leetcode.cn/problems/copy-list-with-random-pointer/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表来存储原节点和新节点的对应关系，然后通过两次遍历来完成复制。

算法步骤:
1. 第一次遍历原链表，创建新节点并建立原节点和新节点的对应关系。
2. 第二次遍历原链表，根据哈希表设置新节点的 next 和 random 指针。

关键点:
- 使用哈希表存储原节点和新节点的对应关系，以便在第二次遍历时快速找到新节点的 next 和 random 指针。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是链表的长度。我们需要遍历链表两次，每次遍历的时间复杂度是 O(n)。
空间复杂度: O(n)，哈希表需要存储 n 个节点的对应关系。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head: 'Node') -> 'Node':
    if not head:
        return None
    
    # 创建一个哈希表来存储原节点和新节点的对应关系
    node_map = {}
    
    # 第一次遍历，创建新节点并建立原节点和新节点的对应关系
    current = head
    while current:
        node_map[current] = Node(current.val)
        current = current.next
    
    # 第二次遍历，设置新节点的 next 和 random 指针
    current = head
    while current:
        if current.next:
            node_map[current].next = node_map[current.next]
        if current.random:
            node_map[current].random = node_map[current.random]
        current = current.next
    
    return node_map[head]

Solution = create_solution(copyRandomList)