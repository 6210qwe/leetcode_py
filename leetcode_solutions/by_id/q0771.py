# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 771
标题: Encode N-ary Tree to Binary Tree
难度: hard
链接: https://leetcode.cn/problems/encode-n-ary-tree-to-binary-tree/
题目类型: 树、深度优先搜索、广度优先搜索、设计、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
431. 将 N 叉树编码为二叉树 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 将 N 叉树编码为二叉树。对于每个节点，左子树表示第一个子节点，右子树表示下一个兄弟节点。

算法步骤:
1. 对于每个 N 叉树节点，创建一个对应的二叉树节点。
2. 将第一个子节点作为当前节点的左子节点。
3. 将后续的子节点依次作为前一个子节点的右子节点。
4. 递归处理每个子节点。

关键点:
- 使用二叉树的左子树表示 N 叉树的第一个子节点。
- 使用二叉树的右子树表示 N 叉树的下一个兄弟节点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 N 叉树中的节点数。每个节点只被访问一次。
空间复杂度: O(h)，其中 h 是 N 叉树的高度。递归调用栈的深度最多为 N 叉树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode, Node

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        if not root:
            return None
        
        binary_root = TreeNode(root.val)
        if root.children:
            binary_root.left = self.encode(root.children[0])
        
        # Connect the siblings
        current = binary_root.left
        for child in root.children[1:]:
            current.right = self.encode(child)
            current = current.right
        
        return binary_root
    
    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        if not data:
            return None
        
        nary_root = Node(data.val, [])
        current = data.left
        while current:
            nary_root.children.append(self.decode(current))
            current = current.right
        
        return nary_root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))

Solution = create_solution(Codec)