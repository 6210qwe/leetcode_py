# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3095
标题: Maximum Number of Alloys
难度: medium
链接: https://leetcode.cn/problems/maximum-number-of-alloys/
题目类型: 数组、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2861. 最大合金数 - 假设你是一家合金制造公司的老板，你的公司使用多种金属来制造合金。现在共有 n 种不同类型的金属可以使用，并且你可以使用 k 台机器来制造合金。每台机器都需要特定数量的每种金属来创建合金。 对于第 i 台机器而言，创建合金需要 composition[i][j] 份 j 类型金属。最初，你拥有 stock[x] 份 x 类型金属，而每购入一份 x 类型金属需要花费 cost[x] 的金钱。 给你整数 n、k、budget，下标从 1 开始的二维数组 composition，两个下标从 1 开始的数组 stock 和 cost，请你在预算不超过 budget 金钱的前提下，最大化 公司制造合金的数量。 所有合金都需要由同一台机器制造。 返回公司可以制造的最大合金数。 示例 1： 输入：n = 3, k = 2, budget = 15, composition = [[1,1,1],[1,1,10]], stock = [0,0,0], cost = [1,2,3] 输出：2 解释：最优的方法是使用第 1 台机器来制造合金。 要想制造 2 份合金，我们需要购买： - 2 份第 1 类金属。 - 2 份第 2 类金属。 - 2 份第 3 类金属。 总共需要 2 * 1 + 2 * 2 + 2 * 3 = 12 的金钱，小于等于预算 15 。 注意，我们最开始时候没有任何一类金属，所以必须买齐所有需要的金属。 可以证明在示例条件下最多可以制造 2 份合金。 示例 2： 输入：n = 3, k = 2, budget = 15, composition = [[1,1,1],[1,1,10]], stock = [0,0,100], cost = [1,2,3] 输出：5 解释：最优的方法是使用第 2 台机器来制造合金。 要想制造 5 份合金，我们需要购买： - 5 份第 1 类金属。 - 5 份第 2 类金属。 - 0 份第 3 类金属。 总共需要 5 * 1 + 5 * 2 + 0 * 3 = 15 的金钱，小于等于预算 15 。 可以证明在示例条件下最多可以制造 5 份合金。 示例 3： 输入：n = 2, k = 3, budget = 10, composition = [[2,1],[1,2],[1,1]], stock = [1,1], cost = [5,5] 输出：2 解释：最优的方法是使用第 3 台机器来制造合金。 要想制造 2 份合金，我们需要购买： - 1 份第 1 类金属。 - 1 份第 2 类金属。 总共需要 1 * 5 + 1 * 5 = 10 的金钱，小于等于预算 10 。 可以证明在示例条件下最多可以制造 2 份合金。 提示： * 1 <= n, k <= 100 * 0 <= budget <= 108 * composition.length == k * composition[i].length == n * 1 <= composition[i][j] <= 100 * stock.length == cost.length == n * 0 <= stock[i] <= 108 * 1 <= cost[i] <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找来确定每台机器可以制造的最大合金数。

算法步骤:
1. 定义一个辅助函数 `can_make` 来判断在给定的预算和库存下，能否制造出 `mid` 个合金。
2. 对于每台机器，使用二分查找来确定可以制造的最大合金数。
3. 返回所有机器中可以制造的最大合金数。

关键点:
- 使用二分查找来高效地找到最大合金数。
- 辅助函数 `can_make` 用于判断在当前预算和库存下能否制造出指定数量的合金。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(k * n * log(max_stock))，其中 k 是机器数量，n 是金属种类数，max_stock 是最大的库存量。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def can_make(composition: List[int], stock: List[int], cost: List[int], mid: int, budget: int) -> bool:
    total_cost = 0
    for i in range(len(composition)):
        needed = max(0, composition[i] * mid - stock[i])
        total_cost += needed * cost[i]
        if total_cost > budget:
            return False
    return True


def max_number_of_alloys(n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
    max_alloys = 0
    for i in range(k):
        left, right = 0, 10**9  # 二分查找的范围
        while left < right:
            mid = (left + right + 1) // 2
            if can_make(composition[i], stock, cost, mid, budget):
                left = mid
            else:
                right = mid - 1
        max_alloys = max(max_alloys, left)
    return max_alloys


Solution = create_solution(max_number_of_alloys)