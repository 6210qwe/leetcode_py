# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 450
标题: Delete Node in a BST
难度: medium
链接: https://leetcode.cn/problems/delete-node-in-a-bst/
题目类型: 树、二叉搜索树、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
450. 删除二叉搜索树中的节点 - 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。 一般来说，删除节点可分为两个步骤： 1. 首先找到需要删除的节点； 2. 如果找到了，删除它。 示例 1: [https://assets.leetcode.com/uploads/2020/09/04/del_node_1.jpg] 输入：root = [5,3,6,2,4,null,7], key = 3 输出：[5,4,6,2,null,null,7] 解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。 一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。 另一个正确答案是 [5,2,6,null,4,null,7]。 [https://assets.leetcode.com/uploads/2020/09/04/del_node_supp.jpg] 示例 2: 输入: root = [5,3,6,2,4,null,7], key = 0 输出: [5,3,6,2,4,null,7] 解释: 二叉树不包含值为 0 的节点 示例 3: 输入: root = [], key = 0 输出: [] 提示: * 节点数的范围 [0, 104]. * -105 <= Node.val <= 105 * 节点值唯一 * root 是合法的二叉搜索树 * -105 <= key <= 105 进阶： 要求算法时间复杂度为 O(h)，h 为树的高度。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 递归删除BST节点，分三种情况处理

算法步骤:
1. 如果节点为空，返回None
2. 如果key小于当前节点值，递归删除左子树
3. 如果key大于当前节点值，递归删除右子树
4. 如果key等于当前节点值：
   - 如果节点没有左子树，返回右子树
   - 如果节点没有右子树，返回左子树
   - 如果节点有左右子树，找到右子树的最小值节点替换当前节点

关键点:
- 保持BST性质
- 时间复杂度O(h)，h为树高
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(h) - h为树的高度，最坏情况O(n)
空间复杂度: O(h) - 递归栈空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def delete_node_in_a_bst(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    """
    函数式接口 - 删除二叉搜索树中的节点
    
    实现思路:
    递归删除BST节点，分三种情况：无子节点、一个子节点、两个子节点。
    
    Args:
        root: 二叉搜索树根节点
        key: 要删除的节点值
        
    Returns:
        删除后的BST根节点
        
    Example:
        >>> root = TreeNode(5)
        >>> root.left = TreeNode(3)
        >>> root.right = TreeNode(6)
        >>> result = delete_node_in_a_bst(root, 3)
    """
    if not root:
        return None
    
    if key < root.val:
        root.left = delete_node_in_a_bst(root.left, key)
    elif key > root.val:
        root.right = delete_node_in_a_bst(root.right, key)
    else:
        # 找到要删除的节点
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        
        # 有两个子节点，找到右子树的最小值节点
        min_node = root.right
        while min_node.left:
            min_node = min_node.left
        
        # 用最小值替换当前节点值，然后删除右子树中的最小值节点
        root.val = min_node.val
        root.right = delete_node_in_a_bst(root.right, min_node.val)
    
    return root


# 自动生成Solution类（无需手动编写）
Solution = create_solution(delete_node_in_a_bst)
