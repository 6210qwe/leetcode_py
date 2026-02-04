# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1267
标题: Remove Zero Sum Consecutive Nodes from Linked List
难度: medium
链接: https://leetcode.cn/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
题目类型: 哈希表、链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1171. 从链表中删去总和值为零的连续节点 - 给你一个链表的头节点 head，请你编写代码，反复删去链表中由 总和 值为 0 的连续节点组成的序列，直到不存在这样的序列为止。 删除完毕后，请你返回最终结果链表的头节点。 你可以返回任何满足题目要求的答案。 （注意，下面示例中的所有序列，都是对 ListNode 对象序列化的表示。） 示例 1： 输入：head = [1,2,-3,3,1] 输出：[3,1] 提示：答案 [1,2,1] 也是正确的。 示例 2： 输入：head = [1,2,3,-3,4] 输出：[1,2,4] 示例 3： 输入：head = [1,2,3,-3,-2] 输出：[1] 提示： * 给你的链表中可能有 1 到 1000 个节点。 * 对于链表中的每个节点，节点的值：-1000 <= node.val <= 1000.
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表记录前缀和，当某个前缀和再次出现时，说明中间的节点和为0，可以删除。

算法步骤:
1. 初始化一个虚拟头节点 dummy 和一个指针 current。
2. 使用一个哈希表 prefix_sum_map 来记录前缀和及其对应的节点。
3. 遍历链表，计算当前节点的前缀和。
4. 如果当前前缀和已经在哈希表中存在，说明从上一次出现该前缀和的节点到当前节点之间的节点和为0，删除这些节点。
5. 否则，将当前前缀和及其对应的节点存入哈希表。
6. 返回处理后的链表头节点。

关键点:
- 使用哈希表记录前缀和及其对应的节点，以便快速找到需要删除的节点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是链表的长度。我们只需要遍历链表一次。
空间复杂度: O(n)，最坏情况下哈希表中存储了 n 个前缀和。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.solution import create_solution


def remove_zero_sum_sublists(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    函数式接口 - 从链表中删去总和值为零的连续节点
    """
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    prefix_sum = 0
    prefix_sum_map = {}

    while current:
        prefix_sum += current.val
        if prefix_sum in prefix_sum_map:
            # 删除从 prefix_sum_map[prefix_sum].next 到 current 之间的节点
            to_delete = prefix_sum_map[prefix_sum].next
            temp_sum = prefix_sum + to_delete.val
            while temp_sum != prefix_sum:
                del prefix_sum_map[temp_sum]
                to_delete = to_delete.next
                temp_sum += to_delete.val
            prefix_sum_map[prefix_sum].next = current.next
        else:
            prefix_sum_map[prefix_sum] = current
        current = current.next

    return dummy.next


Solution = create_solution(remove_zero_sum_sublists)