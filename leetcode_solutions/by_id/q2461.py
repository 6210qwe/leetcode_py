# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2461
标题: Amount of Time for Binary Tree to Be Infected
难度: medium
链接: https://leetcode.cn/problems/amount-of-time-for-binary-tree-to-be-infected/
题目类型: 树、深度优先搜索、广度优先搜索、哈希表、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2385. 感染二叉树需要的总时间 - 给你一棵二叉树的根节点 root ，二叉树中节点的值 互不相同 。另给你一个整数 start 。在第 0 分钟，感染 将会从值为 start 的节点开始爆发。 每分钟，如果节点满足以下全部条件，就会被感染： * 节点此前还没有感染。 * 节点与一个已感染节点相邻。 返回感染整棵树需要的分钟数。 示例 1： [https://assets.leetcode.com/uploads/2022/06/25/image-20220625231744-1.png] 输入：root = [1,5,3,null,4,10,6,9,2], start = 3 输出：4 解释：节点按以下过程被感染： - 第 0 分钟：节点 3 - 第 1 分钟：节点 1、10、6 - 第 2 分钟：节点5 - 第 3 分钟：节点 4 - 第 4 分钟：节点 9 和 2 感染整棵树需要 4 分钟，所以返回 4 。 示例 2： [https://assets.leetcode.com/uploads/2022/06/25/image-20220625231812-2.png] 输入：root = [1], start = 1 输出：0 解释：第 0 分钟，树中唯一一个节点处于感染状态，返回 0 。 提示： * 树中节点的数目在范围 [1, 105] 内 * 1 <= Node.val <= 105 * 每个节点的值 互不相同 * 树中必定存在值为 start 的节点
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 BFS 来模拟感染过程，并通过 DFS 构建每个节点的父节点关系。

算法步骤:
1. 使用 DFS 构建每个节点的父节点关系。
2. 使用 BFS 从 start 节点开始模拟感染过程，记录每分钟感染的节点。
3. 返回感染整棵树所需的分钟数。

关键点:
- 使用字典存储每个节点的父节点关系。
- 使用队列进行 BFS 模拟感染过程。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是树中节点的数量。DFS 和 BFS 各遍历一次树。
空间复杂度: O(n)，存储父节点关系和队列所需的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def amount_of_time(root: Optional[TreeNode], start: int) -> int:
    # 构建每个节点的父节点关系
    parent_map = {}
    start_node = None

    def dfs(node: TreeNode, parent: Optional[TreeNode]):
        nonlocal start_node
        if node is None:
            return
        if node.val == start:
            start_node = node
        parent_map[node] = parent
        dfs(node.left, node)
        dfs(node.right, node)

    dfs(root, None)

    # 使用 BFS 模拟感染过程
    from collections import deque
    queue = deque([start_node])
    visited = set([start_node])
    time = 0

    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            for neighbor in [node.left, node.right, parent_map[node]]:
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        if queue:
            time += 1

    return time

Solution = create_solution(amount_of_time)