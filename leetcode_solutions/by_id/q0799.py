# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 799
标题: Minimum Distance Between BST Nodes
难度: easy
链接: https://leetcode.cn/problems/minimum-distance-between-bst-nodes/
题目类型: 树、深度优先搜索、广度优先搜索、二叉搜索树、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
783. 二叉搜索树节点最小距离 - 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。 差值是一个正数，其数值等于两值之差的绝对值。 示例 1： [https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg] 输入：root = [4,2,6,1,3] 输出：1 示例 2： [https://assets.leetcode.com/uploads/2021/02/05/bst2.jpg] 输入：root = [1,0,48,null,null,12,49] 输出：1 提示： * 树中节点的数目范围是 [2, 100] * 0 <= Node.val <= 105 注意：本题与 530：https://leetcode.cn/problems/minimum-absolute-difference-in-bst/ [https://leetcode.cn/problems/minimum-absolute-difference-in-bst/] 相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 利用二叉搜索树的中序遍历特性，中序遍历会得到一个递增的序列，相邻节点的差值最小。

算法步骤:
1. 定义一个全局变量 `prev` 用于记录前一个节点。
2. 定义一个全局变量 `min_diff` 用于记录最小差值。
3. 进行中序遍历：
   - 递归遍历左子树。
   - 计算当前节点与前一个节点的差值，并更新 `min_diff`。
   - 更新 `prev` 为当前节点。
   - 递归遍历右子树。

关键点:
- 中序遍历保证了节点值的有序性。
- 通过记录前一个节点，可以方便地计算相邻节点的差值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量，因为每个节点都被访问一次。
空间复杂度: O(h)，其中 h 是树的高度，这是由于递归调用栈的深度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

prev: Optional[TreeNode] = None
min_diff: int = float('inf')

def min_distance_bst(root: Optional[TreeNode]) -> int:
    """
    函数式接口 - 返回二叉搜索树中任意两不同节点值之间的最小差值
    """
    global prev, min_diff

    def inorder_traversal(node: Optional[TreeNode]):
        nonlocal prev, min_diff
        if not node:
            return
        inorder_traversal(node.left)
        if prev:
            min_diff = min(min_diff, node.val - prev.val)
        prev = node
        inorder_traversal(node.right)

    inorder_traversal(root)
    return min_diff

Solution = create_solution(min_distance_bst)