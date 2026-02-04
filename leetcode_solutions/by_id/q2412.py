# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2412
标题: Minimum Amount of Time to Fill Cups
难度: easy
链接: https://leetcode.cn/problems/minimum-amount-of-time-to-fill-cups/
题目类型: 贪心、数组、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2335. 装满杯子需要的最短总时长 - 现有一台饮水机，可以制备冷水、温水和热水。每秒钟，可以装满 2 杯 不同 类型的水或者 1 杯任意类型的水。 给你一个下标从 0 开始、长度为 3 的整数数组 amount ，其中 amount[0]、amount[1] 和 amount[2] 分别表示需要装满冷水、温水和热水的杯子数量。返回装满所有杯子所需的 最少 秒数。 示例 1： 输入：amount = [1,4,2] 输出：4 解释：下面给出一种方案： 第 1 秒：装满一杯冷水和一杯温水。 第 2 秒：装满一杯温水和一杯热水。 第 3 秒：装满一杯温水和一杯热水。 第 4 秒：装满一杯温水。 可以证明最少需要 4 秒才能装满所有杯子。 示例 2： 输入：amount = [5,4,4] 输出：7 解释：下面给出一种方案： 第 1 秒：装满一杯冷水和一杯热水。 第 2 秒：装满一杯冷水和一杯温水。 第 3 秒：装满一杯冷水和一杯温水。 第 4 秒：装满一杯温水和一杯热水。 第 5 秒：装满一杯冷水和一杯热水。 第 6 秒：装满一杯冷水和一杯温水。 第 7 秒：装满一杯热水。 示例 3： 输入：amount = [5,0,0] 输出：5 解释：每秒装满一杯冷水。 提示： * amount.length == 3 * 0 <= amount[i] <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，每次尽可能多地同时装满两杯不同类型的水。

算法步骤:
1. 对数组进行排序，找到最大值 max_amount。
2. 计算剩余的总杯数 total_remaining = amount[1] + amount[2]。
3. 如果 max_amount 大于等于 total_remaining，那么所需时间就是 max_amount。
4. 否则，所需时间是 (total_remaining + 1) // 2 + max_amount - total_remaining。

关键点:
- 每次尽可能多地同时装满两杯不同类型的水。
- 使用贪心算法确保最小化总时间。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def minimum_time_to_fill_cups(amount: List[int]) -> int:
    """
    函数式接口 - 返回装满所有杯子所需的最少秒数
    """
    # 对数组进行排序
    amount.sort()
    
    # 找到最大值
    max_amount = amount[2]
    
    # 计算剩余的总杯数
    total_remaining = amount[0] + amount[1]
    
    # 如果 max_amount 大于等于 total_remaining，那么所需时间就是 max_amount
    if max_amount >= total_remaining:
        return max_amount
    else:
        # 否则，所需时间是 (total_remaining + 1) // 2 + max_amount - total_remaining
        return (total_remaining + 1) // 2 + max_amount - total_remaining


Solution = create_solution(minimum_time_to_fill_cups)