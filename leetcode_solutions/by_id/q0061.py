# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 61
标题: Rotate List
难度: medium
链接: https://leetcode.cn/problems/rotate-list/
题目类型: 链表、双指针
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
61. 旋转链表 - 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。 示例 1： [https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg] 输入：head = [1,2,3,4,5], k = 2 输出：[4,5,1,2,3] 示例 2： [https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg] 输入：head = [0,1,2], k = 4 输出：[2,0,1] 提示： * 链表中节点的数目在范围 [0, 500] 内 * -100 <= Node.val <= 100 * 0 <= k <= 2 * 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 将链表首尾相连形成环，然后找到新的头节点并断开

算法步骤:
1. 特殊情况：如果链表为空或只有一个节点，或k=0，直接返回
2. 计算链表长度，并将k对长度取模（因为旋转k次和旋转k%len次等价）
3. 将链表首尾相连形成环
4. 找到新的尾节点：从head开始移动(len - k)步
5. 新的头节点是尾节点的下一个节点
6. 断开环：将尾节点的next设为None
7. 返回新的头节点

关键点:
- 先计算长度，避免k过大时重复旋转
- 形成环后，只需要移动指针即可，不需要实际移动节点
- 时间复杂度O(n)，空间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要遍历链表计算长度和找到新头节点
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.solution import create_solution


def rotate_right(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    函数式接口 - 首尾相连形成环
    
    实现思路:
    将链表首尾相连形成环，然后找到新的头节点并断开环。
    
    Args:
        head: 链表的头节点
        k: 向右旋转的步数
        
    Returns:
        旋转后的链表头节点
        
    Example:
        >>> head = ListNode.from_list([1, 2, 3, 4, 5])
        >>> rotate_right(head, 2)
        # 返回[4, 5, 1, 2, 3]
    """
    if not head or not head.next or k == 0:
        return head
    
    # 计算链表长度
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1
    
    # k对长度取模
    k = k % length
    if k == 0:
        return head
    
    # 将链表首尾相连形成环
    tail.next = head
    
    # 找到新的尾节点（从head开始移动length - k步）
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next
    
    # 新的头节点
    new_head = new_tail.next
    # 断开环
    new_tail.next = None
    
    return new_head


# 自动生成Solution类（无需手动编写）
Solution = create_solution(rotate_right)
