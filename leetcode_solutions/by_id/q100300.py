# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100300
标题: 随机链表的复制
难度: medium
链接: https://leetcode.cn/problems/fu-za-lian-biao-de-fu-zhi-lcof/
题目类型: 哈希表、链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 154. 复杂链表的复制 - 请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/09/e1.png] 输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]] 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]] 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/09/e2.png] 输入：head = [[1,1],[2,1]] 输出：[[1,1],[2,1]] 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/09/e3.png] 输入：head = [[3,null],[3,0],[3,null]] 输出：[[3,null],[3,0],[3,null]] 示例 4： 输入：head = [] 输出：[] 解释：给定的链表为空（空指针），因此返回 null。 提示： * -10000 <= Node.val <= 10000 * Node.random 为空（null）或指向链表中的节点。 * 节点数目不超过 1000 。 注意：本题与主站 138 题相同：https://leetcode.cn/problems/copy-list-with-random-pointer/ [https://leetcode.cn/problems/copy-list-with-random-pointer/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
