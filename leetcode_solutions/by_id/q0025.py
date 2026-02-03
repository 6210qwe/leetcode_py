# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 25
标题: Reverse Nodes in k-Group
难度: hard
链接: https://leetcode.cn/problems/reverse-nodes-in-k-group/
题目类型: 递归、链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
25. K 个一组翻转链表 - 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。 k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。 示例 1： [https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg] 输入：head = [1,2,3,4,5], k = 2 输出：[2,1,4,3,5] 示例 2： [https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg] 输入：head = [1,2,3,4,5], k = 3 输出：[3,2,1,4,5] 提示： * 链表中的节点数目为 n * 1 <= k <= n <= 5000 * 0 <= Node.val <= 1000 进阶：你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 递归法，先检查是否有k个节点，如果有则翻转这k个节点，然后递归处理剩余部分

算法步骤:
1. 检查从head开始是否有k个节点，如果没有则直接返回head
2. 如果有k个节点，翻转这k个节点：
   - 使用三个指针：prev, cur, next
   - 翻转k个节点
3. 递归处理剩余部分：head.next = reverse_k_group(next, k)
4. 返回翻转后的头节点

关键点:
- 递归法思路清晰，代码简洁
- 需要先检查是否有k个节点，避免翻转不足k个节点
- 时间复杂度O(n)，空间复杂度O(n/k)（递归栈深度）
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要遍历所有节点，n为链表长度
空间复杂度: O(n/k) - 递归栈的深度为n/k
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.solution import create_solution


def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    函数式接口 - 递归法实现
    
    实现思路:
    先检查是否有k个节点，如果有则翻转这k个节点，然后递归处理剩余部分。
    
    Args:
        head: 链表头节点
        k: 每组翻转的节点数
        
    Returns:
        翻转后的链表头节点
        
    Example:
        >>> head = ListNode.from_list([1,2,3,4,5])
        >>> result = reverse_k_group(head, 2)
        >>> result.to_list()
        [2, 1, 4, 3, 5]
        >>> head = ListNode.from_list([1,2,3,4,5])
        >>> result = reverse_k_group(head, 3)
        >>> result.to_list()
        [3, 2, 1, 4, 5]
    """
    # 检查是否有k个节点
    cur = head
    count = 0
    while cur and count < k:
        cur = cur.next
        count += 1
    
    # 如果有k个节点，则翻转
    if count == k:
        # 翻转k个节点
        prev = None
        cur = head
        for _ in range(k):
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        # 递归处理剩余部分
        head.next = reverse_k_group(cur, k)
        return prev
    
    # 如果不足k个节点，直接返回
    return head


# 自动生成Solution类（无需手动编写）
Solution = create_solution(reverse_k_group)
