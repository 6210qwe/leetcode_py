# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 431
标题: 将 N 叉树编码为二叉树
难度: 中等
链接: https://leetcode.cn/problems/encode-n-ary-tree-to-binary-tree/
题目类型: 树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
设计一个算法，将 N 叉树编码为二叉树，并能将该二叉树解码为原 N 叉树。N 叉树是一种每个节点都有不超过 N 个子节点的树。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二叉树来表示 N 叉树

算法步骤:
1. 编码时，将 N 叉树的每个节点转换为二叉树的一个节点，左子节点指向第一个子节点，右子节点指向下一个兄弟节点。
2. 解码时，从二叉树的根节点开始，通过左子节点找到第一个子节点，通过右子节点找到下一个兄弟节点。

关键点:
- 注意边界条件，特别是空树和只有一个节点的情况
- 优化时间和空间复杂度，确保编码和解码过程高效
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 其中 n 是 N 叉树中的节点数，每个节点都需要访问一次
空间复杂度: O(1) - 除了输入和输出外，不需要额外的空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode, Node
from leetcode_solutions.utils.solution import create_solution


class Codec:

    def encode(self, root: 'Node') -> TreeNode:
        """
        Encodes an n-ary tree to a binary tree.
        
        Args:
            root: The root of the n-ary tree.
            
        Returns:
            The root of the encoded binary tree.
        """
        if not root:
            return None
        
        binary_root = TreeNode(root.val)
        if root.children:
            binary_root.left = self.encode(root.children[0])
        
        # Link the siblings
        current = binary_root.left
        for child in root.children[1:]:
            current.right = self.encode(child)
            current = current.right
        
        return binary_root

    def decode(self, data: TreeNode) -> 'Node':
        """
        Decodes your binary tree to an n-ary tree.
        
        Args:
            data: The root of the binary tree.
            
        Returns:
            The root of the decoded n-ary tree.
        """
        if not data:
            return None
        
        n_ary_root = Node(data.val, [])
        current = data.left
        while current:
            n_ary_root.children.append(self.decode(current))
            current = current.right
        
        return n_ary_root


# 自动生成Solution类（无需手动编写）
Solution = create_solution(Codec)