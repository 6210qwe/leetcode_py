# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2843
标题: Extract Kth Character From The Rope Tree
难度: easy
链接: https://leetcode.cn/problems/extract-kth-character-from-the-rope-tree/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2689. 从 Rope 树中提取第 K 个字符 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）遍历 Rope 树，找到第 k 个字符。

算法步骤:
1. 定义一个递归函数 dfs(node, k) 来遍历节点。
2. 如果当前节点是叶子节点（即字符串），检查 k 是否在当前字符串的范围内。
3. 如果 k 在当前字符串的范围内，返回该字符。
4. 如果当前节点是非叶子节点，递归调用 dfs 函数遍历左子树和右子树。
5. 返回结果。

关键点:
- 通过递归遍历树结构，确保时间复杂度最优。
- 通过提前返回，减少不必要的计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 Rope 树中的节点数。最坏情况下需要遍历所有节点。
空间复杂度: O(h)，其中 h 是 Rope 树的高度。递归调用栈的深度取决于树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class Solution:
    def getKthCharacter(self, root: Optional[TreeNode], k: int) -> str:
        def dfs(node: Optional[TreeNode], k: int) -> str:
            if not node:
                return ""
            
            if isinstance(node.val, str):
                # 叶子节点，直接返回字符
                if 0 < k <= len(node.val):
                    return node.val[k - 1]
                else:
                    return ""
            
            left_result = dfs(node.left, k)
            if left_result:
                return left_result
            
            right_result = dfs(node.right, k - (len(node.left.val) if node.left and isinstance(node.left.val, str) else 0))
            return right_result
        
        return dfs(root, k)

Solution = create_solution(Solution)