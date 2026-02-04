# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 835
标题: Linked List Components
难度: medium
链接: https://leetcode.cn/problems/linked-list-components/
题目类型: 数组、哈希表、链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
817. 链表组件 - 给定链表头结点 head，该链表上的每个结点都有一个 唯一的整型值 。同时给定列表 nums，该列表是上述链表中整型值的一个子集。 返回列表 nums 中组件的个数，这里对组件的定义为：链表中一段最长连续结点的值（该值必须在列表 nums 中）构成的集合。 示例 1： [https://assets.leetcode.com/uploads/2021/07/22/lc-linkedlistcom1.jpg] 输入: head = [0,1,2,3], nums = [0,1,3] 输出: 2 解释: 链表中,0 和 1 是相连接的，且 nums 中不包含 2，所以 [0, 1] 是 nums 的一个组件，同理 [3] 也是一个组件，故返回 2。 示例 2： [https://assets.leetcode.com/uploads/2021/07/22/lc-linkedlistcom2.jpg] 输入: head = [0,1,2,3,4], nums = [0,3,1,4] 输出: 2 解释: 链表中，0 和 1 是相连接的，3 和 4 是相连接的，所以 [0, 1] 和 [3, 4] 是两个组件，故返回 2。 提示： * 链表中节点数为n * 1 <= n <= 104 * 0 <= Node.val < n * Node.val 中所有值 不同 * 1 <= nums.length <= n * 0 <= nums[i] < n * nums 中所有值 不同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希集合来快速查找链表中的节点值是否在 nums 中，并通过遍历链表来计算组件的数量。

算法步骤:
1. 将 nums 转换为哈希集合，以便 O(1) 时间复杂度进行查找。
2. 初始化计数器 `count` 和标志变量 `in_component`。
3. 遍历链表：
   - 如果当前节点的值在哈希集合中且 `in_component` 为 False，则找到一个新的组件，将 `count` 加 1 并将 `in_component` 置为 True。
   - 如果当前节点的值不在哈希集合中且 `in_component` 为 True，则结束当前组件，将 `in_component` 置为 False。
4. 返回 `count`。

关键点:
- 使用哈希集合来快速查找节点值是否在 nums 中。
- 通过标志变量 `in_component` 来跟踪当前是否在一个组件中。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是链表的长度。我们只需遍历链表一次。
空间复杂度: O(m)，其中 m 是 nums 的长度。我们需要存储 nums 中的所有值以进行 O(1) 时间复杂度的查找。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(head: ListNode, nums: List[int]) -> int:
    """
    函数式接口 - 计算链表组件的数量
    """
    # 将 nums 转换为哈希集合
    num_set = set(nums)
    
    count = 0
    in_component = False
    
    # 遍历链表
    current = head
    while current:
        if current.val in num_set:
            if not in_component:
                count += 1
                in_component = True
        else:
            in_component = False
        current = current.next
    
    return count


Solution = create_solution(solution_function_name)