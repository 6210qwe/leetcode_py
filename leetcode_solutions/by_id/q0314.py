# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 314
标题: Binary Tree Vertical Order Traversal
难度: medium
链接: https://leetcode.cn/problems/binary-tree-vertical-order-traversal/
题目类型: 树、深度优先搜索、广度优先搜索、哈希表、二叉树、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
314. 二叉树的垂直遍历 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: BFS层序遍历，给每个节点分配列索引，根节点为0，左子节点-1，右子节点+1

算法步骤:
1. 使用BFS遍历二叉树，同时记录每个节点的列索引
2. 使用哈希表按列索引分组存储节点值
3. 按列索引排序后返回结果

关键点:
- 使用BFS保证同一列内从上到下的顺序
- 时间复杂度O(n)，空间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要访问每个节点一次
空间复杂度: O(n) - 队列和哈希表空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from collections import deque, defaultdict
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def binary_tree_vertical_order_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    """
    函数式接口 - 二叉树的垂直遍历
    
    实现思路:
    BFS层序遍历，给每个节点分配列索引，根节点为0，左子节点-1，右子节点+1。
    
    Args:
        root: 二叉树的根节点
        
    Returns:
        按列索引排序的节点值列表
        
    Example:
        >>> root = TreeNode.from_list([3, 9, 20, None, None, 15, 7])
        >>> binary_tree_vertical_order_traversal(root)
        [[9], [3, 15], [20], [7]]
    """
    if not root:
        return []
    
    column_map = defaultdict(list)
    queue = deque([(root, 0)])  # (node, column_index)
    min_col = max_col = 0
    
    while queue:
        node, col = queue.popleft()
        column_map[col].append(node.val)
        min_col = min(min_col, col)
        max_col = max(max_col, col)
        
        if node.left:
            queue.append((node.left, col - 1))
        if node.right:
            queue.append((node.right, col + 1))
    
    return [column_map[i] for i in range(min_col, max_col + 1)]


# 自动生成Solution类（无需手动编写）
Solution = create_solution(binary_tree_vertical_order_traversal)
