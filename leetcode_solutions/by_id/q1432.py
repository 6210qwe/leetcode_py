# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1432
标题: Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
难度: medium
链接: https://leetcode.cn/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/
题目类型: 树、深度优先搜索、广度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1430. 判断给定的序列是否是二叉树从根到叶的路径 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）来检查是否存在一条从根节点到叶子节点的路径，使得路径上的节点值与给定数组中的值一一对应。

算法步骤:
1. 定义一个递归函数 `dfs`，参数包括当前节点、当前数组索引。
2. 如果当前节点为空，返回 False。
3. 如果当前节点值不等于数组中对应索引的值，返回 False。
4. 如果当前节点是叶子节点且数组索引指向最后一个元素，返回 True。
5. 递归调用 `dfs` 检查左子节点和右子节点。
6. 返回左子节点或右子节点的结果。

关键点:
- 递归终止条件：当前节点为空、当前节点值不匹配、叶子节点且数组索引指向最后一个元素。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点最多访问一次。
空间复杂度: O(h)，其中 h 是树的高度。递归调用栈的深度最多为树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def is_valid_sequence(root: Optional[TreeNode], arr: List[int]) -> bool:
    def dfs(node: Optional[TreeNode], index: int) -> bool:
        if not node:
            return False
        if index == len(arr) or node.val != arr[index]:
            return False
        if not node.left and not node.right and index == len(arr) - 1:
            return True
        return dfs(node.left, index + 1) or dfs(node.right, index + 1)
    
    return dfs(root, 0)

Solution = create_solution(is_valid_sequence)