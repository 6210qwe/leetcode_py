# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 107
标题: Binary Tree Level Order Traversal II
难度: medium
链接: https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/
题目类型: 树、广度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
107. 二叉树的层序遍历 II - 给你二叉树的根节点 root ，返回其节点值 自底向上的层序遍历 。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历） 示例 1： [https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg] 输入：root = [3,9,20,null,null,15,7] 输出：[[15,7],[9,20],[3]] 示例 2： 输入：root = [1] 输出：[[1]] 示例 3： 输入：root = [] 输出：[] 提示： * 树中节点数目在范围 [0, 2000] 内 * -1000 <= Node.val <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用队列进行BFS，最后反转结果列表

算法步骤:
1. 如果根节点为空，返回空列表
2. 使用队列进行BFS层序遍历
3. 将每层的节点值存储在一个列表中
4. 遍历完成后，反转结果列表

关键点:
- 与102题类似，只需最后反转结果
- 时间复杂度O(n)，空间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要访问每个节点一次
空间复杂度: O(n) - 队列最多存储一层的节点
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from collections import deque
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def binary_tree_level_order_traversal_ii(root: Optional[TreeNode]) -> List[List[int]]:
    """
    函数式接口 - 自底向上层序遍历
    
    实现思路:
    使用队列进行BFS层序遍历，最后反转结果列表。
    
    Args:
        root: 二叉树的根节点
        
    Returns:
        自底向上的层序遍历结果
        
    Example:
        >>> root = TreeNode.from_list([3, 9, 20, None, None, 15, 7])
        >>> binary_tree_level_order_traversal_ii(root)
        [[15, 7], [9, 20], [3]]
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    result.reverse()
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(binary_tree_level_order_traversal_ii)
