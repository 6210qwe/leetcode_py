# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1757
标题: Minimum Jumps to Reach Home
难度: medium
链接: https://leetcode.cn/problems/minimum-jumps-to-reach-home/
题目类型: 广度优先搜索、数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1654. 到家的最少跳跃次数 - 有一只跳蚤的家在数轴上的位置 x 处。请你帮助它从位置 0 出发，到达它的家。 跳蚤跳跃的规则如下： * 它可以 往前 跳恰好 a 个位置（即往右跳）。 * 它可以 往后 跳恰好 b 个位置（即往左跳）。 * 它不能 连续 往后跳 2 次。 * 它不能跳到任何 forbidden 数组中的位置。 跳蚤可以往前跳 超过 它的家的位置，但是它 不能跳到负整数 的位置。 给你一个整数数组 forbidden ，其中 forbidden[i] 是跳蚤不能跳到的位置，同时给你整数 a， b 和 x ，请你返回跳蚤到家的最少跳跃次数。如果没有恰好到达 x 的可行方案，请你返回 -1 。 示例 1： 输入：forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9 输出：3 解释：往前跳 3 次（0 -> 3 -> 6 -> 9），跳蚤就到家了。 示例 2： 输入：forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11 输出：-1 示例 3： 输入：forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7 输出：2 解释：往前跳一次（0 -> 16），然后往回跳一次（16 -> 7），跳蚤就到家了。 提示： * 1 <= forbidden.length <= 1000 * 1 <= a, b, forbidden[i] <= 2000 * 0 <= x <= 2000 * forbidden 中所有位置互不相同。 * 位置 x 不在 forbidden 中。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索 (BFS) 来找到从起点 0 到目标 x 的最短路径。为了避免重复访问和连续两次向后跳跃，我们使用一个集合来记录已经访问过的位置，并使用队列来存储当前的跳跃状态。

算法步骤:
1. 初始化一个队列，将起点 (0, False) 加入队列，表示当前位置为 0，且上一步没有向后跳跃。
2. 使用一个集合 `visited` 来记录已经访问过的位置，以避免重复访问。
3. 开始 BFS 循环：
   - 从队列中取出当前状态 (position, is_backwards)。
   - 如果当前位置等于目标 x，则返回当前步数。
   - 计算向前跳跃的新位置 `next_pos`，如果新位置未被访问且不在 forbidden 中，则将其加入队列。
   - 如果上一步不是向后跳跃，计算向后跳跃的新位置 `prev_pos`，如果新位置未被访问且不在 forbidden 中，则将其加入队列。
4. 如果队列为空且未找到目标 x，则返回 -1。

关键点:
- 使用 BFS 确保找到最短路径。
- 使用集合 `visited` 避免重复访问。
- 使用布尔值 `is_backwards` 来跟踪上一步是否是向后跳跃。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + max(forbidden))，其中 n 是 x 的值，max(forbidden) 是 forbidden 中的最大值。最坏情况下，我们需要遍历所有可能的位置。
空间复杂度: O(n + max(forbidden))，用于存储 visited 集合和队列。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_jumps_to_reach_home(forbidden: List[int], a: int, b: int, x: int) -> int:
    """
    返回跳蚤到家的最少跳跃次数。
    """
    from collections import deque

    # 将 forbidden 转换为集合，方便快速查找
    forbidden_set = set(forbidden)
    # 初始化队列，存储 (位置, 是否上次向后跳跃, 当前步数)
    queue = deque([(0, False, 0)])
    # 初始化已访问集合
    visited = set([0])

    while queue:
        position, is_backwards, steps = queue.popleft()

        # 如果当前位置等于目标 x，则返回当前步数
        if position == x:
            return steps

        # 计算向前跳跃的新位置
        next_pos = position + a
        if next_pos not in visited and next_pos not in forbidden_set and next_pos <= 6000:  # 6000 是一个合理的上限
            visited.add(next_pos)
            queue.append((next_pos, False, steps + 1))

        # 如果上一步不是向后跳跃，计算向后跳跃的新位置
        if not is_backwards:
            prev_pos = position - b
            if prev_pos >= 0 and prev_pos not in visited and prev_pos not in forbidden_set:
                visited.add(prev_pos)
                queue.append((prev_pos, True, steps + 1))

    # 如果队列为空且未找到目标 x，则返回 -1
    return -1


Solution = create_solution(min_jumps_to_reach_home)