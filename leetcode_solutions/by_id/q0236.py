# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 236
标题: Lowest Common Ancestor of a Binary Tree
难度: medium
链接: https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
236. 二叉树的最近公共祖先 - 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。 百度百科 [https://baike.baidu.com/item/%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88/8918834?fr=aladdin]中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。” 示例 1： [https://assets.leetcode.com/uploads/2018/12/14/binarytree.png] 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1 输出：3 解释：节点 5 和节点 1 的最近公共祖先是节点 3 。 示例 2： [https://assets.leetcode.com/uploads/2018/12/14/binarytree.png] 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4 输出：5 解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。 示例 3： 输入：root = [1,2], p = 1, q = 2 输出：1 提示： * 树中节点数目在范围 [2, 105] 内。 * -109 <= Node.val <= 109 * 所有 Node.val 互不相同 。 * p != q * p 和 q 均存在于给定的二叉树中。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 递归查找，如果当前节点是p或q，返回当前节点；否则递归左右子树，如果左右子树都找到，当前节点就是LCA

算法步骤:
1. 如果当前节点是None、p或q，返回当前节点
2. 递归查找左子树和右子树
3. 如果左右子树都返回非None，说明p和q分别在左右子树，当前节点是LCA
4. 否则返回非None的那一边

关键点:
- 递归查找，利用返回值判断
- 时间复杂度O(n)，空间复杂度O(h)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要访问每个节点一次
空间复杂度: O(h) - 递归栈深度，h为树的高度
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def lowest_common_ancestor_of_a_binary_tree(root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    函数式接口 - 二叉树的最近公共祖先
    
    实现思路:
    递归查找，如果当前节点是p或q，返回当前节点；否则递归左右子树，如果左右子树都找到，当前节点就是LCA。
    
    Args:
        root: 二叉树的根节点
        p: 节点p
        q: 节点q
        
    Returns:
        最近公共祖先节点
        
    Example:
        >>> root = TreeNode.from_list([3,5,1,6,2,0,8,None,None,7,4])
        >>> p = TreeNode(5)
        >>> q = TreeNode(1)
        >>> lowest_common_ancestor_of_a_binary_tree(root, p, q).val
        3
    """
    if not root or root == p or root == q:
        return root
    
    left = lowest_common_ancestor_of_a_binary_tree(root.left, p, q)
    right = lowest_common_ancestor_of_a_binary_tree(root.right, p, q)
    
    if left and right:
        return root
    
    return left if left else right


# 自动生成Solution类（无需手动编写）
Solution = create_solution(lowest_common_ancestor_of_a_binary_tree)
