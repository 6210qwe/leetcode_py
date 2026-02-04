# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1642
标题: Water Bottles
难度: easy
链接: https://leetcode.cn/problems/water-bottles/
题目类型: 数学、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1518. 换水问题 - 超市正在促销，你可以用 numExchange 个空水瓶从超市兑换一瓶水。最开始，你一共购入了 numBottles 瓶水。 如果喝掉了水瓶中的水，那么水瓶就会变成空的。 给你两个整数 numBottles 和 numExchange ，返回你 最多 可以喝到多少瓶水。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/07/19/sample_1_1875.png] 输入：numBottles = 9, numExchange = 3 输出：13 解释：你可以用 3 个空瓶兑换 1 瓶水。 所以最多能喝到 9 + 3 + 1 = 13 瓶水。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/07/19/sample_2_1875.png] 输入：numBottles = 15, numExchange = 4 输出：19 解释：你可以用 4 个空瓶兑换 1 瓶水。 所以最多能喝到 15 + 3 + 1 = 19 瓶水。 提示： * 1 <= numBottles <= 100 * 2 <= numExchange <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过循环不断计算可以兑换的新瓶子数量，并累加到总瓶子数量中。

算法步骤:
1. 初始化总瓶子数量 total_bottles 为 numBottles。
2. 初始化当前空瓶子数量 empty_bottles 为 numBottles。
3. 当空瓶子数量大于等于 numExchange 时，继续循环：
   - 计算可以兑换的新瓶子数量 new_bottles。
   - 更新总瓶子数量 total_bottles。
   - 更新空瓶子数量 empty_bottles 为 (empty_bottles - numExchange) + new_bottles。
4. 返回总瓶子数量 total_bottles。

关键点:
- 循环条件是空瓶子数量大于等于 numExchange。
- 每次兑换后更新空瓶子数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log(numBottles)) - 每次循环中空瓶子数量都会减少。
空间复杂度: O(1) - 使用常数级额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(numBottles: int, numExchange: int) -> int:
    """
    函数式接口 - 计算最多可以喝到多少瓶水
    """
    total_bottles = numBottles
    empty_bottles = numBottles

    while empty_bottles >= numExchange:
        new_bottles = empty_bottles // numExchange
        total_bottles += new_bottles
        empty_bottles = (empty_bottles % numExchange) + new_bottles

    return total_bottles


Solution = create_solution(solution_function_name)