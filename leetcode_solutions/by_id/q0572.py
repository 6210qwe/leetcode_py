# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 572
标题: Subtree of Another Tree
难度: easy
链接: https://leetcode.cn/problems/subtree-of-another-tree/
题目类型: 树、深度优先搜索、二叉树、字符串匹配、哈希函数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
572. 另一棵树的子树 - 给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true ；否则，返回 false 。 二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。 示例 1： [https://pic.leetcode.cn/1724998676-cATjhe-image.png] 输入：root = [3,4,5,1,2], subRoot = [4,1,2] 输出：true 示例 2： [https://pic.leetcode.cn/1724998698-sEJWnq-image.png] 输入：root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2] 输出：false 提示： * root 树上的节点数量范围是 [1, 2000] * subRoot 树上的节点数量范围是 [1, 1000] * -104 <= root.val <= 104 * -104 <= subRoot.val <= 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用递归方法来检查子树是否相等。

算法步骤:
1. 定义一个辅助函数 `is_same_tree` 来检查两棵树是否完全相同。
2. 在主函数 `is_subtree` 中，递归地检查当前节点的子树是否与 `subRoot` 相同。
3. 如果当前节点的子树与 `subRoot` 相同，则返回 `True`。
4. 否则，递归地检查左子树和右子树。

关键点:
- 使用递归方法可以简化代码逻辑。
- 通过 `is_same_tree` 辅助函数来判断两棵树是否相同。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 是 root 树的节点数，n 是 subRoot 树的节点数。在最坏情况下，每个节点都需要与 subRoot 进行比较。
空间复杂度: O(h)，其中 h 是 root 树的高度。递归调用栈的深度最多为树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def is_same_tree(s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
    if not s and not t:
        return True
    if not s or not t:
        return False
    return s.val == t.val and is_same_tree(s.left, t.left) and is_same_tree(s.right, t.right)

def is_subtree(root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
    if not root:
        return False
    if is_same_tree(root, sub_root):
        return True
    return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)

Solution = create_solution(is_subtree)