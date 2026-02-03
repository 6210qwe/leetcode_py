# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 160
标题: Intersection of Two Linked Lists
难度: easy
链接: https://leetcode.cn/problems/intersection-of-two-linked-lists/
题目类型: 哈希表、链表、双指针
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
160. 相交链表 - 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。 图示两个链表在节点 c1 开始相交： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/14/160_statement.png] [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/14/160_statement.png] 题目数据 保证 整个链式结构中不存在环。 注意，函数返回结果后，链表必须 保持其原始结构 。 自定义评测： 评测系统 的输入如下（你设计的程序 不适用 此输入）： * intersectVal - 相交的起始节点的值。如果不存在相交节点，这一值为 0 * listA - 第一个链表 * listB - 第二个链表 * skipA - 在 listA 中（从头节点开始）跳到交叉节点的节点数 * skipB - 在 listB 中（从头节点开始）跳到交叉节点的节点数 评测系统将根据这些输入创建链式数据结构，并将两个头节点 headA 和 headB 传递给你的程序。如果程序能够正确返回相交节点，那么你的解决方案将被 视作正确答案 。 示例 1： [https://assets.leetcode.com/uploads/2021/03/05/160_example_1_1.png] [https://assets.leetcode.com/uploads/2018/12/13/160_example_1.png] 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3 输出：Intersected at '8' 解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。 从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,6,1,8,4,5]。 在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。 — 请注意相交节点的值不为 1，因为在链表 A 和链表 B 之中值为 1 的节点 (A 中第二个节点和 B 中第三个节点) 是不同的节点。换句话说，它们在内存中指向两个不同的位置，而链表 A 和链表 B 中值为 8 的节点 (A 中第三个节点，B 中第四个节点) 在内存中指向相同的位置。 示例 2： [https://assets.leetcode.com/uploads/2021/03/05/160_example_2.png] [https://assets.leetcode.com/uploads/2018/12/13/160_example_2.png] 输入：intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1 输出：Intersected at '2' 解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。 从各自的表头开始算起，链表 A 为 [1,9,1,2,4]，链表 B 为 [3,2,4]。 在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/14/160_example_3.png] [https://assets.leetcode.com/uploads/2018/12/13/160_example_3.png] 输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2 输出：No intersection 解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。 由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。 这两个链表不相交，因此返回 null 。 提示： * listA 中节点数目为 m * listB 中节点数目为 n * 1 <= m, n <= 3 * 104 * 1 <= Node.val <= 105 * 0 <= skipA <= m * 0 <= skipB <= n * 如果 listA 和 listB 没有交点，intersectVal 为 0 * 如果 listA 和 listB 有交点，intersectVal == listA[skipA] == listB[skipB] 进阶：你能否设计一个时间复杂度 O(m + n) 、仅用 O(1) 内存的解决方案？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针，让两个指针分别遍历两个链表，然后交换起点

算法步骤:
1. 使用两个指针分别从headA和headB开始
2. 当一个指针到达末尾时，切换到另一个链表的头部
3. 如果两个链表相交，两个指针会在交点相遇
4. 如果两个链表不相交，两个指针会同时到达None

关键点:
- 双指针技巧，消除长度差
- 时间复杂度O(m+n)，空间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m+n) - m和n分别是两个链表的长度
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.solution import create_solution


def intersection_of_two_linked_lists(headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
    """
    函数式接口 - 找出两个链表的交点
    
    实现思路:
    使用双指针，让两个指针分别遍历两个链表，然后交换起点。
    
    Args:
        headA: 第一个链表的头节点
        headB: 第二个链表的头节点
        
    Returns:
        相交节点，如果不存在返回None
        
    Example:
        >>> # 创建相交的链表
        >>> headA = ListNode(4)
        >>> headA.next = ListNode(1)
        >>> headB = ListNode(5)
        >>> headB.next = ListNode(6)
        >>> headB.next.next = ListNode(1)
        >>> intersect = ListNode(8)
        >>> headA.next.next = intersect
        >>> headB.next.next.next = intersect
        >>> intersection_of_two_linked_lists(headA, headB).val
        8
    """
    if not headA or not headB:
        return None
    
    pA, pB = headA, headB
    
    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
    
    return pA


# 自动生成Solution类（无需手动编写）
Solution = create_solution(intersection_of_two_linked_lists)
