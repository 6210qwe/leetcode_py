# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3220
标题: Count Tested Devices After Test Operations
难度: easy
链接: https://leetcode.cn/problems/count-tested-devices-after-test-operations/
题目类型: 数组、计数、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2960. 统计已测试设备 - 给你一个长度为 n 、下标从 0 开始的整数数组 batteryPercentages ，表示 n 个设备的电池百分比。 你的任务是按照顺序测试每个设备 i，执行以下测试操作： * 如果 batteryPercentages[i] 大于 0： * 增加 已测试设备的计数。 * 将下标 j 在 [i + 1, n - 1] 的所有设备的电池百分比减少 1，确保它们的电池百分比 不会低于 0 ，即 batteryPercentages[j] = max(0, batteryPercentages[j] - 1)。 * 移动到下一个设备。 * 否则，移动到下一个设备而不执行任何测试。 返回一个整数，表示按顺序执行测试操作后 已测试设备 的数量。 示例 1： 输入：batteryPercentages = [1,1,2,1,3] 输出：3 解释：按顺序从设备 0 开始执行测试操作： 在设备 0 上，batteryPercentages[0] > 0 ，现在有 1 个已测试设备，batteryPercentages 变为 [1,0,1,0,2] 。 在设备 1 上，batteryPercentages[1] == 0 ，移动到下一个设备而不进行测试。 在设备 2 上，batteryPercentages[2] > 0 ，现在有 2 个已测试设备，batteryPercentages 变为 [1,0,1,0,1] 。 在设备 3 上，batteryPercentages[3] == 0 ，移动到下一个设备而不进行测试。 在设备 4 上，batteryPercentages[4] > 0 ，现在有 3 个已测试设备，batteryPercentages 保持不变。 因此，答案是 3 。 示例 2： 输入：batteryPercentages = [0,1,2] 输出：2 解释：按顺序从设备 0 开始执行测试操作： 在设备 0 上，batteryPercentages[0] == 0 ，移动到下一个设备而不进行测试。 在设备 1 上，batteryPercentages[1] > 0 ，现在有 1 个已测试设备，batteryPercentages 变为 [0,1,1] 。 在设备 2 上，batteryPercentages[2] > 0 ，现在有 2 个已测试设备，batteryPercentages 保持不变。 因此，答案是 2 。 提示： * 1 <= n == batteryPercentages.length <= 100 * 0 <= batteryPercentages[i] <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过一次遍历数组来模拟测试过程，对于每个电池百分比大于0的设备，增加已测试设备的计数，并将后续设备的电池百分比减1。

算法步骤:
1. 初始化已测试设备的计数器 `tested_count` 为 0。
2. 遍历数组 `batteryPercentages`，对于每个元素：
   - 如果当前设备的电池百分比大于0，则增加 `tested_count`。
   - 将后续设备的电池百分比减1，但确保不低于0。
3. 返回 `tested_count`。

关键点:
- 通过一次遍历完成所有操作，时间复杂度为 O(n^2)，但由于 n 最大为 100，可以接受。
- 空间复杂度为 O(1)，因为只使用了常数级的额外空间。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_tested_devices(battery_percentages: List[int]) -> int:
    """
    函数式接口 - 统计已测试设备的数量
    """
    tested_count = 0
    n = len(battery_percentages)
    
    for i in range(n):
        if battery_percentages[i] > 0:
            tested_count += 1
            for j in range(i + 1, n):
                battery_percentages[j] = max(0, battery_percentages[j] - 1)
    
    return tested_count


Solution = create_solution(count_tested_devices)