# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000090
标题: 最小跳跃次数
难度: hard
链接: https://leetcode.cn/problems/zui-xiao-tiao-yue-ci-shu/
题目类型: 广度优先搜索、线段树、数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 09. 最小跳跃次数 - 为了给刷题的同学一些奖励，力扣团队引入了一个弹簧游戏机。游戏机由 N 个特殊弹簧排成一排，编号为 0 到 N-1。初始有一个小球在编号 0 的弹簧处。若小球在编号为 i 的弹簧处，通过按动弹簧，可以选择把小球向右弹射 jump[i] 的距离，或者向左弹射到任意左侧弹簧的位置。也就是说，在编号为 i 弹簧处按动弹簧，小球可以弹向 0 到 i-1 中任意弹簧或者 i+jump[i] 的弹簧（若 i+jump[i]>=N ，则表示小球弹出了机器）。小球位于编号 0 处的弹簧时不能再向左弹。 为了获得奖励，你需要将小球弹出机器。请求出最少需要按动多少次弹簧，可以将小球从编号 0 弹簧弹出整个机器，即向右越过编号 N-1 的弹簧。 示例 1： > 输入：jump = [2, 5, 1, 1, 1, 1] > > 输出：3 > > 解释：小 Z 最少需要按动 3 次弹簧，小球依次到达的顺序为 0 -> 2 -> 1 -> 6，最终小球弹出了机器。 限制： * 1 <= jump.length <= 10^6 * 1 <= jump[i] <= 10000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）来找到从起点到终点的最短路径。

算法步骤:
1. 初始化一个队列，将起点 (0, 0) 加入队列，其中 0 表示当前弹簧位置，0 表示当前步数。
2. 使用一个集合 visited 来记录已经访问过的弹簧位置，避免重复访问。
3. 进行 BFS：
   - 从队列中取出一个节点 (position, steps)。
   - 如果 position + jump[position] >= N，则返回 steps + 1。
   - 将 position + jump[position] 和 0 到 position-1 的所有位置加入队列，并标记为已访问。
4. 如果队列为空且未找到解，则返回 -1。

关键点:
- 使用 BFS 可以保证找到最短路径。
- 使用集合 visited 来避免重复访问，提高效率。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(N)
空间复杂度: O(N)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(jump: List[int]) -> int:
    """
    函数式接口 - 使用广度优先搜索找到最小跳跃次数
    """
    N = len(jump)
    if N == 0:
        return -1

    from collections import deque
    queue = deque([(0, 0)])  # (position, steps)
    visited = set([0])

    while queue:
        position, steps = queue.popleft()
        if position + jump[position] >= N:
            return steps + 1
        for next_pos in range(position):
            if next_pos not in visited:
                visited.add(next_pos)
                queue.append((next_pos, steps + 1))
        if position + jump[position] not in visited:
            visited.add(position + jump[position])
            queue.append((position + jump[position], steps + 1))

    return -1


Solution = create_solution(solution_function_name)