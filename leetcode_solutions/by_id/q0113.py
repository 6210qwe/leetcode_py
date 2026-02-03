# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 113
标题: Path Sum II
难度: medium
链接: https://leetcode.cn/problems/path-sum-ii/
题目类型: 树、深度优先搜索、回溯、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
113. 路径总和 II - 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。 叶子节点 是指没有子节点的节点。 示例 1： [https://assets.leetcode.com/uploads/2021/01/18/pathsumii1.jpg] 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22 输出：[[5,4,11,2],[5,8,4,5]] 示例 2： [https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg] 输入：root = [1,2,3], targetSum = 5 输出：[] 示例 3： 输入：root = [1,2], targetSum = 0 输出：[] 提示： * 树中节点总数在范围 [0, 5000] 内 * -1000 <= Node.val <= 1000 * -1000 <= targetSum <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用回溯法收集所有满足条件的路径

算法步骤:
1. 定义回溯函数，维护当前路径和剩余和
2. 如果当前节点是叶子节点且剩余和为0，将路径加入结果
3. 递归遍历左子树和右子树
4. 回溯时移除当前节点

关键点:
- 使用回溯收集所有路径
- 时间复杂度O(n^2)，空间复杂度O(h)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2) - 需要遍历所有节点，每个路径最多n个节点
空间复杂度: O(h) - 递归栈深度和路径存储
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def path_sum_ii(root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    """
    函数式接口 - 找出所有路径和等于targetSum的路径
    
    实现思路:
    使用回溯法收集所有从根到叶子且路径和等于targetSum的路径。
    
    Args:
        root: 二叉树的根节点
        targetSum: 目标和
        
    Returns:
        所有满足条件的路径列表
        
    Example:
        >>> root = TreeNode.from_list([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
        >>> path_sum_ii(root, 22)
        [[5, 4, 11, 2], [5, 8, 4, 5]]
    """
    result = []
    path = []
    
    def backtrack(node: Optional[TreeNode], remaining: int):
        if not node:
            return
        
        path.append(node.val)
        remaining -= node.val
        
        if not node.left and not node.right and remaining == 0:
            result.append(path[:])
        else:
            backtrack(node.left, remaining)
            backtrack(node.right, remaining)
        
        path.pop()
    
    backtrack(root, targetSum)
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(path_sum_ii)
