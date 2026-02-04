# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1745
标题: Find Nearest Right Node in Binary Tree
难度: medium
链接: https://leetcode.cn/problems/find-nearest-right-node-in-binary-tree/
题目类型: 树、广度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1602. 找到二叉树中最近的右侧节点 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）来遍历二叉树，找到目标节点后返回其右侧相邻节点。

算法步骤:
1. 初始化一个队列，将根节点加入队列。
2. 开始层次遍历：
   - 对于每一层，记录当前层的节点数量。
   - 遍历当前层的所有节点：
     - 如果当前节点是目标节点，则返回队列中的下一个节点（即右侧相邻节点）。
     - 将当前节点的左子节点和右子节点依次加入队列。
3. 如果遍历完整棵树未找到目标节点，则返回 None。

关键点:
- 使用队列进行层次遍历。
- 在同一层内找到目标节点后，直接返回其右侧相邻节点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是二叉树的节点数。最坏情况下需要遍历整棵树。
空间复杂度: O(n)，队列在最坏情况下需要存储整棵树的所有节点。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def find_nearest_right_node(root: Optional[TreeNode], u: TreeNode) -> Optional[TreeNode]:
    """
    找到二叉树中最近的右侧节点
    :param root: 二叉树的根节点
    :param u: 目标节点
    :return: 目标节点的右侧相邻节点，如果不存在则返回 None
    """
    if not root:
        return None

    from collections import deque
    queue = deque([root])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if node == u:
                # 如果当前节点是目标节点，返回队列中的下一个节点
                if i < level_size - 1:
                    return queue.popleft()
                else:
                    return None
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return None

Solution = create_solution(find_nearest_right_node)