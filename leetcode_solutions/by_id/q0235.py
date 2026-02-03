# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 235
标题: Lowest Common Ancestor of a Binary Search Tree
难度: medium
链接: https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/
题目类型: 树、深度优先搜索、二叉搜索树、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
235. 二叉搜索树的最近公共祖先 - 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。 百度百科 [https://baike.baidu.com/item/%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88/8918834?fr=aladdin]中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。” 例如，给定如下二叉搜索树: root = [6,2,8,0,4,7,9,null,null,3,5] [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/14/binarysearchtree_improved.png] 示例 1: 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8 输出: 6 解释: 节点 2 和节点 8 的最近公共祖先是 6。 示例 2: 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4 输出: 2 解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。 说明: * 所有节点的值都是唯一的。 * p、q 为不同节点且均存在于给定的二叉搜索树中。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 利用BST的性质，如果p和q的值都小于当前节点，在左子树；都大于当前节点，在右子树；否则当前节点就是LCA

算法步骤:
1. 从根节点开始遍历
2. 如果p和q的值都小于当前节点，递归左子树
3. 如果p和q的值都大于当前节点，递归右子树
4. 否则当前节点就是LCA

关键点:
- 利用BST的排序性质
- 时间复杂度O(h)，空间复杂度O(1)（迭代）或O(h)（递归）
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(h) - h为树的高度
空间复杂度: O(1) - 迭代实现只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def lowest_common_ancestor_of_a_binary_search_tree(root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    函数式接口 - 二叉搜索树的最近公共祖先
    
    实现思路:
    利用BST的性质，如果p和q的值都小于当前节点，在左子树；都大于当前节点，在右子树；否则当前节点就是LCA。
    
    Args:
        root: 二叉搜索树的根节点
        p: 节点p
        q: 节点q
        
    Returns:
        最近公共祖先节点
        
    Example:
        >>> root = TreeNode.from_list([6,2,8,0,4,7,9,None,None,3,5])
        >>> p = TreeNode(2)
        >>> q = TreeNode(8)
        >>> lowest_common_ancestor_of_a_binary_search_tree(root, p, q).val
        6
    """
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
    return None


# 自动生成Solution类（无需手动编写）
Solution = create_solution(lowest_common_ancestor_of_a_binary_search_tree)
