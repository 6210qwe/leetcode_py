# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1475
标题: Maximum Sum BST in Binary Tree
难度: hard
链接: https://leetcode.cn/problems/maximum-sum-bst-in-binary-tree/
题目类型: 树、深度优先搜索、二叉搜索树、动态规划、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1373. 二叉搜索子树的最大键值和 - 给你一棵以 root 为根的 二叉树 ，请你返回 任意 二叉搜索子树的最大键值和。 二叉搜索树的定义如下： * 任意节点的左子树中的键值都 小于 此节点的键值。 * 任意节点的右子树中的键值都 大于 此节点的键值。 * 任意节点的左子树和右子树都是二叉搜索树。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/03/07/sample_1_1709.png] 输入：root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6] 输出：20 解释：键值为 3 的子树是和最大的二叉搜索树。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/03/07/sample_2_1709.png] 输入：root = [4,3,null,1,2] 输出：2 解释：键值为 2 的单节点子树是和最大的二叉搜索树。 示例 3： 输入：root = [-4,-2,-5] 输出：0 解释：所有节点键值都为负数，和最大的二叉搜索树为空。 示例 4： 输入：root = [2,1,3] 输出：6 示例 5： 输入：root = [5,4,8,3,null,6,3] 输出：7 提示： * 每棵树有 1 到 40000 个节点。 * 每个节点的键值在 [-4 * 10^4 , 4 * 10^4] 之间。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）遍历树，同时维护每个子树的状态（是否为BST，最小值，最大值，和）。通过递归的方式，从叶子节点向上计算每个节点的子树是否为BST，并更新最大和。

算法步骤:
1. 定义一个辅助函数 `dfs`，用于递归地处理每个节点。
2. 对于每个节点，递归处理其左子树和右子树，获取它们的状态。
3. 如果当前节点的左子树和右子树都是BST，并且当前节点的值大于左子树的最大值且小于右子树的最小值，则当前节点也是BST的一部分。
4. 更新当前节点的子树状态，并计算当前子树的和。
5. 递归结束后，返回最大和。

关键点:
- 使用四元组 (is_bst, min_val, max_val, sum) 来表示每个子树的状态。
- 递归过程中，自底向上地更新状态。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点只会被访问一次。
空间复杂度: O(h)，其中 h 是树的高度。递归调用栈的深度最多为树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0

        def dfs(node: Optional[TreeNode]) -> (bool, int, int, int):
            if not node:
                return True, float('inf'), float('-inf'), 0

            left_is_bst, left_min, left_max, left_sum = dfs(node.left)
            right_is_bst, right_min, right_max, right_sum = dfs(node.right)

            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                current_sum = left_sum + right_sum + node.val
                self.max_sum = max(self.max_sum, current_sum)
                return True, min(left_min, node.val), max(right_max, node.val), current_sum
            else:
                return False, float('inf'), float('-inf'), 0

        dfs(root)
        return self.max_sum


Solution = create_solution(Solution)