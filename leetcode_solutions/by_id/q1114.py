# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1114
标题: Binary Search Tree to Greater Sum Tree
难度: medium
链接: https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree/
题目类型: 树、深度优先搜索、二叉搜索树、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1038. 从二叉搜索树到更大和树 - 给定一个二叉搜索树 root (BST)，请将它的每个节点的值替换成树中大于或者等于该节点值的所有节点值之和。 提醒一下， 二叉搜索树 满足下列约束条件： * 节点的左子树仅包含键 小于 节点键的节点。 * 节点的右子树仅包含键 大于 节点键的节点。 * 左右子树也必须是二叉搜索树。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/05/03/tree.png] 输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8] 输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8] 示例 2： 输入：root = [0,null,1] 输出：[1,null,1] 提示： * 树中的节点数在 [1, 100] 范围内。 * 0 <= Node.val <= 100 * 树中的所有值均 不重复 。 注意：该题目与 538: https://leetcode.cn/problems/convert-bst-to-greater-tree/ [https://leetcode.cn/problems/convert-bst-to-greater-tree/]相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用反向中序遍历（右-根-左）来累加节点值。

算法步骤:
1. 初始化一个累加器 `total` 为 0。
2. 从根节点开始进行反向中序遍历：
   - 递归遍历右子树。
   - 更新当前节点的值为当前节点值加上累加器 `total` 的值。
   - 更新累加器 `total` 为当前节点的新值。
   - 递归遍历左子树。
3. 返回根节点。

关键点:
- 反向中序遍历确保了我们先处理较大的节点值，从而可以正确累加。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 其中 n 是树中节点的数量。每个节点访问一次。
空间复杂度: O(h) - 其中 h 是树的高度。递归调用栈的深度最多为树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def bst_to_greater_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    将二叉搜索树转换为更大和树
    """
    total = 0

    def reverse_inorder(node: Optional[TreeNode]):
        nonlocal total
        if node is None:
            return
        # 递归遍历右子树
        reverse_inorder(node.right)
        # 更新当前节点的值
        node.val += total
        # 更新累加器
        total = node.val
        # 递归遍历左子树
        reverse_inorder(node.left)

    reverse_inorder(root)
    return root


Solution = create_solution(bst_to_greater_tree)