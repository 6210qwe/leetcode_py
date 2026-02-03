# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 86
标题: Partition List
难度: medium
链接: https://leetcode.cn/problems/partition-list/
题目类型: 链表、双指针
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
86. 分隔链表 - 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。 你应当 保留 两个分区中每个节点的初始相对位置。 示例 1： [https://assets.leetcode.com/uploads/2021/01/04/partition.jpg] 输入：head = [1,4,3,2,5,2], x = 3 输出：[1,2,2,4,3,5] 示例 2： 输入：head = [2,1], x = 2 输出：[1,2] 提示： * 链表中节点的数目在范围 [0, 200] 内 * -100 <= Node.val <= 100 * -200 <= x <= 200
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个链表分别存储小于x和大于等于x的节点，然后连接

算法步骤:
1. 创建两个虚拟头节点：small和large
2. 遍历原链表：
   - 如果节点值小于x，加入small链表
   - 否则，加入large链表
3. 将small链表的尾部连接到large链表的头部
4. 返回small.next

关键点:
- 使用两个链表分别存储，保持相对顺序
- 最后需要将large链表的尾部设为None
- 时间复杂度O(n)，空间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 只需一次遍历
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.solution import create_solution


def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    """
    函数式接口 - 双链表
    
    实现思路:
    使用两个链表分别存储小于x和大于等于x的节点，然后连接。
    
    Args:
        head: 链表头节点
        x: 特定值
        
    Returns:
        分隔后的链表头节点
        
    Example:
        >>> head = ListNode.from_list([1,4,3,2,5,2])
        >>> partition(head, 3)
        # 返回[1,2,2,4,3,5]
    """
    small = ListNode(0)
    large = ListNode(0)
    small_head = small
    large_head = large
    
    current = head
    while current:
        if current.val < x:
            small.next = current
            small = small.next
        else:
            large.next = current
            large = large.next
        current = current.next
    
    # 连接两个链表
    small.next = large_head.next
    large.next = None  # 重要：将large链表的尾部设为None
    
    return small_head.next


# 自动生成Solution类（无需手动编写）
Solution = create_solution(partition)
