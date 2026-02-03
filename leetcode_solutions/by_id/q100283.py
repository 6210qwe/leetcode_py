# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100283
标题: 推理二叉树
难度: medium
链接: https://leetcode.cn/problems/zhong-jian-er-cha-shu-lcof/
题目类型: 树、数组、哈希表、分治、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 124. 推理二叉树 - 某二叉树的先序遍历结果记录于整数数组 preorder，它的中序遍历结果记录于整数数组 inorder。请根据 preorder 和 inorder 的提示构造出这棵二叉树并返回其根节点。 注意：preorder 和 inorder 中均不含重复数字。 示例 1： [https://assets.leetcode.com/uploads/2021/02/19/tree.jpg] 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7] 输出: [3,9,20,null,null,15,7] 示例 2: 输入: preorder = [-1], inorder = [-1] 输出: [-1] 提示: * 1 <= preorder.length <= 3000 * inorder.length == preorder.length * -3000 <= preorder[i], inorder[i] <= 3000 * inorder 均出现在 preorder * preorder 保证 为二叉树的前序遍历序列 * inorder 保证 为二叉树的中序遍历序列 注意：本题与主站 105 题重复：https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/ [https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/]
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
