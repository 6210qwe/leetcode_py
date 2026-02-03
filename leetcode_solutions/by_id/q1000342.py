# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000342
标题: 合并 K 个升序链表
难度: hard
链接: https://leetcode.cn/problems/vvXgSW/
题目类型: 链表、分治、堆（优先队列）、归并排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 078. 合并 K 个升序链表 - 给定一个链表数组，每个链表都已经按升序排列。 请将所有链表合并到一个升序链表中，返回合并后的链表。 示例 1： 输入：lists = [[1,4,5],[1,3,4],[2,6]] 输出：[1,1,2,3,4,4,5,6] 解释：链表数组如下： [ 1->4->5, 1->3->4, 2->6 ] 将它们合并到一个有序链表中得到。 1->1->2->3->4->4->5->6 示例 2： 输入：lists = [] 输出：[] 示例 3： 输入：lists = [[]] 输出：[] 提示： * k == lists.length * 0 <= k <= 10^4 * 0 <= lists[i].length <= 500 * -10^4 <= lists[i][j] <= 10^4 * lists[i] 按 升序 排列 * lists[i].length 的总和不超过 10^4 注意：本题与主站 23 题相同： https://leetcode.cn/problems/merge-k-sorted-lists/ [https://leetcode.cn/problems/merge-k-sorted-lists/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用最小堆，每次取出最小的节点

算法步骤:
1. 将所有链表的头节点加入最小堆
2. 每次取出堆顶节点，加入结果链表
3. 如果该节点还有下一个节点，将其加入堆

关键点:
- 最小堆维护k个链表的当前最小节点
- 时间复杂度O(n log k)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log k) - n为总节点数，k为链表数
空间复杂度: O(k) - 堆空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
import heapq
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    函数式接口 - 合并 K 个升序链表
    
    实现思路:
    使用最小堆，每次取出最小的节点。
    
    Args:
        lists: 链表数组
        
    Returns:
        合并后的链表头节点
        
    Example:
        >>> lists = [ListNode(1), ListNode(1), ListNode(2)]
        >>> result = merge_k_lists(lists)
    """
    if not lists:
        return None
    
    # 最小堆
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    
    dummy = ListNode(0)
    curr = dummy
    
    while heap:
        val, idx, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, idx, node.next))
    
    return dummy.next


Solution = create_solution(merge_k_lists)
