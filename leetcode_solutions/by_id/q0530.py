# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 530
标题: Minimum Absolute Difference in BST
难度: easy
链接: https://leetcode.cn/problems/minimum-absolute-difference-in-bst/
题目类型: 树、深度优先搜索、广度优先搜索、二叉搜索树、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
530. 二叉搜索树的最小绝对差 - 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。 差值是一个正数，其数值等于两值之差的绝对值。 示例 1： [https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg] 输入：root = [4,2,6,1,3] 输出：1 示例 2： [https://assets.leetcode.com/uploads/2021/02/05/bst2.jpg] 输入：root = [1,0,48,null,null,12,49] 输出：1 提示： * 树中节点的数目范围是 [2, 104] * 0 <= Node.val <= 105 注意：本题与 783 https://leetcode.cn/problems/minimum-distance-between-bst-nodes/ [https://leetcode.cn/problems/minimum-distance-between-bst-nodes/] 相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 利用二叉搜索树的中序遍历特性，中序遍历的结果是一个有序数组。在遍历过程中，我们可以逐个比较相邻节点的差值，找到最小的差值。

算法步骤:
1. 使用中序遍历（递归或迭代）遍历二叉搜索树。
2. 在遍历过程中，记录前一个节点的值，并计算当前节点与前一个节点的差值。
3. 更新最小差值。

关键点:
- 中序遍历二叉搜索树会得到一个有序序列。
- 通过比较相邻节点的差值，可以找到最小的绝对差值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点都被访问一次。
空间复杂度: O(h)，其中 h 是树的高度。递归调用栈的深度最多为树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_diff = float('inf')
        
        def inorder(node: Optional[TreeNode]):
            if not node:
                return
            
            inorder(node.left)
            
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            
            inorder(node.right)
        
        inorder(root)
        return self.min_diff

Solution = create_solution(Solution)