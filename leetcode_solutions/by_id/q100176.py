# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100176
标题: Check Balance LCCI
难度: easy
链接: https://leetcode.cn/problems/check-balance-lcci/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 04.04. 检查平衡性 - 实现一个函数，检查二叉树是否平衡。在这个问题中，平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。 示例 1： 给定二叉树 [3,9,20,null,null,15,7] 3 / \ 9 20 / \ 15 7 返回 true 。 示例 2： 给定二叉树 [1,2,2,3,3,null,null,4,4] 1 / \ 2 2 / \ 3 3 / \ 4 4 返回 false 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用后序遍历（自底向上）来计算每个节点的高度，并在计算过程中检查是否平衡。

算法步骤:
1. 定义一个辅助函数 `is_balanced_and_height`，返回一个布尔值和节点的高度。
2. 对于每个节点，递归地检查其左右子树是否平衡，并计算它们的高度。
3. 如果左右子树都平衡且高度差不超过 1，则该节点平衡，否则不平衡。
4. 返回根节点是否平衡。

关键点:
- 使用后序遍历可以避免重复计算节点的高度。
- 在递归过程中同时检查平衡性和计算高度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是二叉树的节点数。每个节点只被访问一次。
空间复杂度: O(h)，其中 h 是二叉树的高度。递归调用栈的深度最多为 h。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def is_balanced_and_height(node: Optional[TreeNode]) -> (bool, int):
    if not node:
        return True, 0
    
    left_balanced, left_height = is_balanced_and_height(node.left)
    right_balanced, right_height = is_balanced_and_height(node.right)
    
    balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
    height = max(left_height, right_height) + 1
    
    return balanced, height

def solution_function_name(root: Optional[TreeNode]) -> bool:
    """
    函数式接口 - 检查二叉树是否平衡
    """
    balanced, _ = is_balanced_and_height(root)
    return balanced

Solution = create_solution(solution_function_name)