# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 257
标题: Binary Tree Paths
难度: easy
链接: https://leetcode.cn/problems/binary-tree-paths/
题目类型: 树、深度优先搜索、字符串、回溯、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
257. 二叉树的所有路径 - 给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。 叶子节点 是指没有子节点的节点。 示例 1： [https://assets.leetcode.com/uploads/2021/03/12/paths-tree.jpg] 输入：root = [1,2,3,null,5] 输出：["1->2->5","1->3"] 示例 2： 输入：root = [1] 输出：["1"] 提示： * 树中节点的数目在范围 [1, 100] 内 * -100 <= Node.val <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: DFS遍历，记录路径

算法步骤:
1. 使用DFS遍历二叉树
2. 到达叶子节点时，将路径加入结果
3. 回溯时移除当前节点

关键点:
- DFS+回溯
- 时间复杂度O(n)
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


def binary_tree_paths(root: Optional[TreeNode]) -> List[str]:
    """
    函数式接口 - 二叉树的所有路径
    
    实现思路:
    DFS遍历，记录从根到叶子的所有路径。
    
    Args:
        root: 二叉树根节点
        
    Returns:
        所有路径字符串数组
        
    Example:
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2)
        >>> root.right = TreeNode(3)
        >>> binary_tree_paths(root)
        ['1->2', '1->3']
    """
    result = []
    
    def dfs(node: Optional[TreeNode], path: List[str]):
        """DFS遍历"""
        if not node:
            return
        
        path.append(str(node.val))
        
        if not node.left and not node.right:
            result.append('->'.join(path))
        else:
            dfs(node.left, path)
            dfs(node.right, path)
        
        path.pop()
    
    dfs(root, [])
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(binary_tree_paths)
