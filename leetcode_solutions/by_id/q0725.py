# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 725
标题: Split Linked List in Parts
难度: medium
链接: https://leetcode.cn/problems/split-linked-list-in-parts/
题目类型: 链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
725. 分隔链表 - 给你一个头结点为 head 的单链表和一个整数 k ，请你设计一个算法将链表分隔为 k 个连续的部分。 每部分的长度应该尽可能的相等：任意两部分的长度差距不能超过 1 。这可能会导致有些部分为 null 。 这 k 个部分应该按照在链表中出现的顺序排列，并且排在前面的部分的长度应该大于或等于排在后面的长度。 返回一个由上述 k 部分组成的数组。 示例 1： [https://assets.leetcode.com/uploads/2021/06/13/split1-lc.jpg] 输入：head = [1,2,3], k = 5 输出：[[1],[2],[3],[],[]] 解释： 第一个元素 output[0] 为 output[0].val = 1 ，output[0].next = null 。 最后一个元素 output[4] 为 null ，但它作为 ListNode 的字符串表示是 [] 。 示例 2： [https://assets.leetcode.com/uploads/2021/06/13/split2-lc.jpg] 输入：head = [1,2,3,4,5,6,7,8,9,10], k = 3 输出：[[1,2,3,4],[5,6,7],[8,9,10]] 解释： 输入被分成了几个连续的部分，并且每部分的长度相差不超过 1 。前面部分的长度大于等于后面部分的长度。 提示： * 链表中节点的数目在范围 [0, 1000] * 0 <= Node.val <= 1000 * 1 <= k <= 50
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 计算每个部分的长度，然后遍历链表进行分割。

算法步骤:
1. 计算链表的总长度。
2. 根据总长度和 k 计算每个部分的基本长度和额外长度。
3. 遍历链表，根据计算出的长度进行分割。

关键点:
- 计算每个部分的长度时，需要确保前面部分的长度大于或等于后面部分的长度。
- 在遍历链表时，正确处理每个部分的结尾，将其 next 设为 None。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + k)，其中 n 是链表的长度，k 是要分割的部分数。需要遍历链表一次来计算长度，然后再遍历链表进行分割。
空间复杂度: O(k)，存储结果数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def split_list_to_parts(head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    # 计算链表的总长度
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    
    # 计算每个部分的基本长度和额外长度
    part_length, extra_length = divmod(length, k)
    
    result = []
    current = head
    for i in range(k):
        part_head = current
        part_size = part_length + (1 if i < extra_length else 0)
        
        for _ in range(part_size - 1):
            if current:
                current = current.next
        
        if current:
            next_node = current.next
            current.next = None
            current = next_node
        
        result.append(part_head)
    
    return result


Solution = create_solution(split_list_to_parts)