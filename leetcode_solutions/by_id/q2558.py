# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2558
标题: Minimum Number of Operations to Sort a Binary Tree by Level
难度: medium
链接: https://leetcode.cn/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/
题目类型: 树、广度优先搜索、二叉树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2471. 逐层排序二叉树所需的最少操作数目 - 给你一个 值互不相同 的二叉树的根节点 root 。 在一步操作中，你可以选择 同一层 上任意两个节点，交换这两个节点的值。 返回每一层按 严格递增顺序 排序所需的最少操作数目。 节点的 层数 是该节点和根节点之间的路径的边数。 示例 1 ： [https://assets.leetcode.com/uploads/2022/09/18/image-20220918174006-2.png] 输入：root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10] 输出：3 解释： - 交换 4 和 3 。第 2 层变为 [3,4] 。 - 交换 7 和 5 。第 3 层变为 [5,6,8,7] 。 - 交换 8 和 7 。第 3 层变为 [5,6,7,8] 。 共计用了 3 步操作，所以返回 3 。 可以证明 3 是需要的最少操作数目。 示例 2 ： [https://assets.leetcode.com/uploads/2022/09/18/image-20220918174026-3.png] 输入：root = [1,3,2,7,6,5,4] 输出：3 解释： - 交换 3 和 2 。第 2 层变为 [2,3] 。 - 交换 7 和 4 。第 3 层变为 [4,6,5,7] 。 - 交换 6 和 5 。第 3 层变为 [4,5,6,7] 。 共计用了 3 步操作，所以返回 3 。 可以证明 3 是需要的最少操作数目。 示例 3 ： [https://assets.leetcode.com/uploads/2022/09/18/image-20220918174052-4.png] 输入：root = [1,2,3,4,5,6] 输出：0 解释：每一层已经按递增顺序排序，所以返回 0 。 提示： * 树中节点的数目在范围 [1, 105] 。 * 1 <= Node.val <= 105 * 树中的所有值 互不相同 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）遍历每一层，并使用贪心算法计算每层排序所需的最少交换次数。

算法步骤:
1. 使用 BFS 遍历二叉树，记录每一层的节点值。
2. 对于每一层，计算将其排序所需的最少交换次数。
3. 累加所有层的交换次数，得到最终结果。

关键点:
- 使用贪心算法计算每层排序所需的最少交换次数。
- 通过 BFS 记录每一层的节点值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是树中节点的数目。BFS 的时间复杂度是 O(n)，而每层排序的时间复杂度是 O(m log m)，其中 m 是该层的节点数。
空间复杂度: O(n)，用于存储每一层的节点值。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def min_swaps_to_sort(arr: List[int]) -> int:
    """
    计算将数组排序所需的最少交换次数。
    """
    n = len(arr)
    arr_pos = [*enumerate(arr)]
    arr_pos.sort(key=lambda it: it[1])
    visited = {i: False for i in range(n)}
    ans = 0

    for i in range(n):
        if visited[i] or arr_pos[i][0] == i:
            continue
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = arr_pos[j][0]
            cycle_size += 1
        if cycle_size > 0:
            ans += (cycle_size - 1)
    return ans

def solution_function_name(root: Optional[TreeNode]) -> int:
    """
    函数式接口 - 计算逐层排序二叉树所需的最少操作数目
    """
    if not root:
        return 0

    from collections import deque
    queue = deque([root])
    total_swaps = 0

    while queue:
        level_size = len(queue)
        level_values = []

        for _ in range(level_size):
            node = queue.popleft()
            level_values.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        total_swaps += min_swaps_to_sort(level_values)

    return total_swaps

Solution = create_solution(solution_function_name)