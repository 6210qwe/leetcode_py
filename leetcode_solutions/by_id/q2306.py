# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2306
标题: Create Binary Tree From Descriptions
难度: medium
链接: https://leetcode.cn/problems/create-binary-tree-from-descriptions/
题目类型: 树、数组、哈希表、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2196. 根据描述创建二叉树 - 给你一个二维整数数组 descriptions ，其中 descriptions[i] = [parenti, childi, isLefti] 表示 parenti 是 childi 在 二叉树 中的 父节点，二叉树中各节点的值 互不相同 。此外： * 如果 isLefti == 1 ，那么 childi 就是 parenti 的左子节点。 * 如果 isLefti == 0 ，那么 childi 就是 parenti 的右子节点。 请你根据 descriptions 的描述来构造二叉树并返回其 根节点 。 测试用例会保证可以构造出 有效 的二叉树。 示例 1： [https://assets.leetcode.com/uploads/2022/02/09/example1drawio.png] 输入：descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]] 输出：[50,20,80,15,17,19] 解释：根节点是值为 50 的节点，因为它没有父节点。 结果二叉树如上图所示。 示例 2： [https://assets.leetcode.com/uploads/2022/02/09/example2drawio.png] 输入：descriptions = [[1,2,1],[2,3,0],[3,4,1]] 输出：[1,2,null,null,3,4] 解释：根节点是值为 1 的节点，因为它没有父节点。 结果二叉树如上图所示。 提示： * 1 <= descriptions.length <= 104 * descriptions[i].length == 3 * 1 <= parenti, childi <= 105 * 0 <= isLefti <= 1 * descriptions 所描述的二叉树是一棵有效二叉树
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表存储节点，并通过集合来确定根节点。

算法步骤:
1. 初始化一个哈希表 `nodes` 来存储所有节点。
2. 初始化一个集合 `children` 来存储所有子节点。
3. 遍历 `descriptions`，对于每个描述：
   - 如果父节点或子节点不在 `nodes` 中，则创建新节点并加入 `nodes`。
   - 根据 `isLeft` 的值，将子节点连接到父节点的左或右子节点。
   - 将子节点加入 `children` 集合。
4. 根节点是 `nodes` 中不在 `children` 集合中的节点。
5. 返回根节点。

关键点:
- 使用哈希表存储节点，方便快速查找和更新。
- 使用集合来确定根节点，避免重复遍历。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 descriptions 的长度。我们只需要遍历一次 descriptions。
空间复杂度: O(n)，用于存储节点和子节点集合。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def create_binary_tree_from_descriptions(descriptions: List[List[int]]) -> Optional[TreeNode]:
    nodes = {}
    children = set()

    for parent, child, is_left in descriptions:
        if parent not in nodes:
            nodes[parent] = TreeNode(parent)
        if child not in nodes:
            nodes[child] = TreeNode(child)

        if is_left:
            nodes[parent].left = nodes[child]
        else:
            nodes[parent].right = nodes[child]

        children.add(child)

    # 根节点是不在 children 集合中的节点
    for node in nodes:
        if node not in children:
            return nodes[node]

    return None


Solution = create_solution(create_binary_tree_from_descriptions)