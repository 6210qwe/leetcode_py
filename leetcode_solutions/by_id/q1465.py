# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1465
标题: Maximum Product of Splitted Binary Tree
难度: medium
链接: https://leetcode.cn/problems/maximum-product-of-splitted-binary-tree/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1339. 分裂二叉树的最大乘积 - 给你一棵二叉树，它的根为 root 。请你删除 1 条边，使二叉树分裂成两棵子树，且它们子树和的乘积尽可能大。 由于答案可能会很大，请你将结果对 10^9 + 7 取模后再返回。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/02/sample_1_1699.png] 输入：root = [1,2,3,4,5,6] 输出：110 解释：删除红色的边，得到 2 棵子树，和分别为 11 和 10 。它们的乘积是 110 （11*10） 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/02/sample_2_1699.png] 输入：root = [1,null,2,3,4,null,null,5,6] 输出：90 解释：移除红色的边，得到 2 棵子树，和分别是 15 和 6 。它们的乘积为 90 （15*6） 示例 3： 输入：root = [2,3,9,10,7,8,6,5,4,11,1] 输出：1025 示例 4： 输入：root = [1,1] 输出：1 提示： * 每棵树最多有 50000 个节点，且至少有 2 个节点。 * 每个节点的值在 [1, 10000] 之间。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）计算每个子树的和，并记录所有可能的子树和。然后遍历这些子树和，找到最大的乘积。

算法步骤:
1. 使用 DFS 计算整棵树的总和。
2. 在 DFS 过程中，记录每个子树的和。
3. 遍历所有子树和，计算 (总和 - 子树和) * 子树和 的最大值。
4. 返回最大乘积并对 10^9 + 7 取模。

关键点:
- 使用 DFS 计算子树和并记录。
- 遍历所有子树和，找到最大乘积。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。我们需要遍历每个节点一次。
空间复杂度: O(n)，递归调用栈的空间复杂度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        self.total_sum = 0
        self.subtree_sums = []

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            current_sum = left_sum + right_sum + node.val
            self.subtree_sums.append(current_sum)
            return current_sum

        # 计算整棵树的总和
        self.total_sum = dfs(root)

        # 找到最大乘积
        max_product = 0
        for subtree_sum in self.subtree_sums:
            product = (self.total_sum - subtree_sum) * subtree_sum
            max_product = max(max_product, product)

        return max_product % MOD

Solution = create_solution(Solution)