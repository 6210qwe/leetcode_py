# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 382
标题: Linked List Random Node
难度: medium
链接: https://leetcode.cn/problems/linked-list-random-node/
题目类型: 水塘抽样、链表、数学、随机化
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
382. 链表随机节点 - 给你一个单链表，随机选择链表的一个节点，并返回相应的节点值。每个节点 被选中的概率一样 。 实现 Solution 类： * Solution(ListNode head) 使用整数数组初始化对象。 * int getRandom() 从链表中随机选择一个节点并返回该节点的值。链表中所有节点被选中的概率相等。 示例： [https://assets.leetcode.com/uploads/2021/03/16/getrand-linked-list.jpg] 输入 ["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"] [[[1, 2, 3]], [], [], [], [], []] 输出 [null, 1, 3, 2, 2, 3] 解释 Solution solution = new Solution([1, 2, 3]); solution.getRandom(); // 返回 1 solution.getRandom(); // 返回 3 solution.getRandom(); // 返回 2 solution.getRandom(); // 返回 2 solution.getRandom(); // 返回 3 // getRandom() 方法应随机返回 1、2、3中的一个，每个元素被返回的概率相等。 提示： * 链表中的节点数在范围 [1, 104] 内 * -104 <= Node.val <= 104 * 至多调用 getRandom 方法 104 次 进阶： * 如果链表非常大且长度未知，该怎么处理？ * 你能否在不使用额外空间的情况下解决此问题？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用水塘抽样（Reservoir Sampling），在单次遍历未知长度链表的过程中，以等概率选出一个节点

算法步骤:
1. 构造函数中保存链表头指针 head，后续每次调用 getRandom 从头开始遍历。
2. 在一次遍历中维护变量：
   - i 表示目前已经访问的节点数，从 1 开始计数；
   - ans 表示当前选中的节点值。
3. 遍历时对于第 i 个节点：
   - 以 1/i 的概率将 ans 更新为该节点值；
   - 以 (i-1)/i 的概率保持 ans 不变。
4. 遍历结束后返回 ans，可证明每个节点被选中的概率均为 1/n。
5. 如果链表长度已知或可预先存入数组，也可以一次性拷贝为数组后用随机下标选取，但会额外占用 O(n) 空间。

关键点:
- 水塘抽样的概率不变性：第 i 个元素最终被选中的概率为 (1/i) * ∏_{j=i+1..n} (1 - 1/j) = 1/n。
- 不依赖链表长度 n，适用于「长度未知或过大」的场景。
- 需要使用高质量的均匀随机数生成函数（如 Python 的 random.random()）。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 每次调用 getRandom 需要遍历一遍链表。
空间复杂度: O(1) - 只使用常数个变量，不额外存储链表内容。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
import random
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def linked_list_random_node(head: Optional[ListNode]) -> int:
    """
    使用水塘抽样从单链表中等概率地随机选择一个节点值。
    """
    if head is None:
        raise ValueError("head cannot be None")

    i = 0
    chosen = 0
    cur = head
    while cur:
        i += 1
        # 以 1/i 的概率选择当前节点
        if random.randrange(i) == 0:
            chosen = cur.val
        cur = cur.next
    return chosen


# 自动生成Solution类（无需手动编写）
Solution = create_solution(linked_list_random_node)
