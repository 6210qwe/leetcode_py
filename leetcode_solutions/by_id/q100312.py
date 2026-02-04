# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100312
标题: 彩灯装饰记录 II
难度: easy
链接: https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/
题目类型: 树、广度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 150. 彩灯装饰记录 II - 一棵圣诞树记作根节点为 root 的二叉树，节点值为该位置装饰彩灯的颜色编号。请按照从左到右的顺序返回每一层彩灯编号，每一层的结果记录于一行。 示例 1： [https://pic.leetcode.cn/1694758674-XYrUiV-%E5%89%91%E6%8C%87%20Offer%2032%20-%20I_%E7%A4%BA%E4%BE%8B1.png] 输入：root = [8,17,21,18,null,null,6] 输出：[[8],[17,21],[18,6]] 提示： 1. 节点总数 <= 1000 注意：本题与主站 102 题相同：https://leetcode.cn/problems/binary-tree-level-order-traversal/ [https://leetcode.cn/problems/binary-tree-level-order-traversal/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）逐层遍历二叉树，并将每一层的节点值记录下来。

算法步骤:
1. 初始化一个队列，将根节点加入队列。
2. 当队列不为空时，进行以下操作：
   - 记录当前队列的长度，即当前层的节点数。
   - 初始化一个空列表，用于存储当前层的节点值。
   - 遍历当前层的所有节点，将它们的值加入列表，并将它们的子节点加入队列。
   - 将当前层的节点值列表加入结果列表。
3. 返回结果列表。

关键点:
- 使用队列进行层次遍历。
- 每次处理一层节点时，记录当前层的节点数，以便在遍历时区分不同层的节点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是二叉树的节点数。每个节点只会被访问一次。
空间复杂度: O(n)，队列中最多会包含所有节点。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    函数式接口 - 二叉树的层次遍历
    """
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        level_size = len(queue)
        level_nodes = []

        for _ in range(level_size):
            node = queue.pop(0)
            level_nodes.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_nodes)

    return result

Solution = create_solution(level_order)