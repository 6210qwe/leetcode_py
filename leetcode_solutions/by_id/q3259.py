# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3259
标题: Binary Tree Nodes
难度: medium
链接: https://leetcode.cn/problems/binary-tree-nodes/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3054. 二叉树节点 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用递归或迭代的方法构建二叉树，并返回根节点。

算法步骤:
1. 检查输入数据是否为空，如果为空则返回 None。
2. 创建一个字典来存储每个节点的引用。
3. 遍历输入数据，创建每个节点并将其存储在字典中。
4. 再次遍历输入数据，设置每个节点的左子节点和右子节点。
5. 返回根节点。

关键点:
- 使用字典来存储节点引用，以便快速查找和设置子节点。
- 通过两次遍历来构建二叉树。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是节点的数量。需要遍历两次输入数据。
空间复杂度: O(n)，使用了额外的字典来存储节点引用。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(node_list: List[List[int]]) -> Optional[TreeNode]:
    """
    函数式接口 - 构建二叉树并返回根节点
    """
    if not node_list:
        return None

    # 创建一个字典来存储每个节点的引用
    node_dict = {}
    
    # 第一次遍历：创建所有节点
    for node_id, left_id, right_id in node_list:
        if node_id not in node_dict:
            node_dict[node_id] = TreeNode(node_id)
        if left_id != -1 and left_id not in node_dict:
            node_dict[left_id] = TreeNode(left_id)
        if right_id != -1 and right_id not in node_dict:
            node_dict[right_id] = TreeNode(right_id)

    # 第二次遍历：设置每个节点的左子节点和右子节点
    for node_id, left_id, right_id in node_list:
        if left_id != -1:
            node_dict[node_id].left = node_dict[left_id]
        if right_id != -1:
            node_dict[node_id].right = node_dict[right_id]

    # 找到根节点
    root = None
    for node_id, _, _ in node_list:
        if all(node_id != left_id and node_id != right_id for _, left_id, right_id in node_list):
            root = node_dict[node_id]
            break

    return root


Solution = create_solution(solution_function_name)