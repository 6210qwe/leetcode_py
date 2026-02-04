# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000314
标题: 序列重建
难度: medium
链接: https://leetcode.cn/problems/ur2n8P/
题目类型: 图、拓扑排序、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 115. 序列重建 - 给定一个长度为 n 的整数数组 nums ，其中 nums 是范围为 [1，n] 的整数的排列。还提供了一个 2D 整数数组 sequences ，其中 sequences[i] 是 nums 的子序列。 检查 nums 是否是唯一的最短 超序列 。最短 超序列 是 长度最短 的序列，并且所有序列 sequences[i] 都是它的子序列。对于给定的数组 sequences ，可能存在多个有效的 超序列 。 * 例如，对于 sequences = [[1,2],[1,3]] ，有两个最短的 超序列 ，[1,2,3] 和 [1,3,2] 。 * 而对于 sequences = [[1,2],[1,3],[1,2,3]] ，唯一可能的最短 超序列 是 [1,2,3] 。[1,2,3,4] 是可能的超序列，但不是最短的。 如果 nums 是序列的唯一最短 超序列 ，则返回 true ，否则返回 false 。 子序列 是一个可以通过从另一个序列中删除一些元素或不删除任何元素，而不改变其余元素的顺序的序列。 示例 1： 输入：nums = [1,2,3], sequences = [[1,2],[1,3]] 输出：false 解释：有两种可能的超序列：[1,2,3]和[1,3,2]。 序列 [1,2] 是[1,2,3]和[1,3,2]的子序列。 序列 [1,3] 是[1,2,3]和[1,3,2]的子序列。 因为 nums 不是唯一最短的超序列，所以返回false。 示例 2： 输入：nums = [1,2,3], sequences = [[1,2]] 输出：false 解释：最短可能的超序列为 [1,2]。 序列 [1,2] 是它的子序列：[1,2]。 因为 nums 不是最短的超序列，所以返回false。 示例 3： 输入：nums = [1,2,3], sequences = [[1,2],[1,3],[2,3]] 输出：true 解释：最短可能的超序列为[1,2,3]。 序列 [1,2] 是它的一个子序列：[1,2,3]。 序列 [1,3] 是它的一个子序列：[1,2,3]。 序列 [2,3] 是它的一个子序列：[1,2,3]。 因为 nums 是唯一最短的超序列，所以返回true。 提示： * n == nums.length * 1 <= n <= 104 * nums 是 [1, n] 范围内所有整数的排列 * 1 <= sequences.length <= 104 * 1 <= sequences[i].length <= 104 * 1 <= sum(sequences[i].length) <= 105 * 1 <= sequences[i][j] <= n * sequences 的所有数组都是 唯一 的 * sequences[i] 是 nums 的一个子序列 注意：本题与主站 444 题相同：https://leetcode.cn/problems/sequence-reconstruction/ [https://leetcode.cn/problems/sequence-reconstruction/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用拓扑排序来检查 nums 是否是唯一的最短超序列。

算法步骤:
1. 构建图和入度表。
2. 初始化队列，将入度为 0 的节点加入队列。
3. 进行拓扑排序，每次从队列中取出一个节点，如果队列中有多个节点，则说明存在多种可能的超序列，返回 False。
4. 如果拓扑排序的结果与 nums 相同，则返回 True，否则返回 False。

关键点:
- 使用拓扑排序来验证 nums 是否是唯一的最短超序列。
- 通过入度表和队列来实现拓扑排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(V + E)，其中 V 是节点数，E 是边数。
空间复杂度: O(V + E)，用于存储图和入度表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(nums: List[int], sequences: List[List[int]]) -> bool:
    """
    函数式接口 - 检查 nums 是否是唯一的最短超序列
    """
    # 构建图和入度表
    graph = {i: [] for i in range(1, len(nums) + 1)}
    in_degree = {i: 0 for i in range(1, len(nums) + 1)}

    for seq in sequences:
        for i in range(len(seq) - 1):
            u, v = seq[i], seq[i + 1]
            graph[u].append(v)
            in_degree[v] += 1

    # 初始化队列，将入度为 0 的节点加入队列
    queue = [node for node in in_degree if in_degree[node] == 0]

    # 进行拓扑排序
    index = 0
    while queue:
        if len(queue) > 1:
            return False
        node = queue.pop(0)
        if node != nums[index]:
            return False
        index += 1
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return index == len(nums)


Solution = create_solution(solution_function_name)