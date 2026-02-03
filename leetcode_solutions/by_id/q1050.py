# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1050
标题: Construct Binary Search Tree from Preorder Traversal
难度: medium
链接: https://leetcode.cn/problems/construct-binary-search-tree-from-preorder-traversal/
题目类型: 栈、树、二叉搜索树、数组、二叉树、单调栈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1008. 前序遍历构造二叉搜索树 - 给定一个整数数组，它表示BST(即 二叉搜索树 )的 先序遍历 ，构造树并返回其根。 保证 对于给定的测试用例，总是有可能找到具有给定需求的二叉搜索树。 二叉搜索树 是一棵二叉树，其中每个节点， Node.left 的任何后代的值 严格小于 Node.val , Node.right 的任何后代的值 严格大于 Node.val。 二叉树的 前序遍历 首先显示节点的值，然后遍历Node.left，最后遍历Node.right。 示例 1： [https://assets.leetcode.com/uploads/2019/03/06/1266.png] 输入：preorder = [8,5,1,7,10,12] 输出：[8,5,10,1,7,null,12] 示例 2: 输入: preorder = [1,3] 输出: [1,null,3] 提示： * 1 <= preorder.length <= 100 * 1 <= preorder[i] <= 10^8 * preorder 中的值 互不相同
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
