# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3501
标题: Delete Nodes From Linked List Present in Array
难度: medium
链接: https://leetcode.cn/problems/delete-nodes-from-linked-list-present-in-array/
题目类型: 数组、哈希表、链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3217. 从链表中移除在数组中存在的节点 - 给你一个整数数组 nums 和一个链表的头节点 head。从链表中移除所有存在于 nums 中的节点后，返回修改后的链表的头节点。 示例 1： 输入： nums = [1,2,3], head = [1,2,3,4,5] 输出： [4,5] 解释： [https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample0.png] 移除数值为 1, 2 和 3 的节点。 示例 2： 输入： nums = [1], head = [1,2,1,2,1,2] 输出： [2,2,2] 解释： [https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample1.png] 移除数值为 1 的节点。 示例 3： 输入： nums = [5], head = [1,2,3,4] 输出： [1,2,3,4] 解释： [https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample2.png] 链表中不存在值为 5 的节点。 提示： * 1 <= nums.length <= 105 * 1 <= nums[i] <= 105 * nums 中的所有元素都是唯一的。 * 链表中的节点数在 [1, 105] 的范围内。 * 1 <= Node.val <= 105 * 输入保证链表中至少有一个值没有在 nums 中出现过。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希集合来存储需要删除的节点值，并遍历链表进行删除操作。

算法步骤:
1. 将 `nums` 转换为哈希集合，以便快速查找。
2. 使用一个虚拟头节点 `dummy` 来简化边界条件处理。
3. 遍历链表，如果当前节点的值在哈希集合中，则跳过该节点；否则，继续遍历。
4. 返回修改后的链表头节点。

关键点:
- 使用哈希集合来实现 O(1) 时间复杂度的查找。
- 使用虚拟头节点来简化边界条件处理。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 `nums` 的长度，m 是链表的长度。
空间复杂度: O(n)，用于存储 `nums` 的哈希集合。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def remove_nodes_from_linked_list(nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
    """
    从链表中移除所有存在于 nums 中的节点后，返回修改后的链表的头节点。
    """
    # 将 nums 转换为哈希集合
    num_set = set(nums)
    
    # 创建虚拟头节点
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    
    # 遍历链表
    while current.next:
        if current.next.val in num_set:
            current.next = current.next.next
        else:
            current = current.next
    
    return dummy.next


Solution = create_solution(remove_nodes_from_linked_list)