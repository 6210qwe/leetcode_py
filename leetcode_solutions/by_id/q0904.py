# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 904
标题: Leaf-Similar Trees
难度: easy
链接: https://leetcode.cn/problems/leaf-similar-trees/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
872. 叶子相似的树 - 请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。 [https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png] 举个例子，如上图所示，给定一棵叶值序列为 (6, 7, 4, 9, 8) 的树。 如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。 如果给定的两个根结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。 示例 1： [https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-1.jpg] 输入：root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8] 输出：true 示例 2： [https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-2.jpg] 输入：root1 = [1,2,3], root2 = [1,3,2] 输出：false 提示： * 给定的两棵树结点数在 [1, 200] 范围内 * 给定的两棵树上的值在 [0, 200] 范围内
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 获取两棵树的叶值序列，并比较这两个序列是否相同。

算法步骤:
1. 定义一个辅助函数 `get_leaf_values` 来获取树的叶值序列。
2. 对于每棵树，使用 `get_leaf_values` 获取其叶值序列。
3. 比较两个叶值序列是否相同。

关键点:
- 使用 DFS 遍历树，确保叶值序列是从左到右的顺序。
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

def get_leaf_values(root: Optional[TreeNode]) -> List[int]:
    """获取树的叶值序列"""
    if not root:
        return []
    if not root.left and not root.right:
        return [root.val]
    return get_leaf_values(root.left) + get_leaf_values(root.right)

def leaf_similar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    """
    判断两棵树是否叶相似
    """
    return get_leaf_values(root1) == get_leaf_values(root2)

Solution = create_solution(leaf_similar)