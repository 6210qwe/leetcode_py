# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1248
标题: Binary Tree Coloring Game
难度: medium
链接: https://leetcode.cn/problems/binary-tree-coloring-game/
题目类型: 树、深度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1145. 二叉树着色游戏 - 有两位极客玩家参与了一场「二叉树着色」的游戏。游戏中，给出二叉树的根节点 root，树上总共有 n 个节点，且 n 为奇数，其中每个节点上的值从 1 到 n 各不相同。 最开始时： * 「一号」玩家从 [1, n] 中取一个值 x（1 <= x <= n）； * 「二号」玩家也从 [1, n] 中取一个值 y（1 <= y <= n）且 y != x。 「一号」玩家给值为 x 的节点染上红色，而「二号」玩家给值为 y 的节点染上蓝色。 之后两位玩家轮流进行操作，「一号」玩家先手。每一回合，玩家选择一个被他染过色的节点，将所选节点一个 未着色 的邻节点（即左右子节点、或父节点）进行染色（「一号」玩家染红色，「二号」玩家染蓝色）。 如果（且仅在此种情况下）当前玩家无法找到这样的节点来染色时，其回合就会被跳过。 若两个玩家都没有可以染色的节点时，游戏结束。着色节点最多的那位玩家获得胜利 ✌️。 现在，假设你是「二号」玩家，根据所给出的输入，假如存在一个 y 值可以确保你赢得这场游戏，则返回 true ；若无法获胜，就请返回 false 。 示例 1 ： [https://assets.leetcode.com/uploads/2019/08/01/1480-binary-tree-coloring-game.png] 输入：root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3 输出：true 解释：第二个玩家可以选择值为 2 的节点。 示例 2 ： 输入：root = [1,2,3], n = 3, x = 1 输出：false 提示： * 树中节点数目为 n * 1 <= x <= n <= 100 * n 是奇数 * 1 <= Node.val <= n * 树中所有值 互不相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 计算以 x 为根的子树的节点数，以及 x 的左子树和右子树的节点数。如果 x 的左子树或右子树的节点数大于 n // 2，则二号玩家可以通过选择 x 的父节点获胜。否则，二号玩家无法获胜。

算法步骤:
1. 找到值为 x 的节点。
2. 计算 x 的左子树和右子树的节点数。
3. 检查 x 的左子树或右子树的节点数是否大于 n // 2。
4. 如果是，则二号玩家可以通过选择 x 的父节点获胜；否则，二号玩家无法获胜。

关键点:
- 使用深度优先搜索 (DFS) 计算子树的节点数。
- 通过比较子树的节点数来判断二号玩家是否能获胜。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。我们需要遍历整个树来计算节点数。
空间复杂度: O(h)，其中 h 是树的高度。递归调用栈的空间复杂度取决于树的高度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def btree_game_winning_move(root: Optional[TreeNode], n: int, x: int) -> bool:
    def count_nodes(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + count_nodes(node.left) + count_nodes(node.right)

    def find_node(node: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not node:
            return None
        if node.val == target:
            return node
        left_result = find_node(node.left, target)
        if left_result:
            return left_result
        return find_node(node.right, target)

    # 找到值为 x 的节点
    x_node = find_node(root, x)
    if not x_node:
        return False

    # 计算 x 的左子树和右子树的节点数
    left_count = count_nodes(x_node.left)
    right_count = count_nodes(x_node.right)

    # 检查 x 的左子树或右子树的节点数是否大于 n // 2
    if left_count > n // 2 or right_count > n // 2:
        return True

    # 检查 x 的父节点是否能获胜
    parent_count = n - (left_count + right_count + 1)
    return parent_count > n // 2


Solution = create_solution(btree_game_winning_move)