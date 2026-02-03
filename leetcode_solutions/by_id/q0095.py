# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 95
标题: Unique Binary Search Trees II
难度: medium
链接: https://leetcode.cn/problems/unique-binary-search-trees-ii/
题目类型: 树、二叉搜索树、动态规划、回溯、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
95. 不同的二叉搜索树 II - 给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。 示例 1： [https://assets.leetcode.com/uploads/2021/01/18/uniquebstn3.jpg] 输入：n = 3 输出：[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]] 示例 2： 输入：n = 1 输出：[[1]] 提示： * 1 <= n <= 8
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 递归构建，对于每个根节点，递归构建左右子树

算法步骤:
1. 递归函数generate(start, end)生成[start, end]范围内的所有BST
2. 对于每个可能的根节点i（start到end）：
   - 递归生成左子树：left_trees = generate(start, i-1)
   - 递归生成右子树：right_trees = generate(i+1, end)
   - 组合所有左右子树，创建以i为根节点的BST
3. 返回所有可能的BST列表

关键点:
- 使用递归分治思想
- 对于每个根节点，组合所有可能的左右子树
- 时间复杂度O(4^n/√n)，空间复杂度O(4^n/√n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(4^n/√n) - 需要生成所有BST
空间复杂度: O(4^n/√n) - 存储所有BST
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def generate_trees(n: int) -> List[Optional[TreeNode]]:
    """
    函数式接口 - 递归构建
    
    实现思路:
    使用递归为每个可能的根节点生成所有可能的左右子树，然后组合成BST。
    
    Args:
        n: 节点数量（节点值从1到n）
        
    Returns:
        所有由n个节点组成的不同二叉搜索树列表
        
    Example:
        >>> trees = generate_trees(3)
        >>> len(trees)
        5
    """
    def generate(start: int, end: int) -> List[Optional[TreeNode]]:
        """生成[start, end]范围内的所有BST"""
        if start > end:
            return [None]
        
        result = []
        for i in range(start, end + 1):
            # 生成所有可能的左子树
            left_trees = generate(start, i - 1)
            # 生成所有可能的右子树
            right_trees = generate(i + 1, end)
            
            # 组合所有左右子树
            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    result.append(root)
        
        return result
    
    return generate(1, n)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(generate_trees)
