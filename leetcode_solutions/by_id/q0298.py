# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 298
标题: Binary Tree Longest Consecutive Sequence
难度: medium
链接: https://leetcode.cn/problems/binary-tree-longest-consecutive-sequence/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
298. 二叉树最长连续序列 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: DFS遍历，维护当前连续序列长度

算法步骤:
1. DFS遍历二叉树
2. 如果当前节点值=父节点值+1，连续长度+1
3. 否则连续长度重置为1
4. 更新最大长度

关键点:
- DFS遍历
- 维护连续长度
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 遍历所有节点
空间复杂度: O(h) - 递归栈空间，h为树高
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def longest_consecutive(root: Optional[TreeNode]) -> int:
    """
    函数式接口 - 二叉树最长连续序列
    
    实现思路:
    DFS遍历，维护当前连续序列长度。
    
    Args:
        root: 二叉树根节点
        
    Returns:
        最长连续序列长度
        
    Example:
        >>> root = TreeNode(1)
        >>> root.right = TreeNode(3)
        >>> root.right.left = TreeNode(2)
        >>> root.right.right = TreeNode(4)
        >>> longest_consecutive(root)
        2
    """
    max_len = 0
    
    def dfs(node: Optional[TreeNode], parent_val: Optional[int], length: int):
        """DFS遍历"""
        nonlocal max_len
        
        if not node:
            return
        
        # 如果当前节点值=父节点值+1，连续长度+1
        if parent_val is not None and node.val == parent_val + 1:
            length += 1
        else:
            length = 1
        
        max_len = max(max_len, length)
        
        dfs(node.left, node.val, length)
        dfs(node.right, node.val, length)
    
    dfs(root, None, 0)
    return max_len


# 自动生成Solution类（无需手动编写）
Solution = create_solution(longest_consecutive)
