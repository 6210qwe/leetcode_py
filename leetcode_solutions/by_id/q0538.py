# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 538
标题: Convert BST to Greater Tree
难度: medium
链接: https://leetcode.cn/problems/convert-bst-to-greater-tree/
题目类型: 树、深度优先搜索、二叉搜索树、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
538. 把二叉搜索树转换为累加树 - 给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。 提醒一下，二叉搜索树满足下列约束条件： * 节点的左子树仅包含键 小于 节点键的节点。 * 节点的右子树仅包含键 大于 节点键的节点。 * 左右子树也必须是二叉搜索树。 注意：本题和 1038: https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree/ [https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree/] 相同 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/05/03/tree.png] 输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8] 输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8] 示例 2： 输入：root = [0,null,1] 输出：[1,null,1] 示例 3： 输入：root = [1,0,2] 输出：[3,3,2] 示例 4： 输入：root = [3,2,4,1] 输出：[7,9,4,10] 提示： * 树中的节点数介于 0 和 104 之间。 * 每个节点的值介于 -104 和 104 之间。 * 树中的所有值 互不相同 。 * 给定的树为二叉搜索树。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用反向中序遍历（右-根-左）来累加节点值。

算法步骤:
1. 初始化一个全局变量 `total` 用于累加节点值。
2. 从右子树开始进行反向中序遍历。
3. 在访问每个节点时，更新节点值为当前节点值加上 `total`，并更新 `total` 为当前节点的新值。
4. 递归处理左子树。

关键点:
- 反向中序遍历确保了我们先访问较大的节点，再访问较小的节点。
- 使用全局变量 `total` 来累加节点值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点只被访问一次。
空间复杂度: O(h)，其中 h 是树的高度。递归调用栈的深度取决于树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total = 0
        self._reverse_inorder_traversal(root)
        return root
    
    def _reverse_inorder_traversal(self, node: Optional[TreeNode]):
        if not node:
            return
        # 先访问右子树
        self._reverse_inorder_traversal(node.right)
        # 更新当前节点值
        self.total += node.val
        node.val = self.total
        # 再访问左子树
        self._reverse_inorder_traversal(node.left)

Solution = create_solution(Solution)