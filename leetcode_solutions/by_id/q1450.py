# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1450
标题: Delete Leaves With a Given Value
难度: medium
链接: https://leetcode.cn/problems/delete-leaves-with-a-given-value/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1325. 删除给定值的叶子节点 - 给你一棵以 root 为根的二叉树和一个整数 target ，请你删除所有值为 target 的 叶子节点 。 注意，一旦删除值为 target 的叶子节点，它的父节点就可能变成叶子节点；如果新叶子节点的值恰好也是 target ，那么这个节点也应该被删除。 也就是说，你需要重复此过程直到不能继续删除。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/16/sample_1_1684.png] 输入：root = [1,2,3,2,null,2,4], target = 2 输出：[1,null,3,null,4] 解释： 上面左边的图中，绿色节点为叶子节点，且它们的值与 target 相同（同为 2 ），它们会被删除，得到中间的图。 有一个新的节点变成了叶子节点且它的值与 target 相同，所以将再次进行删除，从而得到最右边的图。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/16/sample_2_1684.png] 输入：root = [1,3,3,3,2], target = 3 输出：[1,3,null,null,2] 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/16/sample_3_1684.png] 输入：root = [1,2,null,2,null,2], target = 2 输出：[1] 解释：每一步都删除一个绿色的叶子节点（值为 2）。 提示： * 树中节点数量的范围是 [1, 3000]。 * 1 <= Node.val, target <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用递归深度优先搜索 (DFS) 来遍历树，并在回溯时检查当前节点是否为叶子节点且值为目标值，如果是则删除该节点。

算法步骤:
1. 定义一个递归函数 `dfs`，用于遍历树。
2. 在 `dfs` 函数中，首先递归处理左子树和右子树。
3. 回溯时，检查当前节点是否为叶子节点且值为目标值，如果是则返回 `None` 表示删除该节点。
4. 否则返回当前节点。

关键点:
- 递归处理子树时，需要更新当前节点的左右子节点。
- 在回溯时检查并删除目标叶子节点。
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


def remove_leaf_nodes(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    """
    删除给定值的叶子节点
    """
    if not root:
        return None

    # 递归处理左子树和右子树
    root.left = remove_leaf_nodes(root.left, target)
    root.right = remove_leaf_nodes(root.right, target)

    # 检查当前节点是否为叶子节点且值为目标值
    if root.left is None and root.right is None and root.val == target:
        return None

    return root


Solution = create_solution(remove_leaf_nodes)