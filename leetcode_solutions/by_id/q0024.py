# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 24
标题: Swap Nodes in Pairs
难度: medium
链接: https://leetcode.cn/problems/swap-nodes-in-pairs/
题目类型: 递归、链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
24. 两两交换链表中的节点 - 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。 示例 1： [https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg] 输入：head = [1,2,3,4] 输出：[2,1,4,3] 示例 2： 输入：head = [] 输出：[] 示例 3： 输入：head = [1] 输出：[1] 提示： * 链表中节点的数目在范围 [0, 100] 内 * 0 <= Node.val <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 迭代法，使用虚拟头节点，每次交换相邻的两个节点

算法步骤:
1. 创建虚拟头节点dummy，简化边界处理
2. 使用prev指针指向当前要交换的两个节点的前一个节点
3. 当prev.next和prev.next.next都存在时：
   - 记录要交换的两个节点：first = prev.next, second = prev.next.next
   - 执行交换：prev.next = second, first.next = second.next, second.next = first
   - 更新prev指针：prev = first
4. 返回dummy.next

关键点:
- 使用虚拟头节点可以简化边界处理
- 需要同时检查prev.next和prev.next.next是否存在
- 时间复杂度O(n)，空间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 只需遍历链表一次，n为链表长度
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.solution import create_solution


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    函数式接口 - 迭代法实现
    
    实现思路:
    使用虚拟头节点，每次交换相邻的两个节点。
    
    Args:
        head: 链表头节点
        
    Returns:
        交换后的链表头节点
        
    Example:
        >>> head = ListNode.from_list([1,2,3,4])
        >>> result = swap_pairs(head)
        >>> result.to_list()
        [2, 1, 4, 3]
    """
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next
        
        # 交换两个节点
        prev.next = second
        first.next = second.next
        second.next = first
        
        # 更新prev指针
        prev = first
    
    return dummy.next


# 自动生成Solution类（无需手动编写）
Solution = create_solution(swap_pairs)
