# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1484
标题: Linked List in Binary Tree
难度: medium
链接: https://leetcode.cn/problems/linked-list-in-binary-tree/
题目类型: 树、深度优先搜索、链表、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1367. 二叉树中的链表 - 给你一棵以 root 为根的二叉树和一个 head 为第一个节点的链表。 如果在二叉树中，存在一条一直向下的路径，且每个点的数值恰好一一对应以 head 为首的链表中每个节点的值，那么请你返回 True ，否则返回 False 。 一直向下的路径的意思是：从树中某个节点开始，一直连续向下的路径。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/29/sample_1_1720.png] 输入：head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3] 输出：true 解释：树中蓝色的节点构成了与链表对应的子路径。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/29/sample_2_1720.png] 输入：head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3] 输出：true 示例 3： 输入：head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3] 输出：false 解释：二叉树中不存在一一对应链表的路径。 提示： * 二叉树和链表中的每个节点的值都满足 1 <= node.val <= 100 。 * 链表包含的节点数目在 1 到 100 之间。 * 二叉树包含的节点数目在 1 到 2500 之间。
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
