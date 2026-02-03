# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 102
标题: Binary Tree Level Order Traversal
难度: medium
链接: https://leetcode.cn/problems/binary-tree-level-order-traversal/
题目类型: 树、广度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
102. 二叉树的层序遍历 - 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。 示例 1： [https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg] 输入：root = [3,9,20,null,null,15,7] 输出：[[3],[9,20],[15,7]] 示例 2： 输入：root = [1] 输出：[[1]] 示例 3： 输入：root = [] 输出：[] 提示： * 树中节点数目在范围 [0, 2000] 内 * -1000 <= Node.val <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用队列进行广度优先搜索，逐层遍历

算法步骤:
1. 如果根节点为空，返回空列表
2. 使用队列存储当前层的所有节点
3. 对于每一层：
   - 记录当前层的节点数
   - 遍历当前层的所有节点，将值加入结果
   - 将下一层的节点加入队列
4. 重复直到队列为空

关键点:
- 使用队列实现BFS
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


def binary_tree_level_order_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    """
    函数式接口 - BFS层序遍历
    
    实现思路:
    使用队列进行广度优先搜索，逐层遍历二叉树，将每层的节点值存储在一个列表中。
    
    Args:
        root: 二叉树的根节点
        
    Returns:
        层序遍历的结果，每层一个列表
        
    Example:
        >>> root = TreeNode.from_list([3, 9, 20, None, None, 15, 7])
        >>> binary_tree_level_order_traversal(root)
        [[3], [9, 20], [15, 7]]
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
    
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(binary_tree_level_order_traversal)
