# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100326
标题: 训练计划 V
难度: easy
链接: https://leetcode.cn/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/
题目类型: 哈希表、链表、双指针
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 171. 训练计划 V - 某教练同时带教两位学员，分别以链表 l1、l2 记录了两套核心肌群训练计划，节点值为训练项目编号。两套计划仅有前半部分热身项目不同，后续正式训练项目相同。请设计一个程序找出并返回第一个正式训练项目编号。如果两个链表不存在相交节点，返回 null 。 如下面的两个链表： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/14/160_statement.png] [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/14/160_statement.png] 在节点 c1 开始相交。 输入说明： intersectVal - 相交的起始节点的值。如果不存在相交节点，这一值为 0 l1 - 第一个训练计划链表 l2 - 第二个训练计划链表 skip1 - 在 l1 中（从头节点开始）跳到交叉节点的节点数 skip2 - 在 l2 中（从头节点开始）跳到交叉节点的节点数 程序将根据这些输入创建链式数据结构，并将两个头节点 head1 和 head2 传递给你的程序。如果程序能够正确返回相交节点，那么你的解决方案将被视作正确答案 。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/14/160_example_1.png] [https://assets.leetcode.com/uploads/2018/12/13/160_example_1.png] 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3 输出：Reference of the node with value = 8 解释：第一个正式训练项目编号为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/14/160_example_2.png] [https://assets.leetcode.com/uploads/2018/12/13/160_example_2.png] 输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1 输出：Reference of the node with value = 2 解释：第一个正式训练项目编号为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/14/160_example_3.png] [https://assets.leetcode.com/uploads/2018/12/13/160_example_3.png] 输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2 输出：null 解释：两套计划完全不同，返回 null。从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。 注意： * 如果两个链表没有交点，返回 null. * 在返回结果后，两个链表仍须保持原有的结构。 * 可假定整个链表结构中没有循环。 * 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。 * 本题与主站 160 题相同：https://leetcode.cn/problems/intersection-of-two-linked-lists/ [https://leetcode.cn/problems/intersection-of-two-linked-lists/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针法，让两个指针分别遍历两个链表，当一个指针到达链表末尾时，切换到另一个链表的头节点继续遍历。这样两个指针会在相交节点相遇。

算法步骤:
1. 初始化两个指针 pA 和 pB，分别指向链表 l1 和 l2 的头节点。
2. 当 pA 和 pB 不相等时：
   - 如果 pA 到达链表末尾，则将其切换到 l2 的头节点。
   - 如果 pB 到达链表末尾，则将其切换到 l1 的头节点。
   - 否则，pA 和 pB 分别向前移动一个节点。
3. 当 pA 和 pB 相等时，返回 pA 或 pB 即可。

关键点:
- 通过双指针法，确保两个指针在相交节点相遇。
- 保证时间复杂度为 O(n)，空间复杂度为 O(1)。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.solution import create_solution


def get_intersection_node(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    """
    找到两个链表的第一个相交节点
    :param headA: 第一个链表的头节点
    :param headB: 第二个链表的头节点
    :return: 第一个相交节点，如果没有相交则返回 None
    """
    if not headA or not headB:
        return None

    pA, pB = headA, headB

    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA

    return pA


Solution = create_solution(get_intersection_node)