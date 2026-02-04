# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 772
标题: Construct Quad Tree
难度: medium
链接: https://leetcode.cn/problems/construct-quad-tree/
题目类型: 树、数组、分治、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
427. 建立四叉树 - 给你一个 n * n 矩阵 grid ，矩阵由若干 0 和 1 组成。请你用四叉树表示该矩阵 grid 。 你需要返回能表示矩阵 grid 的 四叉树 的根结点。 四叉树数据结构中，每个内部节点只有四个子节点。此外，每个节点都有两个属性： * val：储存叶子结点所代表的区域的值。1 对应 True，0 对应 False。注意，当 isLeaf 为 False 时，你可以把 True 或者 False 赋值给节点，两种值都会被判题机制 接受 。 * isLeaf: 当这个节点是一个叶子结点时为 True，如果它有 4 个子节点则为 False 。 class Node { public boolean val; public boolean isLeaf; public Node topLeft; public Node topRight; public Node bottomLeft; public Node bottomRight; } 我们可以按以下步骤为二维区域构建四叉树： 1. 如果当前网格的值相同（即，全为 0 或者全为 1），将 isLeaf 设为 True ，将 val 设为网格相应的值，并将四个子节点都设为 Null 然后停止。 2. 如果当前网格的值不同，将 isLeaf 设为 False， 将 val 设为任意值，然后如下图所示，将当前网格划分为四个子网格。 3. 使用适当的子网格递归每个子节点。 [https://assets.leetcode.com/uploads/2020/02/11/new_top.png] 如果你想了解更多关于四叉树的内容，可以参考 百科 [https://baike.baidu.com/item/%E5%9B%9B%E5%8F%89%E6%A0%91] 。 四叉树格式： 你不需要阅读本节来解决这个问题。只有当你想了解输出格式时才会这样做。输出为使用层序遍历后四叉树的序列化形式，其中 null 表示路径终止符，其下面不存在节点。 它与二叉树的序列化非常相似。唯一的区别是节点以列表形式表示 [isLeaf, val] 。 如果 isLeaf 或者 val 的值为 True ，则表示它在列表 [isLeaf, val] 中的值为 1 ；如果 isLeaf 或者 val 的值为 False ，则表示值为 0 。 示例 1： [https://assets.leetcode.com/uploads/2020/02/11/grid1.png] 输入：grid = [[0,1],[1,0]] 输出：[[0,1],[1,0],[1,1],[1,1],[1,0]] 解释：此示例的解释如下： 请注意，在下面四叉树的图示中，0 表示 false，1 表示 True 。 [https://assets.leetcode.com/uploads/2020/02/12/e1tree.png] 示例 2： [https://assets.leetcode.com/uploads/2020/02/12/e2mat.png] 输入：grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]] 输出：[[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]] 解释：网格中的所有值都不相同。我们将网格划分为四个子网格。 topLeft，bottomLeft 和 bottomRight 均具有相同的值。 topRight 具有不同的值，因此我们将其再分为 4 个子网格，这样每个子网格都具有相同的值。 解释如下图所示： [https://assets.leetcode.com/uploads/2020/02/12/e2tree.png] 提示： 1. n == grid.length == grid[i].length 2. n == 2x 其中 0 <= x <= 6
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 递归地划分网格，直到每个子网格的值相同。

算法步骤:
1. 检查当前网格的所有值是否相同。
2. 如果相同，创建一个叶子节点并返回。
3. 如果不同，将当前网格划分为四个子网格，并递归处理每个子网格。
4. 创建一个内部节点，将四个子节点连接到该节点，并返回。

关键点:
- 递归地处理每个子网格。
- 只有当子网格的值完全相同时，才创建叶子节点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 log n)，其中 n 是网格的边长。每次递归调用处理的子网格大小减半，总共需要 O(log n) 层递归，每层递归需要 O(n^2) 时间检查网格值。
空间复杂度: O(n^2)，递归调用栈的最大深度为 O(log n)，每个节点需要存储 O(1) 的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional


class Node:
    def __init__(self, val: bool, is_leaf: bool, top_left: 'Node' = None, top_right: 'Node' = None, bottom_left: 'Node' = None, bottom_right: 'Node' = None):
        self.val = val
        self.is_leaf = is_leaf
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right


def construct(grid: List[List[int]]) -> 'Node':
    def build_quad_tree(r0: int, c0: int, r1: int, c1: int) -> 'Node':
        if r1 - r0 == 1:
            return Node(bool(grid[r0][c0]), True)
        
        r_mid = (r0 + r1) // 2
        c_mid = (c0 + c1) // 2
        
        top_left = build_quad_tree(r0, c0, r_mid, c_mid)
        top_right = build_quad_tree(r0, c_mid, r_mid, c1)
        bottom_left = build_quad_tree(r_mid, c0, r1, c_mid)
        bottom_right = build_quad_tree(r_mid, c_mid, r1, c1)
        
        if top_left.is_leaf and top_right.is_leaf and bottom_left.is_leaf and bottom_right.is_leaf and \
           top_left.val == top_right.val == bottom_left.val == bottom_right.val:
            return Node(top_left.val, True)
        
        return Node(False, False, top_left, top_right, bottom_left, bottom_right)
    
    return build_quad_tree(0, 0, len(grid), len(grid))


Solution = create_solution(construct)