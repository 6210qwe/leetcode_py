# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3327
标题: Minimum Moves to Pick K Ones
难度: hard
链接: https://leetcode.cn/problems/minimum-moves-to-pick-k-ones/
题目类型: 贪心、数组、前缀和、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3086. 拾起 K 个 1 需要的最少行动次数 - 给你一个下标从 0 开始的二进制数组 nums，其长度为 n ；另给你一个 正整数 k 以及一个 非负整数 maxChanges 。 Alice 在玩一个游戏，游戏的目标是让 Alice 使用 最少 数量的 行动 次数从 nums 中拾起 k 个 1 。游戏开始时，Alice 可以选择数组 [0, n - 1] 范围内的任何索引 aliceIndex 站立。如果 nums[aliceIndex] == 1 ，Alice 会拾起一个 1 ，并且 nums[aliceIndex] 变成0（这 不算 作一次行动）。之后，Alice 可以执行 任意数量 的 行动（包括零次），在每次行动中 Alice 必须 恰好 执行以下动作之一： * 选择任意一个下标 j != aliceIndex 且满足 nums[j] == 0 ，然后将 nums[j] 设置为 1 。这个动作最多可以执行 maxChanges 次。 * 选择任意两个相邻的下标 x 和 y（|x - y| == 1）且满足 nums[x] == 1, nums[y] == 0 ，然后交换它们的值（将 nums[y] = 1 和 nums[x] = 0）。如果 y == aliceIndex，在这次行动后 Alice 拾起一个 1 ，并且 nums[y] 变成 0 。 返回 Alice 拾起 恰好 k 个 1 所需的 最少 行动次数。 示例 1： 输入：nums = [1,1,0,0,0,1,1,0,0,1], k = 3, maxChanges = 1 输出：3 解释：如果游戏开始时 Alice 在 aliceIndex == 1 的位置上，按照以下步骤执行每个动作，他可以利用 3 次行动拾取 3 个 1 ： * 游戏开始时 Alice 拾取了一个 1 ，nums[1] 变成了 0。此时 nums 变为 [1,0,0,0,0,1,1,0,0,1] 。 * 选择 j == 2 并执行第一种类型的动作。nums 变为 [1,0,1,0,0,1,1,0,0,1] * 选择 x == 2 和 y == 1 ，并执行第二种类型的动作。nums 变为 [1,1,0,0,0,1,1,0,0,1] 。由于 y == aliceIndex，Alice 拾取了一个 1 ，nums 变为 [1,0,0,0,0,1,1,0,0,1] 。 * 选择 x == 0 和 y == 1 ，并执行第二种类型的动作。nums 变为 [0,1,0,0,0,1,1,0,0,1] 。由于 y == aliceIndex，Alice 拾取了一个 1 ，nums 变为 [0,0,0,0,0,1,1,0,0,1] 。 请注意，Alice 也可能执行其他的 3 次行动序列达成拾取 3 个 1 。 示例 2： 输入：nums = [0,0,0,0], k = 2, maxChanges = 3 输出：4 解释：如果游戏开始时 Alice 在 aliceIndex == 0 的位置上，按照以下步骤执行每个动作，他可以利用 4 次行动拾取 2 个 1 ： * 选择 j == 1 并执行第一种类型的动作。nums 变为 [0,1,0,0] 。 * 选择 x == 1 和 y == 0 ，并执行第二种类型的动作。nums 变为 [1,0,0,0] 。由于 y == aliceIndex，Alice 拾起了一个 1 ，nums 变为 [0,0,0,0] 。 * 再次选择 j == 1 并执行第一种类型的动作。nums 变为 [0,1,0,0] 。 * 再次选择 x == 1 和 y == 0 ，并执行第二种类型的动作。nums 变为 [1,0,0,0] 。由于y == aliceIndex，Alice 拾起了一个 1 ，nums 变为 [0,0,0,0] 。 提示： * 2 <= n <= 105 * 0 <= nums[i] <= 1 * 1 <= k <= 105 * 0 <= maxChanges <= 105 * maxChanges + sum(nums) >= k
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口来找到最优的子数组，使得在该子数组中拾起 k 个 1 的操作次数最少。

算法步骤:
1. 计算前缀和数组 `prefix_sum`，其中 `prefix_sum[i]` 表示 `nums` 前 i 个元素的 1 的个数。
2. 初始化滑动窗口的左右边界 `left` 和 `right`，以及当前窗口内 1 的个数 `current_ones`。
3. 移动右边界 `right`，更新 `current_ones` 和 `prefix_sum`。
4. 如果 `current_ones` 大于等于 k，则移动左边界 `left`，更新 `current_ones` 和 `prefix_sum`。
5. 计算当前窗口内的操作次数，并更新最小操作次数。
6. 返回最小操作次数。

关键点:
- 使用前缀和数组来快速计算窗口内的 1 的个数。
- 使用滑动窗口来找到最优的子数组。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 nums 的长度。滑动窗口遍历数组一次。
空间复杂度: O(n)，存储前缀和数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def min_moves_to_pick_k_ones(nums: List[int], k: int, max_changes: int) -> int:
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    
    left = 0
    right = 0
    current_ones = 0
    min_operations = float('inf')
    
    while right < n:
        if nums[right] == 1:
            current_ones += 1
        
        while current_ones >= k:
            window_size = right - left + 1
            ones_in_window = prefix_sum[right + 1] - prefix_sum[left]
            zeros_in_window = window_size - ones_in_window
            operations = zeros_in_window - max_changes
            
            if operations < 0:
                operations = 0
            
            min_operations = min(min_operations, operations)
            
            if nums[left] == 1:
                current_ones -= 1
            left += 1
        
        right += 1
    
    return min_operations

Solution = create_solution(min_moves_to_pick_k_ones)