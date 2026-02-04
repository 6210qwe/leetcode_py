# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 687
标题: Longest Univalue Path
难度: medium
链接: https://leetcode.cn/problems/longest-univalue-path/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
687. 最长同值路径 - 给定一个二叉树的 root ，返回 最长的路径的长度 ，这个路径中的 每个节点具有相同值 。 这条路径可以经过也可以不经过根节点。 两个节点之间的路径长度 由它们之间的边数表示。 示例 1: [https://assets.leetcode.com/uploads/2020/10/13/ex1.jpg] 输入：root = [5,4,5,1,1,5] 输出：2 示例 2: [https://assets.leetcode.com/uploads/2020/10/13/ex2.jpg] 输入：root = [1,4,5,4,4,5] 输出：2 提示: * 树的节点数的范围是 [0, 104] * -1000 <= Node.val <= 1000 * 树的深度将不超过 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）来遍历树，并在遍历过程中计算最长同值路径。

算法步骤:
1. 定义一个辅助函数 `dfs`，用于递归遍历树。
2. 在 `dfs` 函数中，计算当前节点的左子树和右子树的最长同值路径。
3. 如果当前节点的左子节点或右子节点与当前节点值相同，则更新最长同值路径。
4. 返回当前节点的最长同值路径。

关键点:
- 使用全局变量 `max_length` 来记录最长同值路径的长度。
- 递归过程中，传递当前节点的值作为参数，以便比较子节点的值。
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
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0
        
        def dfs(node: Optional[TreeNode], parent_val: int) -> int:
            if not node:
                return 0
            
            left_length = dfs(node.left, node.val)
            right_length = dfs(node.right, node.val)
            
            self.max_length = max(self.max_length, left_length + right_length)
            
            if node.val == parent_val:
                return max(left_length, right_length) + 1
            else:
                return 0
        
        dfs(root, None)
        return self.max_length

Solution = create_solution(Solution)