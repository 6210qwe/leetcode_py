# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2182
标题: Find the Minimum and Maximum Number of Nodes Between Critical Points
难度: medium
链接: https://leetcode.cn/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/
题目类型: 链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2058. 找出临界点之间的最小和最大距离 - 链表中的 临界点 定义为一个 局部极大值点 或 局部极小值点 。 如果当前节点的值 严格大于 前一个节点和后一个节点，那么这个节点就是一个 局部极大值点 。 如果当前节点的值 严格小于 前一个节点和后一个节点，那么这个节点就是一个 局部极小值点 。 注意：节点只有在同时存在前一个节点和后一个节点的情况下，才能成为一个 局部极大值点 / 极小值点 。 给你一个链表 head ，返回一个长度为 2 的数组 [minDistance, maxDistance] ，其中 minDistance 是任意两个不同临界点之间的最小距离，maxDistance 是任意两个不同临界点之间的最大距离。如果临界点少于两个，则返回 [-1，-1] 。 示例 1： [https://assets.leetcode.com/uploads/2021/10/13/a1.png] 输入：head = [3,1] 输出：[-1,-1] 解释：链表 [3,1] 中不存在临界点。 示例 2： [https://assets.leetcode.com/uploads/2021/10/13/a2.png] 输入：head = [5,3,1,2,5,1,2] 输出：[1,3] 解释：存在三个临界点： - [5,3,1,2,5,1,2]：第三个节点是一个局部极小值点，因为 1 比 3 和 2 小。 - [5,3,1,2,5,1,2]：第五个节点是一个局部极大值点，因为 5 比 2 和 1 大。 - [5,3,1,2,5,1,2]：第六个节点是一个局部极小值点，因为 1 比 5 和 2 小。 第五个节点和第六个节点之间距离最小。minDistance = 6 - 5 = 1 。 第三个节点和第六个节点之间距离最大。maxDistance = 6 - 3 = 3 。 示例 3： [https://assets.leetcode.com/uploads/2021/10/14/a5.png] 输入：head = [1,3,2,2,3,2,2,2,7] 输出：[3,3] 解释：存在两个临界点： - [1,3,2,2,3,2,2,2,7]：第二个节点是一个局部极大值点，因为 3 比 1 和 2 大。 - [1,3,2,2,3,2,2,2,7]：第五个节点是一个局部极大值点，因为 3 比 2 和 2 大。 最小和最大距离都存在于第二个节点和第五个节点之间。 因此，minDistance 和 maxDistance 是 5 - 2 = 3 。 注意，最后一个节点不算一个局部极大值点，因为它之后就没有节点了。 示例 4： [https://assets.leetcode.com/uploads/2021/10/13/a4.png] 输入：head = [2,3,3,2] 输出：[-1,-1] 解释：链表 [2,3,3,2] 中不存在临界点。 提示： * 链表中节点的数量在范围 [2, 105] 内 * 1 <= Node.val <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 遍历链表，找到所有临界点，并记录它们的位置。然后计算这些位置之间的最小和最大距离。

算法步骤:
1. 初始化指针 prev, curr, next，分别指向链表的前一个节点、当前节点和下一个节点。
2. 遍历链表，检查当前节点是否是临界点（即局部极大值或局部极小值）。
3. 如果是临界点，记录其位置。
4. 计算临界点之间的最小和最大距离。
5. 返回结果。

关键点:
- 临界点的定义：当前节点的值严格大于或小于前后节点的值。
- 记录临界点的位置以便计算距离。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是链表的长度。我们只需遍历链表一次。
空间复杂度: O(1)，只使用常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_min_max_distance(head: ListNode) -> List[int]:
    if not head or not head.next or not head.next.next:
        return [-1, -1]

    prev = head
    curr = head.next
    next_node = head.next.next

    critical_points = []
    index = 1

    while next_node:
        if (prev.val < curr.val > next_node.val) or (prev.val > curr.val < next_node.val):
            critical_points.append(index)
        prev = curr
        curr = next_node
        next_node = next_node.next
        index += 1

    if len(critical_points) < 2:
        return [-1, -1]

    min_distance = min(critical_points[i + 1] - critical_points[i] for i in range(len(critical_points) - 1))
    max_distance = critical_points[-1] - critical_points[0]

    return [min_distance, max_distance]


Solution = create_solution(find_min_max_distance)