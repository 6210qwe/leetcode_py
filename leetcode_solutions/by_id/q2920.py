# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2920
标题: Minimum Seconds to Equalize a Circular Array
难度: medium
链接: https://leetcode.cn/problems/minimum-seconds-to-equalize-a-circular-array/
题目类型: 数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2808. 使循环数组所有元素相等的最少秒数 - 给你一个下标从 0 开始长度为 n 的数组 nums 。 每一秒，你可以对数组执行以下操作： * 对于范围在 [0, n - 1] 内的每一个下标 i ，将 nums[i] 替换成 nums[i] ，nums[(i - 1 + n) % n] 或者 nums[(i + 1) % n] 三者之一。 注意，所有元素会被同时替换。 请你返回将数组 nums 中所有元素变成相等元素所需要的 最少 秒数。 示例 1： 输入：nums = [1,2,1,2] 输出：1 解释：我们可以在 1 秒内将数组变成相等元素： - 第 1 秒，将每个位置的元素分别变为 [nums[3],nums[1],nums[3],nums[3]] 。变化后，nums = [2,2,2,2] 。 1 秒是将数组变成相等元素所需要的最少秒数。 示例 2： 输入：nums = [2,1,3,3,2] 输出：2 解释：我们可以在 2 秒内将数组变成相等元素： - 第 1 秒，将每个位置的元素分别变为 [nums[0],nums[2],nums[2],nums[2],nums[3]] 。变化后，nums = [2,3,3,3,3] 。 - 第 2 秒，将每个位置的元素分别变为 [nums[1],nums[1],nums[2],nums[3],nums[4]] 。变化后，nums = [3,3,3,3,3] 。 2 秒是将数组变成相等元素所需要的最少秒数。 示例 3： 输入：nums = [5,5,5,5] 输出：0 解释：不需要执行任何操作，因为一开始数组中的元素已经全部相等。 提示： * 1 <= n == nums.length <= 105 * 1 <= nums[i] <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表记录每个元素的位置，然后计算每个元素扩散到整个数组所需的最短时间。

算法步骤:
1. 使用哈希表记录每个元素的所有出现位置。
2. 对于每个元素，计算其相邻两个位置之间的最大间隔，并更新最小时间。
3. 返回最小时间。

关键点:
- 计算每个元素相邻位置之间的最大间隔。
- 处理循环数组的边界情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def minimum_seconds_to_equalize(nums: List[int]) -> int:
    """
    函数式接口 - 返回将数组 nums 中所有元素变成相等元素所需要的最少秒数
    """
    from collections import defaultdict

    # 记录每个元素的所有出现位置
    positions = defaultdict(list)
    for i, num in enumerate(nums):
        positions[num].append(i)

    n = len(nums)
    min_time = float('inf')

    for pos in positions.values():
        if len(pos) == 1:
            continue
        max_gap = max((pos[i] - pos[i - 1]) // 2 for i in range(1, len(pos)))
        max_gap = max(max_gap, (n - (pos[-1] - pos[0])) // 2)
        min_time = min(min_time, max_gap)

    return min_time if min_time != float('inf') else 0


Solution = create_solution(minimum_seconds_to_equalize)