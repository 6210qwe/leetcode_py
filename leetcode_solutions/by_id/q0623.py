# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 623
标题: Add One Row to Tree
难度: medium
链接: https://leetcode.cn/problems/add-one-row-to-tree/
题目类型: 树、深度优先搜索、广度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
623. 在二叉树中增加一行 - 给定一个二叉树的根 root 和两个整数 val 和 depth ，在给定的深度 depth 处添加一个值为 val 的节点行。 注意，根节点 root 位于深度 1 。 加法规则如下: * 给定整数 depth，对于深度为 depth - 1 的每个非空树节点 cur ，创建两个值为 val 的树节点作为 cur 的左子树根和右子树根。 * cur 原来的左子树应该是新的左子树根的左子树。 * cur 原来的右子树应该是新的右子树根的右子树。 * 如果 depth == 1 意味着 depth - 1 根本没有深度，那么创建一个树节点，值 val 作为整个原始树的新根，而原始树就是新根的左子树。 示例 1: [https://assets.leetcode.com/uploads/2021/03/15/addrow-tree.jpg] 输入: root = [4,2,6,3,1,5], val = 1, depth = 2 输出: [4,1,1,2,null,null,6,3,1,5] 示例 2: [https://assets.leetcode.com/uploads/2021/03/11/add2-tree.jpg] 输入: root = [4,2,null,3,1], val = 1, depth = 3 输出: [4,2,null,1,1,3,null,null,1] 提示: * 节点数在 [1, 104] 范围内 * 树的深度在 [1, 104]范围内 * -100 <= Node.val <= 100 * -105 <= val <= 105 * 1 <= depth <= the depth of tree + 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）遍历树，在指定深度插入新节点。

算法步骤:
1. 如果 depth 为 1，则创建一个新节点作为新的根节点，并将原树作为其左子树。
2. 否则，使用 DFS 遍历树，直到达到 depth - 1 的深度。
3. 对于每个到达 depth - 1 的节点，创建两个新节点作为其左子树和右子树的根节点，并将原来的左子树和右子树分别作为新节点的左子树和右子树。

关键点:
- 使用递归实现 DFS。
- 在指定深度插入新节点时，需要处理好原有子树的连接。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。因为我们需要遍历每个节点一次。
空间复杂度: O(h)，其中 h 是树的高度。这是由于递归调用栈的空间消耗。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def add_one_row(root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
    """
    在二叉树中增加一行
    """
    if depth == 1:
        new_root = TreeNode(val)
        new_root.left = root
        return new_root

    def dfs(node: Optional[TreeNode], current_depth: int):
        if not node:
            return
        if current_depth == depth - 1:
            left_child = TreeNode(val)
            right_child = TreeNode(val)
            left_child.left = node.left
            right_child.right = node.right
            node.left = left_child
            node.right = right_child
        else:
            dfs(node.left, current_depth + 1)
            dfs(node.right, current_depth + 1)

    dfs(root, 1)
    return root


Solution = create_solution(add_one_row)