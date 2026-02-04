# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2417
标题: The Latest Time to Catch a Bus
难度: medium
链接: https://leetcode.cn/problems/the-latest-time-to-catch-a-bus/
题目类型: 数组、双指针、二分查找、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2332. 坐上公交的最晚时间 - 给你一个下标从 0 开始长度为 n 的整数数组 buses ，其中 buses[i] 表示第 i 辆公交车的出发时间。同时给你一个下标从 0 开始长度为 m 的整数数组 passengers ，其中 passengers[j] 表示第 j 位乘客的到达时间。所有公交车出发的时间互不相同，所有乘客到达的时间也互不相同。 给你一个整数 capacity ，表示每辆公交车 最多 能容纳的乘客数目。 每位乘客都会排队搭乘下一辆有座位的公交车。如果你在 y 时刻到达，公交在 x 时刻出发，满足 y <= x 且公交没有满，那么你可以搭乘这一辆公交。最早 到达的乘客优先上车。 返回你可以搭乘公交车的最晚到达公交站时间。你 不能 跟别的乘客同时刻到达。 注意：数组 buses 和 passengers 不一定是有序的。 示例 1： 输入：buses = [10,20], passengers = [2,17,18,19], capacity = 2 输出：16 解释： 第 1 辆公交车载着第 1 位乘客。 第 2 辆公交车载着你和第 2 位乘客。 注意你不能跟其他乘客同一时间到达，所以你必须在第二位乘客之前到达。 示例 2： 输入：buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2 输出：20 解释： 第 1 辆公交车载着第 4 位乘客。 第 2 辆公交车载着第 6 位和第 2 位乘客。 第 3 辆公交车载着第 1 位乘客和你。 提示： * n == buses.length * m == passengers.length * 1 <= n, m, capacity <= 105 * 2 <= buses[i], passengers[i] <= 109 * buses 中的元素 互不相同 。 * passengers 中的元素 互不相同 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 先对 buses 和 passengers 进行排序，然后使用双指针模拟乘客上车过程，找到可以搭乘公交车的最晚到达时间。

算法步骤:
1. 对 buses 和 passengers 进行排序。
2. 使用双指针遍历 buses 和 passengers，模拟乘客上车过程。
3. 记录每辆公交车上的乘客，并检查是否还有空位。
4. 如果最后一辆公交车还有空位，找到可以搭乘的最晚时间。

关键点:
- 排序后使用双指针模拟乘客上车过程。
- 处理最后一辆公交车时，找到可以搭乘的最晚时间。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n + m log m)，其中 n 是 buses 的长度，m 是 passengers 的长度。排序操作的时间复杂度是 O(n log n) 和 O(m log m)，双指针遍历的时间复杂度是 O(n + m)。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def latest_time_to_catch_bus(buses: List[int], passengers: List[int], capacity: int) -> int:
    """
    返回你可以搭乘公交车的最晚到达公交站时间。
    """
    # 对 buses 和 passengers 进行排序
    buses.sort()
    passengers.sort()

    # 初始化指针
    bus_index = 0
    passenger_index = 0

    # 用于记录已经上车的乘客
    on_bus = set()

    while bus_index < len(buses):
        count = 0
        while count < capacity and passenger_index < len(passengers) and passengers[passenger_index] <= buses[bus_index]:
            if passengers[passenger_index] not in on_bus:
                on_bus.add(passengers[passenger_index])
                count += 1
            passenger_index += 1

        bus_index += 1

    # 找到可以搭乘的最晚时间
    last_time = buses[-1]
    while last_time in on_bus or last_time in passengers:
        last_time -= 1

    return last_time


Solution = create_solution(latest_time_to_catch_bus)