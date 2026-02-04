# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 545
标题: Boundary of Binary Tree
难度: medium
链接: https://leetcode.cn/problems/boundary-of-binary-tree/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
545. 二叉树的边界 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过深度优先搜索 (DFS) 来分别找到二叉树的左边界、右边界和叶子节点。

算法步骤:
1. 找到根节点，并将其加入结果列表。
2. 通过 DFS 找到左边界（不包括叶子节点）。
3. 通过 DFS 找到所有叶子节点。
4. 通过 DFS 找到右边界（不包括叶子节点），并反向添加到结果列表中。
5. 返回结果列表。

关键点:
- 左边界是根节点到最左侧叶子节点的路径。
- 右边界是根节点到最右侧叶子节点的路径。
- 叶子节点是左右子节点都为空的节点。
- 在处理右边界时，需要反向添加到结果列表中。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是二叉树的节点数。每个节点只被访问一次。
空间复杂度: O(h)，其中 h 是二叉树的高度。递归调用栈的深度最多为 h。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def find_left_boundary(node: TreeNode, boundary: List[int]):
    if not node or (not node.left and not node.right):
        return
    boundary.append(node.val)
    if node.left:
        find_left_boundary(node.left, boundary)
    else:
        find_left_boundary(node.right, boundary)

def find_right_boundary(node: TreeNode, boundary: List[int]):
    if not node or (not node.left and not node.right):
        return
    if node.right:
        find_right_boundary(node.right, boundary)
    else:
        find_right_boundary(node.left, boundary)
    boundary.append(node.val)

def find_leaves(node: TreeNode, leaves: List[int]):
    if not node:
        return
    if not node.left and not node.right:
        leaves.append(node.val)
    find_leaves(node.left, leaves)
    find_leaves(node.right, leaves)

def solution_function_name(root: Optional[TreeNode]) -> List[int]:
    """
    函数式接口 - 返回二叉树的边界
    """
    if not root:
        return []
    
    boundary = [root.val]
    
    # 找到左边界
    if root.left:
        find_left_boundary(root.left, boundary)
    
    # 找到所有叶子节点
    find_leaves(root, boundary)
    
    # 找到右边界
    right_boundary = []
    if root.right:
        find_right_boundary(root.right, right_boundary)
    boundary.extend(right_boundary)
    
    return boundary

Solution = create_solution(solution_function_name)