# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 4165
标题: Find Diameter Endpoints of a Tree
难度: medium
链接: https://leetcode.cn/problems/find-diameter-endpoints-of-a-tree/
题目类型: 树、广度优先搜索、图
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3787. 查找树的直径端点 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两次深度优先搜索（DFS）来找到树的直径及其端点。

算法步骤:
1. 从任意节点开始进行第一次 DFS，找到距离该节点最远的节点 A。
2. 从节点 A 开始进行第二次 DFS，找到距离 A 最远的节点 B。A 和 B 即为树的直径端点。

关键点:
- 第一次 DFS 找到的节点 A 必定是树的直径的一个端点。
- 第二次 DFS 从 A 开始，找到的节点 B 是树的直径的另一个端点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点最多被访问两次。
空间复杂度: O(n)，递归调用栈的空间复杂度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def find_farthest_node(node: TreeNode, parent: Optional[TreeNode]) -> (int, TreeNode):
    """从当前节点出发，找到最远的节点及其距离"""
    max_distance = 0
    farthest_node = node
    for child in [node.left, node.right]:
        if child and child != parent:
            distance, farthest_child = find_farthest_node(child, node)
            if distance + 1 > max_distance:
                max_distance = distance + 1
                farthest_node = farthest_child
    return max_distance, farthest_node

def solution_function_name(root: TreeNode) -> List[int]:
    """
    函数式接口 - 找到树的直径端点
    """
    if not root:
        return []
    
    # 第一次 DFS 找到最远的节点 A
    _, farthest_node_A = find_farthest_node(root, None)
    
    # 第二次 DFS 从节点 A 开始，找到最远的节点 B
    _, farthest_node_B = find_farthest_node(farthest_node_A, None)
    
    return [farthest_node_A.val, farthest_node_B.val]

Solution = create_solution(solution_function_name)