# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1218
标题: Lowest Common Ancestor of Deepest Leaves
难度: medium
链接: https://leetcode.cn/problems/lowest-common-ancestor-of-deepest-leaves/
题目类型: 树、深度优先搜索、广度优先搜索、哈希表、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1123. 最深叶节点的最近公共祖先 - 给你一个有根节点 root 的二叉树，返回它 最深的叶节点的最近公共祖先 。 回想一下： * 叶节点 是二叉树中没有子节点的节点 * 树的根节点的 深度 为 0，如果某一节点的深度为 d，那它的子节点的深度就是 d+1 * 如果我们假定 A 是一组节点 S 的 最近公共祖先，S 中的每个节点都在以 A 为根节点的子树中，且 A 的深度达到此条件下可能的最大值。 示例 1： [https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/01/sketch1.png] 输入：root = [3,5,1,6,2,0,8,null,null,7,4] 输出：[2,7,4] 解释：我们返回值为 2 的节点，在图中用黄色标记。 在图中用蓝色标记的是树的最深的节点。 注意，节点 6、0 和 8 也是叶节点，但是它们的深度是 2 ，而节点 7 和 4 的深度是 3 。 示例 2： 输入：root = [1] 输出：[1] 解释：根节点是树中最深的节点，它是它本身的最近公共祖先。 示例 3： 输入：root = [0,1,3,null,2] 输出：[2] 解释：树中最深的叶节点是 2 ，最近公共祖先是它自己。 提示： * 树中的节点数将在 [1, 1000] 的范围内。 * 0 <= Node.val <= 1000 * 每个节点的值都是 独一无二 的。 注意：本题与力扣 865 重复：https://leetcode.cn/problems/smallest-subtree-with-all-the-deepest-nodes/ [https://leetcode.cn/problems/smallest-subtree-with-all-the-deepest-nodes/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来找到最深的叶节点，并记录它们的最近公共祖先。

算法步骤:
1. 定义一个辅助函数 `dfs`，该函数返回当前节点的深度和最深叶节点的最近公共祖先。
2. 在 `dfs` 函数中，递归地计算左子树和右子树的深度及最近公共祖先。
3. 如果左右子树的深度相同，则当前节点即为最近公共祖先。
4. 返回当前节点的深度和最近公共祖先。

关键点:
- 使用 DFS 一次遍历即可找到最深叶节点及其最近公共祖先。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点只访问一次。
空间复杂度: O(h)，其中 h 是树的高度。递归调用栈的深度最多为树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def lca_deepest_leaves(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    函数式接口 - 找到最深叶节点的最近公共祖先
    """
    def dfs(node: Optional[TreeNode]) -> (int, Optional[TreeNode]):
        if not node:
            return 0, None
        
        left_depth, left_lca = dfs(node.left)
        right_depth, right_lca = dfs(node.right)
        
        if left_depth == right_depth:
            return left_depth + 1, node
        elif left_depth > right_depth:
            return left_depth + 1, left_lca
        else:
            return right_depth + 1, right_lca
    
    _, lca = dfs(root)
    return lca


Solution = create_solution(lca_deepest_leaves)