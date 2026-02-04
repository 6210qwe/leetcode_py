# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1285
标题: Balance a Binary Search Tree
难度: medium
链接: https://leetcode.cn/problems/balance-a-binary-search-tree/
题目类型: 贪心、树、深度优先搜索、二叉搜索树、分治、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1382. 将二叉搜索树变平衡 - 给你一棵二叉搜索树，请你返回一棵 平衡后 的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。如果有多种构造方法，请你返回任意一种。 如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是 平衡的 。 示例 1： [https://assets.leetcode.com/uploads/2021/08/10/balance1-tree.jpg] 输入：root = [1,null,2,null,3,null,4,null,null] 输出：[2,1,3,null,null,null,4] 解释：这不是唯一的正确答案，[3,1,4,null,2,null,null] 也是一个可行的构造方案。 示例 2： [https://assets.leetcode.com/uploads/2021/08/10/balanced2-tree.jpg] 输入: root = [2,1,3] 输出: [2,1,3] 提示： * 树节点的数目在 [1, 104] 范围内。 * 1 <= Node.val <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用中序遍历将二叉搜索树转换为有序数组，然后通过递归构建平衡二叉搜索树。

算法步骤:
1. 中序遍历原二叉搜索树，得到一个有序数组。
2. 通过递归方式构建平衡二叉搜索树，每次选择中间元素作为根节点，左半部分作为左子树，右半部分作为右子树。

关键点:
- 中序遍历确保了节点值的有序性。
- 递归构建时，选择中间元素作为根节点，保证了树的高度平衡。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是节点数。中序遍历和构建平衡二叉搜索树的时间复杂度均为 O(n)。
空间复杂度: O(n)，中序遍历需要 O(n) 的空间存储节点值，递归调用栈的空间复杂度也为 O(log n)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def balance_bst(root: TreeNode) -> TreeNode:
    """
    将二叉搜索树变平衡
    """
    # 中序遍历，将节点值存入列表
    def inorder_traversal(node: TreeNode, values: List[int]):
        if node is None:
            return
        inorder_traversal(node.left, values)
        values.append(node.val)
        inorder_traversal(node.right, values)

    # 通过有序数组构建平衡二叉搜索树
    def build_balanced_bst(values: List[int], start: int, end: int) -> Optional[TreeNode]:
        if start > end:
            return None
        mid = (start + end) // 2
        root = TreeNode(values[mid])
        root.left = build_balanced_bst(values, start, mid - 1)
        root.right = build_balanced_bst(values, mid + 1, end)
        return root

    values = []
    inorder_traversal(root, values)
    return build_balanced_bst(values, 0, len(values) - 1)

Solution = create_solution(balance_bst)