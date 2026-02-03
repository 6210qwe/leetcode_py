# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 23
标题: Merge k Sorted Lists
难度: hard
链接: https://leetcode.cn/problems/merge-k-sorted-lists/
题目类型: 链表、分治、堆（优先队列）、归并排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
23. 合并 K 个升序链表 - 给你一个链表数组，每个链表都已经按升序排列。 请你将所有链表合并到一个升序链表中，返回合并后的链表。 示例 1： 输入：lists = [[1,4,5],[1,3,4],[2,6]] 输出：[1,1,2,3,4,4,5,6] 解释：链表数组如下： [ 1->4->5, 1->3->4, 2->6 ] 将它们合并到一个有序链表中得到。 1->1->2->3->4->4->5->6 示例 2： 输入：lists = [] 输出：[] 示例 3： 输入：lists = [[]] 输出：[] 提示： * k == lists.length * 0 <= k <= 10^4 * 0 <= lists[i].length <= 500 * -10^4 <= lists[i][j] <= 10^4 * lists[i] 按 升序 排列 * lists[i].length 的总和不超过 10^4
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 分治合并，将k个链表两两合并，重复直到只剩一个链表

算法步骤:
1. 如果链表数组为空，返回None
2. 使用分治思想，将链表数组分成两部分
3. 递归合并两部分
4. 使用合并两个有序链表的方法合并两个链表
5. 返回合并后的链表

关键点:
- 分治合并比顺序合并更高效，时间复杂度O(nlogk)
- 每次合并将链表数量减半，共logk层
- 每层需要合并所有节点，总节点数为n
- 空间复杂度O(logk)，递归栈的深度
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(nlogk) - n为所有节点的总数，k为链表数量，分治合并需要logk层
空间复杂度: O(logk) - 递归栈的深度为logk
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.solution import create_solution


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    函数式接口 - 分治合并实现
    
    实现思路:
    使用分治思想，将k个链表两两合并，递归合并直到只剩一个链表。
    
    Args:
        lists: 链表数组
        
    Returns:
        合并后的有序链表
        
    Example:
        >>> lists = [ListNode.from_list([1,4,5]), ListNode.from_list([1,3,4]), ListNode.from_list([2,6])]
        >>> result = merge_k_lists(lists)
        >>> result.to_list()
        [1, 1, 2, 3, 4, 4, 5, 6]
    """
    if not lists:
        return None
    
    def merge_two(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """合并两个有序链表"""
        dummy = ListNode(0)
        cur = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 if list1 else list2
        return dummy.next
    
    def merge_lists(left: int, right: int) -> Optional[ListNode]:
        """分治合并"""
        if left == right:
            return lists[left]
        mid = (left + right) // 2
        left_list = merge_lists(left, mid)
        right_list = merge_lists(mid + 1, right)
        return merge_two(left_list, right_list)
    
    return merge_lists(0, len(lists) - 1)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(merge_k_lists)
