# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 893
标题: All Nodes Distance K in Binary Tree
难度: medium
链接: https://leetcode.cn/problems/all-nodes-distance-k-in-binary-tree/
题目类型: 树、深度优先搜索、广度优先搜索、哈希表、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
863. 二叉树中所有距离为 K 的结点 - 给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 k ，返回到目标结点 target 距离为 k 的所有结点的值的数组。 答案可以以 任何顺序 返回。 示例 1： [https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/28/sketch0.png] 输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2 输出：[7,4,1] 解释：所求结点为与目标结点（值为 5）距离为 2 的结点，值分别为 7，4，以及 1 示例 2: 输入: root = [1], target = 1, k = 3 输出: [] 提示: * 节点数在 [1, 500] 范围内 * 0 <= Node.val <= 500 * Node.val 中所有值 不同 * 目标结点 target 是树上的结点。 * 0 <= k <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 构建从每个节点到其父节点的映射，然后使用广度优先搜索 (BFS) 找到距离目标节点 k 的所有节点。

算法步骤:
1. 使用 DFS 构建从每个节点到其父节点的映射。
2. 使用 BFS 从目标节点开始，找到距离为 k 的所有节点。

关键点:
- 使用字典存储每个节点的父节点，以便在 BFS 中能够向上遍历。
- 使用集合记录已经访问过的节点，避免重复访问。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。构建父节点映射和 BFS 都需要遍历所有节点。
空间复杂度: O(n)，用于存储父节点映射和访问记录。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def find_nodes_distance_k(root: TreeNode, target: TreeNode, k: int) -> List[int]:
    # 构建从每个节点到其父节点的映射
    parent_map = {}
    def dfs(node: TreeNode, parent: Optional[TreeNode]):
        if node:
            parent_map[node] = parent
            dfs(node.left, node)
            dfs(node.right, node)
    
    dfs(root, None)

    # 使用 BFS 从目标节点开始，找到距离为 k 的所有节点
    queue = [(target, 0)]
    visited = {target}
    result = []

    while queue:
        node, distance = queue.pop(0)
        if distance == k:
            result.append(node.val)
        for neighbor in (node.left, node.right, parent_map.get(node)):
            if neighbor and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    
    return result

Solution = create_solution(find_nodes_distance_k)