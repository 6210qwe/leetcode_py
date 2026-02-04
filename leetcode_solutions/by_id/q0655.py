# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 655
标题: Print Binary Tree
难度: medium
链接: https://leetcode.cn/problems/print-binary-tree/
题目类型: 树、深度优先搜索、广度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
655. 输出二叉树 - 给你一棵二叉树的根节点 root ，请你构造一个下标从 0 开始、大小为 m x n 的字符串矩阵 res ，用以表示树的 格式化布局 。构造此格式化布局矩阵需要遵循以下规则： * 树的 高度 为 height ，矩阵的行数 m 应该等于 height + 1 。 * 矩阵的列数 n 应该等于 2height+1 - 1 。 * 根节点 需要放置在 顶行 的 正中间 ，对应位置为 res[0][(n-1)/2] 。 * 对于放置在矩阵中的每个节点，设对应位置为 res[r][c] ，将其左子节点放置在 res[r+1][c-2height-r-1] ，右子节点放置在 res[r+1][c+2height-r-1] 。 * 继续这一过程，直到树中的所有节点都妥善放置。 * 任意空单元格都应该包含空字符串 "" 。 返回构造得到的矩阵 res 。 示例 1： [https://assets.leetcode.com/uploads/2021/05/03/print1-tree.jpg] 输入：root = [1,2] 输出： [["","1",""], ["2","",""]] 示例 2： [https://assets.leetcode.com/uploads/2021/05/03/print2-tree.jpg] 输入：root = [1,2,3,null,4] 输出： [["","","","1","","",""], ["","2","","","","3",""], ["","","4","","","",""]] 提示： * 树中节点数在范围 [1, 210] 内 * -99 <= Node.val <= 99 * 树的深度在范围 [1, 10] 内
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来确定每个节点的位置，并填充矩阵。

算法步骤:
1. 计算树的高度。
2. 初始化结果矩阵，行数为高度加一，列数为 2^height - 1。
3. 使用 DFS 遍历树，递归地将每个节点放置在矩阵中的正确位置。
4. 返回结果矩阵。

关键点:
- 使用 DFS 递归地计算每个节点的位置。
- 通过计算左右子节点的位置来确保节点正确放置。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点只访问一次。
空间复杂度: O(n)，存储结果矩阵所需的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def print_tree(root: Optional[TreeNode]) -> List[List[str]]:
    """
    构造一个下标从 0 开始、大小为 m x n 的字符串矩阵 res，用以表示树的格式化布局。
    """
    def get_height(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + max(get_height(node.left), get_height(node.right))

    def fill_matrix(node: Optional[TreeNode], row: int, col: int, left: int, right: int):
        if not node:
            return
        mid = (left + right) // 2
        matrix[row][mid] = str(node.val)
        fill_matrix(node.left, row + 1, mid, left, mid - 1)
        fill_matrix(node.right, row + 1, mid, mid + 1, right)

    height = get_height(root)
    width = 2**height - 1
    matrix = [[""] * width for _ in range(height)]
    fill_matrix(root, 0, 0, 0, width - 1)
    return matrix

Solution = create_solution(print_tree)