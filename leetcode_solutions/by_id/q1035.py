# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1035
标题: Cousins in Binary Tree
难度: easy
链接: https://leetcode.cn/problems/cousins-in-binary-tree/
题目类型: 树、深度优先搜索、广度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
993. 二叉树的堂兄弟节点 - 在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。 如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。 我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。 只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/02/16/q1248-01.png] 输入：root = [1,2,3,4], x = 4, y = 3 输出：false 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/02/16/q1248-02.png] 输入：root = [1,2,3,null,4,null,5], x = 5, y = 4 输出：true 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/02/16/q1248-03.png] 输入：root = [1,2,3,null,4], x = 2, y = 3 输出：false 提示： * 二叉树的节点数介于 2 到 100 之间。 * 每个节点的值都是唯一的、范围为 1 到 100 的整数。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）遍历二叉树，记录每个节点的深度和父节点。检查 x 和 y 是否在同一深度且父节点不同。

算法步骤:
1. 初始化一个队列，将根节点加入队列，并设置其深度为 0，父节点为 None。
2. 使用一个字典来存储每个节点的深度和父节点。
3. 进行 BFS 遍历：
   - 从队列中取出一个节点。
   - 如果该节点的值等于 x 或 y，则记录其深度和父节点。
   - 将该节点的左右子节点加入队列，并设置其深度和父节点。
4. 检查 x 和 y 是否在同一深度且父节点不同。

关键点:
- 使用 BFS 遍历二叉树，确保在第一次遇到 x 和 y 时就能确定它们是否为堂兄弟节点。
- 使用字典记录每个节点的深度和父节点，方便后续比较。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是二叉树的节点数。因为每个节点只会被访问一次。
空间复杂度: O(n)，最坏情况下队列中会包含所有节点。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def is_cousins(root: Optional[TreeNode], x: int, y: int) -> bool:
    if not root:
        return False

    # 用于存储每个节点的深度和父节点
    node_info = {}
    queue = [(root, 0, None)]  # (node, depth, parent)

    while queue:
        node, depth, parent = queue.pop(0)
        if node.val == x or node.val == y:
            node_info[node.val] = (depth, parent)
        if len(node_info) == 2:
            break
        if node.left:
            queue.append((node.left, depth + 1, node))
        if node.right:
            queue.append((node.right, depth + 1, node))

    # 检查 x 和 y 是否在同一深度且父节点不同
    (x_depth, x_parent), (y_depth, y_parent) = node_info[x], node_info[y]
    return x_depth == y_depth and x_parent != y_parent

Solution = create_solution(is_cousins)