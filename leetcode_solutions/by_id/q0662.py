# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 662
标题: Maximum Width of Binary Tree
难度: medium
链接: https://leetcode.cn/problems/maximum-width-of-binary-tree/
题目类型: 树、深度优先搜索、广度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
662. 二叉树最大宽度 - 给你一棵二叉树的根节点 root ，返回树的 最大宽度 。 树的 最大宽度 是所有层中最大的 宽度 。 每一层的 宽度 被定义为该层最左和最右的非空节点（即，两个端点）之间的长度。将这个二叉树视作与满二叉树结构相同，两端点间会出现一些延伸到这一层的 null 节点，这些 null 节点也计入长度。 题目数据保证答案将会在 32 位 带符号整数范围内。 示例 1： [https://assets.leetcode.com/uploads/2021/05/03/width1-tree.jpg] 输入：root = [1,3,2,5,3,null,9] 输出：4 解释：最大宽度出现在树的第 3 层，宽度为 4 (5,3,null,9) 。 示例 2： [https://assets.leetcode.com/uploads/2022/03/14/maximum-width-of-binary-tree-v3.jpg] 输入：root = [1,3,2,5,null,null,9,6,null,7] 输出：7 解释：最大宽度出现在树的第 4 层，宽度为 7 (6,null,null,null,null,null,7) 。 示例 3： [https://assets.leetcode.com/uploads/2021/05/03/width3-tree.jpg] 输入：root = [1,3,2,5] 输出：2 解释：最大宽度出现在树的第 2 层，宽度为 2 (3,2) 。 提示： * 树中节点的数目范围是 [1, 3000] * -100 <= Node.val <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）遍历树，并记录每一层的最左和最右节点的位置。

算法步骤:
1. 初始化一个队列，将根节点及其位置（设为 1）加入队列。
2. 使用一个字典来记录每一层的第一个节点的位置。
3. 开始层次遍历：
   - 对于每个节点，计算其子节点的位置（左子节点为 2 * pos，右子节点为 2 * pos + 1）。
   - 更新当前层的最大宽度。
   - 将子节点及其位置加入队列。
4. 返回最大宽度。

关键点:
- 使用位置编号来计算宽度。
- 记录每一层的第一个节点的位置以便计算宽度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点只会被访问一次。
空间复杂度: O(n)，队列和字典的空间开销。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def solution_function_name(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    max_width = 0
    queue = [(root, 1)]
    level_first_pos = {}

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node, pos = queue.pop(0)

            # 记录每一层的第一个节点的位置
            if i == 0:
                level_first_pos[node.depth] = pos

            # 计算当前层的宽度
            if i == level_size - 1:
                max_width = max(max_width, pos - level_first_pos[node.depth] + 1)

            # 将子节点及其位置加入队列
            if node.left:
                node.left.depth = node.depth + 1
                queue.append((node.left, 2 * pos))
            if node.right:
                node.right.depth = node.depth + 1
                queue.append((node.right, 2 * pos + 1))

    return max_width

Solution = create_solution(solution_function_name)