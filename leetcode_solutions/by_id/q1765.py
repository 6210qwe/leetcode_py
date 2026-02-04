# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1765
标题: Merge In Between Linked Lists
难度: medium
链接: https://leetcode.cn/problems/merge-in-between-linked-lists/
题目类型: 链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1669. 合并两个链表 - 给你两个链表 list1 和 list2 ，它们包含的元素分别为 n 个和 m 个。 请你将 list1 中下标从 a 到 b 的全部节点都删除，并将list2 接在被删除节点的位置。 下图中蓝色边和节点展示了操作后的结果： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/11/28/fig1.png] 请你返回结果链表的头指针。 示例 1： [https://pic.leetcode.cn/1709608717-NVGojm-image.png] 输入：list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002] 输出：[10,1,13,1000000,1000001,1000002,5] 解释：我们删除 list1 中下标为 3 和 4 的两个节点，并将 list2 接在该位置。上图中蓝色的边和节点为答案链表。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/11/28/merge_linked_list_ex2.png] 输入：list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004] 输出：[0,1,1000000,1000001,1000002,1000003,1000004,6] 解释：上图中蓝色的边和节点为答案链表。 提示： * 3 <= list1.length <= 104 * 1 <= a <= b < list1.length - 1 * 1 <= list2.length <= 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
- 找到 list1 中下标为 a-1 和 b+1 的节点。
- 将 list2 插入到这两个节点之间。

算法步骤:
1. 遍历 list1，找到下标为 a-1 的节点（记为 prev）。
2. 继续遍历 list1，找到下标为 b+1 的节点（记为 next）。
3. 将 prev 的 next 指向 list2 的头节点。
4. 将 list2 的尾节点的 next 指向 next 节点。
5. 返回 list1 的头节点。

关键点:
- 确保正确处理边界情况，如 a=0 或 b=list1.length-1。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 list1 的长度，m 是 list2 的长度。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.solution import create_solution


def merge_in_between(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    """
    合并两个链表 - 将 list1 中下标从 a 到 b 的全部节点都删除，并将 list2 接在被删除节点的位置。
    """
    # 找到下标为 a-1 的节点
    prev = list1
    for _ in range(a - 1):
        prev = prev.next
    
    # 找到下标为 b+1 的节点
    current = prev
    for _ in range(b - a + 2):
        current = current.next
    
    # 将 prev 的 next 指向 list2 的头节点
    prev.next = list2
    
    # 找到 list2 的尾节点
    while list2.next:
        list2 = list2.next
    
    # 将 list2 的尾节点的 next 指向 current 节点
    list2.next = current
    
    return list1


Solution = create_solution(merge_in_between)