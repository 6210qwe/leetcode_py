# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 549
标题: Binary Tree Longest Consecutive Sequence II
难度: medium
链接: https://leetcode.cn/problems/binary-tree-longest-consecutive-sequence-ii/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
549. 二叉树最长连续序列 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）来遍历树，并在遍历过程中记录当前节点的最长递增和递减序列长度。

算法步骤:
1. 定义一个辅助函数 `dfs`，该函数返回以当前节点为根的最长递增序列长度和最长递减序列长度。
2. 对于每个节点，计算其左子树和右子树的最长递增和递减序列长度。
3. 如果当前节点值比其左/右子节点值大1，则更新当前节点的最长递减序列长度。
4. 如果当前节点值比其左/右子节点值小1，则更新当前节点的最长递增序列长度。
5. 更新全局最长连续序列长度。
6. 返回当前节点的最长递增和递减序列长度。

关键点:
- 使用DFS遍历树，并在遍历过程中记录最长递增和递减序列长度。
- 通过比较当前节点与其子节点的值来更新序列长度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点只被访问一次。
空间复杂度: O(h)，其中 h 是树的高度。递归调用栈的深度最多为树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0
        
        def dfs(node: Optional[TreeNode]) -> (int, int):
            if not node:
                return 0, 0
            
            inc, dec = 1, 1
            left_inc, left_dec = dfs(node.left)
            right_inc, right_dec = dfs(node.right)
            
            if node.left:
                if node.val == node.left.val + 1:
                    inc = max(inc, left_inc + 1)
                elif node.val == node.left.val - 1:
                    dec = max(dec, left_dec + 1)
            
            if node.right:
                if node.val == node.right.val + 1:
                    inc = max(inc, right_inc + 1)
                elif node.val == node.right.val - 1:
                    dec = max(dec, right_dec + 1)
            
            self.max_length = max(self.max_length, inc + dec - 1)
            return inc, dec
        
        dfs(root)
        return self.max_length

Solution = create_solution(Solution)