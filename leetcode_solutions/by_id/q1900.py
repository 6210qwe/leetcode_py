# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1900
标题: Closest Dessert Cost
难度: medium
链接: https://leetcode.cn/problems/closest-dessert-cost/
题目类型: 数组、动态规划、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1774. 最接近目标价格的甜点成本 - 你打算做甜点，现在需要购买配料。目前共有 n 种冰激凌基料和 m 种配料可供选购。而制作甜点需要遵循以下几条规则： * 必须选择 一种 冰激凌基料。 * 可以添加 一种或多种 配料，也可以不添加任何配料。 * 每种类型的配料 最多两份 。 给你以下三个输入： * baseCosts ，一个长度为 n 的整数数组，其中每个 baseCosts[i] 表示第 i 种冰激凌基料的价格。 * toppingCosts，一个长度为 m 的整数数组，其中每个 toppingCosts[i] 表示 一份 第 i 种冰激凌配料的价格。 * target ，一个整数，表示你制作甜点的目标价格。 你希望自己做的甜点总成本尽可能接近目标价格 target 。 返回最接近 target 的甜点成本。如果有多种方案，返回 成本相对较低 的一种。 示例 1： 输入：baseCosts = [1,7], toppingCosts = [3,4], target = 10 输出：10 解释：考虑下面的方案组合（所有下标均从 0 开始）： - 选择 1 号基料：成本 7 - 选择 1 份 0 号配料：成本 1 x 3 = 3 - 选择 0 份 1 号配料：成本 0 x 4 = 0 总成本：7 + 3 + 0 = 10 。 示例 2： 输入：baseCosts = [2,3], toppingCosts = [4,5,100], target = 18 输出：17 解释：考虑下面的方案组合（所有下标均从 0 开始）： - 选择 1 号基料：成本 3 - 选择 1 份 0 号配料：成本 1 x 4 = 4 - 选择 2 份 1 号配料：成本 2 x 5 = 10 - 选择 0 份 2 号配料：成本 0 x 100 = 0 总成本：3 + 4 + 10 + 0 = 17 。不存在总成本为 18 的甜点制作方案。 示例 3： 输入：baseCosts = [3,10], toppingCosts = [2,5], target = 9 输出：8 解释：可以制作总成本为 8 和 10 的甜点。返回 8 ，因为这是成本更低的方案。 示例 4： 输入：baseCosts = [10], toppingCosts = [1], target = 1 输出：10 解释：注意，你可以选择不添加任何配料，但你必须选择一种基料。 提示： * n == baseCosts.length * m == toppingCosts.length * 1 <= n, m <= 10 * 1 <= baseCosts[i], toppingCosts[i] <= 104 * 1 <= target <= 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用回溯法生成所有可能的成本，并找到最接近目标价格的成本。

算法步骤:
1. 定义一个递归函数来生成所有可能的成本。
2. 对于每种基料，递归地添加配料的成本（0份、1份或2份）。
3. 记录所有生成的成本，并找到最接近目标价格的成本。

关键点:
- 使用回溯法生成所有可能的成本。
- 通过比较绝对差值找到最接近目标价格的成本。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(3^m * n)，其中 m 是配料的数量，n 是基料的数量。每种配料有 3 种选择（0份、1份或2份），总共需要遍历 n 种基料。
空间复杂度: O(3^m * n)，递归调用栈的深度最多为 m，且每种基料都会生成 3^m 个成本。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def closest_dessert_cost(base_costs: List[int], topping_costs: List[int], target: int) -> int:
    """
    函数式接口 - 实现最优解法
    """
    def backtrack(index: int, current_cost: int):
        nonlocal min_diff, result
        if index == len(topping_costs):
            diff = abs(current_cost - target)
            if diff < min_diff or (diff == min_diff and current_cost < result):
                min_diff = diff
                result = current_cost
            return
        # 不加当前配料
        backtrack(index + 1, current_cost)
        # 加一份当前配料
        backtrack(index + 1, current_cost + topping_costs[index])
        # 加两份当前配料
        backtrack(index + 1, current_cost + 2 * topping_costs[index])

    min_diff = float('inf')
    result = 0
    for base in base_costs:
        backtrack(0, base)
    
    return result


Solution = create_solution(closest_dessert_cost)