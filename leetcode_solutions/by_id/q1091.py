# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1091
标题: Maximum Average Subtree
难度: medium
链接: https://leetcode.cn/problems/maximum-average-subtree/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1120. 子树的最大平均值 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）遍历二叉树，计算每个子树的节点和与节点数，从而得到每个子树的平均值。

算法步骤:
1. 定义一个递归函数 `dfs`，用于计算当前子树的节点和与节点数。
2. 在 `dfs` 函数中，递归计算左子树和右子树的节点和与节点数。
3. 计算当前子树的节点和与节点数，并更新最大平均值。
4. 返回当前子树的节点和与节点数。

关键点:
- 通过递归遍历每个节点，确保每个子树都被计算到。
- 使用全局变量 `max_avg` 来记录最大平均值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是二叉树的节点数。每个节点只被访问一次。
空间复杂度: O(h)，其中 h 是二叉树的高度。递归调用栈的深度为树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.max_avg = 0.0
        
        def dfs(node: Optional[TreeNode]) -> (int, int):
            if not node:
                return 0, 0
            
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            current_sum = left_sum + right_sum + node.val
            current_count = left_count + right_count + 1
            current_avg = current_sum / current_count
            
            self.max_avg = max(self.max_avg, current_avg)
            
            return current_sum, current_count
        
        dfs(root)
        return self.max_avg

Solution = create_solution(Solution)