# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100347
标题: 寻找二叉树的最近公共祖先
难度: easy
链接: https://leetcode.cn/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 194. 二叉树的最近公共祖先 - 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。 百度百科 [https://baike.baidu.com/item/%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88/8918834?fr=aladdin]中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。” 例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4] [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/15/binarytree.png] 示例 1： 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1 输出：3 解释：节点 5 和节点 1 的最近公共祖先是节点 3。 示例 2： 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4 输出：5 解释：节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。 说明： * 所有节点的值都是唯一的。 * p、q 为不同节点且均存在于给定的二叉树中。 注意：本题与主站 236 题相同：https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/ [https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用递归进行深度优先搜索 (DFS) 来查找最近公共祖先。

算法步骤:
1. 如果当前节点为空，返回 None。
2. 如果当前节点是 p 或 q，返回当前节点。
3. 递归查找左子树和右子树。
4. 如果左子树和右子树都找到了 p 或 q，返回当前节点。
5. 否则，返回找到的那个节点。

关键点:
- 递归调用时，如果左右子树都找到了 p 或 q，则当前节点就是最近公共祖先。
- 如果只有一个子树找到了 p 或 q，则返回找到的那个节点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是二叉树的节点数，因为每个节点最多访问一次。
空间复杂度: O(h)，其中 h 是二叉树的高度，这是由于递归调用栈的深度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def lowest_common_ancestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    """
    函数式接口 - 寻找二叉树的最近公共祖先
    """
    if not root:
        return None
    
    if root == p or root == q:
        return root
    
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    if left and right:
        return root
    else:
        return left if left else right


Solution = create_solution(lowest_common_ancestor)