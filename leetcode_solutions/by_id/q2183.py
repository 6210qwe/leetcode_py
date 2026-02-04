# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2183
标题: Minimum Operations to Convert Number
难度: medium
链接: https://leetcode.cn/problems/minimum-operations-to-convert-number/
题目类型: 广度优先搜索、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2059. 转化数字的最小运算数 - 给你一个下标从 0 开始的整数数组 nums ，该数组由 互不相同 的数字组成。另给你两个整数 start 和 goal 。 整数 x 的值最开始设为 start ，你打算执行一些运算使 x 转化为 goal 。你可以对数字 x 重复执行下述运算： 如果 0 <= x <= 1000 ，那么，对于数组中的任一下标 i（0 <= i < nums.length），可以将 x 设为下述任一值： * x + nums[i] * x - nums[i] * x ^ nums[i]（按位异或 XOR） 注意，你可以按任意顺序使用每个 nums[i] 任意次。使 x 越过 0 <= x <= 1000 范围的运算同样可以生效，但该该运算执行后将不能执行其他运算。 返回将 x = start 转化为 goal 的最小操作数；如果无法完成转化，则返回 -1 。 示例 1： 输入：nums = [2,4,12], start = 2, goal = 12 输出：2 解释： 可以按 2 → 14 → 12 的转化路径进行，只需执行下述 2 次运算： - 2 + 12 = 14 - 14 - 2 = 12 示例 2： 输入：nums = [3,5,7], start = 0, goal = -4 输出：2 解释： 可以按 0 → 3 → -4 的转化路径进行，只需执行下述 2 次运算： - 0 + 3 = 3 - 3 - 7 = -4 注意，最后一步运算使 x 超过范围 0 <= x <= 1000 ，但该运算仍然可以生效。 示例 3： 输入：nums = [2,8,16], start = 0, goal = 1 输出：-1 解释： 无法将 0 转化为 1 提示： * 1 <= nums.length <= 1000 * -109 <= nums[i], goal <= 109 * 0 <= start <= 1000 * start != goal * nums 中的所有整数互不相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索 (BFS) 来找到从 start 到 goal 的最短路径。

算法步骤:
1. 初始化一个队列，将 start 加入队列，并初始化一个集合 visited 来记录已经访问过的节点。
2. 开始 BFS 循环：
   - 从队列中取出当前节点 current。
   - 如果 current 等于 goal，返回当前的操作数。
   - 对于每个 nums[i]，计算三种可能的新状态：current + nums[i]，current - nums[i]，current ^ nums[i]。
   - 如果新状态在 0 到 1000 之间且未被访问过，将其加入队列和 visited 集合。
3. 如果队列为空且未找到 goal，返回 -1。

关键点:
- 使用 BFS 可以保证找到最短路径。
- 使用集合来记录已访问的状态，避免重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(3 * n * 1000) = O(n)，其中 n 是 nums 的长度。因为每个状态最多有 3 种变化，且状态范围在 0 到 1000 之间。
空间复杂度: O(1000) = O(1)，因为 visited 集合的最大大小为 1001。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_operations_to_convert_number(nums: List[int], start: int, goal: int) -> int:
    """
    函数式接口 - 使用广度优先搜索 (BFS) 找到从 start 到 goal 的最短路径。
    """
    from collections import deque

    # 初始化队列和已访问集合
    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        current, steps = queue.popleft()

        if current == goal:
            return steps

        for num in nums:
            for new_state in [current + num, current - num, current ^ num]:
                if 0 <= new_state <= 1000 and new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, steps + 1))

    return -1


Solution = create_solution(min_operations_to_convert_number)