# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 930
标题: All Possible Full Binary Trees
难度: medium
链接: https://leetcode.cn/problems/all-possible-full-binary-trees/
题目类型: 树、递归、记忆化搜索、动态规划、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
894. 所有可能的真二叉树 - 给你一个整数 n ，请你找出所有可能含 n 个节点的 真二叉树 ，并以列表形式返回。答案中每棵树的每个节点都必须符合 Node.val == 0 。 答案的每个元素都是一棵真二叉树的根节点。你可以按 任意顺序 返回最终的真二叉树列表。 真二叉树 是一类二叉树，树中每个节点恰好有 0 或 2 个子节点。 示例 1： [https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/22/fivetrees.png] 输入：n = 7 输出：[[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]] 示例 2： 输入：n = 3 输出：[[0,0,0]] 提示： * 1 <= n <= 20
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用递归和记忆化搜索来生成所有可能的真二叉树。

算法步骤:
1. 定义一个递归函数 `all_possible_FBT` 来生成所有可能的真二叉树。
2. 如果 n 为 1，返回一个只有一个节点的树。
3. 对于奇数 n，尝试将 n 分成两个部分，分别生成左子树和右子树。
4. 使用记忆化搜索来避免重复计算。

关键点:
- 只有当 n 为奇数时，才能生成真二叉树。
- 使用记忆化搜索来优化递归过程。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^n) - 每个节点都有两种选择（左子树或右子树），且递归深度为 n。
空间复杂度: O(n) - 递归调用栈的深度最多为 n。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def all_possible_FBT(N: int) -> List[Optional[TreeNode]]:
    if N % 2 == 0:
        return []
    
    memo = {}
    
    def helper(n):
        if n in memo:
            return memo[n]
        
        if n == 1:
            return [TreeNode(0)]
        
        result = []
        for i in range(1, n, 2):
            left_trees = helper(i)
            right_trees = helper(n - i - 1)
            
            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    result.append(root)
        
        memo[n] = result
        return result
    
    return helper(N)

Solution = create_solution(all_possible_FBT)