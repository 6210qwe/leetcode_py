# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 138
标题: Copy List with Random Pointer
难度: medium
链接: https://leetcode.cn/problems/copy-list-with-random-pointer/
题目类型: 哈希表、链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
138. 随机链表的复制 - 给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。 构造这个链表的 深拷贝 [https://baike.baidu.com/item/深拷贝/22785317?fr=aladdin]。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。 例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。 返回复制链表的头节点。 用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示： * val：一个表示 Node.val 的整数。 * random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为 null 。 你的代码 只 接受原链表的头节点 head 作为传入参数。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/09/e1.png] 输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]] 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]] 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/09/e2.png] 输入：head = [[1,1],[2,1]] 输出：[[1,1],[2,1]] 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/09/e3.png] 输入：head = [[3,null],[3,0],[3,null]] 输出：[[3,null],[3,0],[3,null]] 提示： * 0 <= n <= 1000 * -104 <= Node.val <= 104 * Node.random 为 null 或指向链表中的节点。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表存储原节点到新节点的映射，两次遍历完成复制

算法步骤:
1. 第一次遍历，创建所有新节点并存储到哈希表
2. 第二次遍历，设置新节点的next和random指针

关键点:
- 哈希表存储映射关系
- 时间复杂度O(n)，空间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要遍历链表两次
空间复杂度: O(n) - 哈希表空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.solution import create_solution


# Node类定义（LeetCode提供）
class Node:
    def __init__(self, x: int, next: Optional['Node'] = None, random: Optional['Node'] = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copy_list_with_random_pointer(head: Optional[Node]) -> Optional[Node]:
    """
    函数式接口 - 随机链表的复制
    
    实现思路:
    使用哈希表存储原节点到新节点的映射，两次遍历完成复制。
    
    Args:
        head: 链表的头节点
        
    Returns:
        复制链表的头节点
        
    Example:
        >>> # 示例用法
        >>> # head = Node(7, Node(13), Node(11))
        >>> # copied = copy_list_with_random_pointer(head)
    """
    if not head:
        return None
    
    node_map = {}
    current = head
    
    # 第一次遍历，创建所有新节点
    while current:
        node_map[current] = Node(current.val)
        current = current.next
    
    # 第二次遍历，设置next和random指针
    current = head
    while current:
        if current.next:
            node_map[current].next = node_map[current.next]
        if current.random:
            node_map[current].random = node_map[current.random]
        current = current.next
    
    return node_map[head]


# 自动生成Solution类（无需手动编写）
Solution = create_solution(copy_list_with_random_pointer)
