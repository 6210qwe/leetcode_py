# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3336
标题: Water Bottles II
难度: medium
链接: https://leetcode.cn/problems/water-bottles-ii/
题目类型: 数学、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3100. 换水问题 II - 给你两个整数 numBottles 和 numExchange 。 numBottles 代表你最初拥有的满水瓶数量。在一次操作中，你可以执行以下操作之一： * 喝掉任意数量的满水瓶，使它们变成空水瓶。 * 用 numExchange 个空水瓶交换一个满水瓶。然后，将 numExchange 的值增加 1 。 注意，你不能使用相同的 numExchange 值交换多批空水瓶。例如，如果 numBottles == 3 并且 numExchange == 1 ，则不能用 3 个空水瓶交换成 3 个满水瓶。 返回你 最多 可以喝到多少瓶水。 示例 1： [https://assets.leetcode.com/uploads/2024/01/28/exampleone1.png] 输入：numBottles = 13, numExchange = 6 输出：15 解释：上表显示了满水瓶的数量、空水瓶的数量、numExchange 的值，以及累计喝掉的水瓶数量。 示例 2： [https://assets.leetcode.com/uploads/2024/01/28/example231.png] 输入：numBottles = 10, numExchange = 3 输出：13 解释：上表显示了满水瓶的数量、空水瓶的数量、numExchange 的值，以及累计喝掉的水瓶数量。 提示： * 1 <= numBottles <= 100 * 1 <= numExchange <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过不断喝掉满水瓶并用空水瓶交换新的满水瓶来最大化喝到的水瓶数量。

算法步骤:
1. 初始化喝掉的水瓶数量和空水瓶数量。
2. 当有足够的空水瓶可以交换时，进行交换并将空水瓶数量减少，同时增加满水瓶数量。
3. 将新获得的满水瓶喝掉，并更新空水瓶数量。
4. 重复步骤2和3，直到没有足够的空水瓶可以交换为止。

关键点:
- 每次交换后，numExchange 会增加 1。
- 只有当空水瓶数量大于等于 numExchange 时，才能进行交换。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(numBottles) - 最坏情况下，每次交换只能得到一个新的满水瓶，最多需要进行 numBottles 次交换。
空间复杂度: O(1) - 只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_water_bottles(num_bottles: int, num_exchange: int) -> int:
    """
    函数式接口 - 计算最多可以喝到多少瓶水
    """
    total_drunk = num_bottles  # 初始喝掉的水瓶数量
    empty_bottles = num_bottles  # 初始空水瓶数量

    while empty_bottles >= num_exchange:
        new_full_bottles = empty_bottles // num_exchange
        total_drunk += new_full_bottles
        empty_bottles = empty_bottles % num_exchange + new_full_bottles
        num_exchange += 1

    return total_drunk


Solution = create_solution(max_water_bottles)