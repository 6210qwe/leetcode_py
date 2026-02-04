# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1680
标题: Count All Possible Routes
难度: hard
链接: https://leetcode.cn/problems/count-all-possible-routes/
题目类型: 记忆化搜索、数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1575. 统计所有可行路径 - 给你一个 互不相同 的整数数组，其中 locations[i] 表示第 i 个城市的位置。同时给你 start，finish 和 fuel 分别表示出发城市、目的地城市和你初始拥有的汽油总量 每一步中，如果你在城市 i ，你可以选择任意一个城市 j ，满足 j != i 且 0 <= j < locations.length ，并移动到城市 j 。从城市 i 移动到 j 消耗的汽油量为 |locations[i] - locations[j]|，|x| 表示 x 的绝对值。 请注意， fuel 任何时刻都 不能 为负，且你 可以 经过任意城市超过一次（包括 start 和 finish ）。 请你返回从 start 到 finish 所有可能路径的数目。 由于答案可能很大， 请将它对 10^9 + 7 取余后返回。 示例 1： 输入：locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5 输出：4 解释：以下为所有可能路径，每一条都用了 5 单位的汽油： 1 -> 3 1 -> 2 -> 3 1 -> 4 -> 3 1 -> 4 -> 2 -> 3 示例 2： 输入：locations = [4,3,1], start = 1, finish = 0, fuel = 6 输出：5 解释：以下为所有可能的路径： 1 -> 0，使用汽油量为 fuel = 1 1 -> 2 -> 0，使用汽油量为 fuel = 5 1 -> 2 -> 1 -> 0，使用汽油量为 fuel = 5 1 -> 0 -> 1 -> 0，使用汽油量为 fuel = 3 1 -> 0 -> 1 -> 0 -> 1 -> 0，使用汽油量为 fuel = 5 示例 3： 输入：locations = [5,2,1], start = 0, finish = 2, fuel = 3 输出：0 解释：没有办法只用 3 单位的汽油从 0 到达 2 。因为最短路径需要 4 单位的汽油。 提示： * 2 <= locations.length <= 100 * 1 <= locations[i] <= 109 * 所有 locations 中的整数 互不相同 。 * 0 <= start, finish < locations.length * 1 <= fuel <= 200
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用记忆化搜索来避免重复计算。

算法步骤:
1. 定义一个递归函数 `dfs(current, remaining_fuel)`，表示从当前城市 `current` 出发，剩余 `remaining_fuel` 汽油时的路径数目。
2. 如果当前城市是终点城市，则路径数加1。
3. 对于每个可以到达的城市 `next_city`，如果从 `current` 到 `next_city` 的油耗不超过 `remaining_fuel`，则递归调用 `dfs(next_city, remaining_fuel - cost)`。
4. 使用缓存来存储已经计算过的状态，避免重复计算。

关键点:
- 使用记忆化搜索来优化递归。
- 注意路径数对 10^9 + 7 取余。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * fuel)，其中 n 是城市的数量，fuel 是初始汽油量。
空间复杂度: O(n * fuel)，用于存储记忆化搜索的状态。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

MOD = 10**9 + 7

def count_routes(locations: List[int], start: int, finish: int, fuel: int) -> int:
    from functools import lru_cache
    
    @lru_cache(None)
    def dfs(current: int, remaining_fuel: int) -> int:
        if remaining_fuel < 0:
            return 0
        total_paths = 1 if current == finish else 0
        for next_city in range(len(locations)):
            if next_city != current:
                cost = abs(locations[current] - locations[next_city])
                if remaining_fuel >= cost:
                    total_paths += dfs(next_city, remaining_fuel - cost)
                    total_paths %= MOD
        return total_paths
    
    return dfs(start, fuel)

Solution = create_solution(count_routes)