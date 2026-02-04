# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2399
标题: Minimum Flips in Binary Tree to Get Result
难度: hard
链接: https://leetcode.cn/problems/minimum-flips-in-binary-tree-to-get-result/
题目类型: 树、深度优先搜索、动态规划、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2313. 二叉树中得到结果所需的最少翻转次数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）遍历二叉树，并在每个节点上计算最小翻转次数。

算法步骤:
1. 定义一个递归函数 `dfs`，用于计算从当前节点开始的最小翻转次数。
2. 在 `dfs` 函数中，分别计算左子树和右子树的最小翻转次数。
3. 根据当前节点的操作符（AND, OR, XOR），计算当前节点的最小翻转次数。
4. 返回根节点的最小翻转次数。

关键点:
- 使用动态规划的思想，通过递归计算每个节点的最小翻转次数。
- 对于每个节点，需要考虑其左右子树的不同状态组合。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是二叉树的节点数。每个节点只被访问一次。
空间复杂度: O(h)，其中 h 是二叉树的高度。递归调用栈的深度最多为树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def dfs(node: Optional[TreeNode]) -> (int, int):
    if not node:
        return 0, 0
    
    left_true, left_false = dfs(node.left)
    right_true, right_false = dfs(node.right)
    
    if node.val == 2:  # AND
        true_flips = min(left_true + right_true, left_true + right_false + 1, left_false + right_true + 1, left_false + right_false + 2)
        false_flips = min(left_true + right_true + 2, left_true + right_false + 1, left_false + right_true + 1, left_false + right_false)
    elif node.val == 3:  # OR
        true_flips = min(left_true + right_true, left_true + right_false + 1, left_false + right_true + 1, left_false + right_false + 2)
        false_flips = min(left_true + right_true + 2, left_true + right_false + 1, left_false + right_true + 1, left_false + right_false)
    else:  # XOR
        true_flips = min(left_true + right_false, left_false + right_true)
        false_flips = min(left_true + right_true, left_false + right_false)
    
    return true_flips, false_flips

def solution_function_name(root: Optional[TreeNode]) -> int:
    """
    函数式接口 - 计算二叉树中得到结果所需的最少翻转次数
    """
    true_flips, false_flips = dfs(root)
    return min(true_flips, false_flips + 1)

Solution = create_solution(solution_function_name)