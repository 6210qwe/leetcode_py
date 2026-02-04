# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1780
标题: Lowest Common Ancestor of a Binary Tree II
难度: medium
链接: https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree-ii/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
给定一棵二叉树，找到两个指定节点的最近公共祖先。如果两个节点中有一个不存在于树中，则返回 None。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来查找两个节点，并记录它们的路径。然后找到两条路径的最后一个共同节点。

算法步骤:
1. 定义一个辅助函数 `find_path`，用于找到从根节点到目标节点的路径。
2. 分别调用 `find_path` 找到从根节点到 p 和 q 的路径。
3. 如果 p 或 q 不存在于树中，返回 None。
4. 比较两条路径，找到最后一个共同节点。

关键点:
- 使用 DFS 来找到路径。
- 比较路径时，找到最后一个共同节点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。在最坏情况下，我们需要遍历整个树来找到路径。
空间复杂度: O(h)，其中 h 是树的高度。递归调用栈的深度最多为树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def find_path(root: TreeNode, target: TreeNode, path: List[TreeNode]) -> bool:
    if not root:
        return False
    path.append(root)
    if root == target:
        return True
    if (root.left and find_path(root.left, target, path)) or (root.right and find_path(root.right, target, path)):
        return True
    path.pop()
    return False

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'Optional[TreeNode]':
        path_p = []
        path_q = []
        
        if not find_path(root, p, path_p) or not find_path(root, q, path_q):
            return None
        
        i = 0
        while i < len(path_p) and i < len(path_q) and path_p[i] == path_q[i]:
            i += 1
        
        return path_p[i - 1]

Solution = create_solution(Solution)