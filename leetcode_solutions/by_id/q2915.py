# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2915
标题: Count of Interesting Subarrays
难度: medium
链接: https://leetcode.cn/problems/count-of-interesting-subarrays/
题目类型: 数组、哈希表、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2845. 统计趣味子数组的数目 - 给你一个下标从 0 开始的整数数组 nums ，以及整数 modulo 和整数 k 。 请你找出并统计数组中 趣味子数组 的数目。 如果 子数组 nums[l..r] 满足下述条件，则称其为 趣味子数组 ： * 在范围 [l, r] 内，设 cnt 为满足 nums[i] % modulo == k 的索引 i 的数量。并且 cnt % modulo == k 。 以整数形式表示并返回趣味子数组的数目。 注意：子数组是数组中的一个连续非空的元素序列。 示例 1： 输入：nums = [3,2,4], modulo = 2, k = 1 输出：3 解释：在这个示例中，趣味子数组分别是： 子数组 nums[0..0] ，也就是 [3] 。 - 在范围 [0, 0] 内，只存在 1 个下标 i = 0 满足 nums[i] % modulo == k 。 - 因此 cnt = 1 ，且 cnt % modulo == k 。 子数组 nums[0..1] ，也就是 [3,2] 。 - 在范围 [0, 1] 内，只存在 1 个下标 i = 0 满足 nums[i] % modulo == k 。 - 因此 cnt = 1 ，且 cnt % modulo == k 。 子数组 nums[0..2] ，也就是 [3,2,4] 。 - 在范围 [0, 2] 内，只存在 1 个下标 i = 0 满足 nums[i] % modulo == k 。 - 因此 cnt = 1 ，且 cnt % modulo == k 。 可以证明不存在其他趣味子数组。因此，答案为 3 。 示例 2： 输入：nums = [3,1,9,6], modulo = 3, k = 0 输出：2 解释：在这个示例中，趣味子数组分别是： 子数组 nums[0..3] ，也就是 [3,1,9,6] 。 - 在范围 [0, 3] 内，只存在 3 个下标 i = 0, 2, 3 满足 nums[i] % modulo == k 。 - 因此 cnt = 3 ，且 cnt % modulo == k 。 子数组 nums[1..1] ，也就是 [1] 。 - 在范围 [1, 1] 内，不存在下标满足 nums[i] % modulo == k 。 - 因此 cnt = 0 ，且 cnt % modulo == k 。 可以证明不存在其他趣味子数组，因此答案为 2 。 提示： * 1 <= nums.length <= 105 * 1 <= nums[i] <= 109 * 1 <= modulo <= 109 * 0 <= k < modulo
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和与哈希表来统计满足条件的子数组数量。

算法步骤:
1. 初始化前缀和数组 `prefix_sum` 和哈希表 `count_map`。
2. 遍历数组 `nums`，更新前缀和数组 `prefix_sum`。
3. 对于每个前缀和 `prefix_sum[i]`，计算 `(prefix_sum[i] - k) % modulo`，并在哈希表中查找该值出现的次数。
4. 更新哈希表 `count_map` 中 `prefix_sum[i] % modulo` 的出现次数。
5. 最终结果为哈希表中所有值的总和。

关键点:
- 使用前缀和和哈希表来高效地统计满足条件的子数组数量。
- 通过 `(prefix_sum[i] - k) % modulo` 来找到满足条件的前缀和。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组 `nums` 的长度。我们只需要遍历数组一次。
空间复杂度: O(min(n, modulo))，哈希表的大小最多为 `modulo`。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_interesting_subarrays(nums: List[int], modulo: int, k: int) -> int:
    """
    函数式接口 - 统计趣味子数组的数目
    """
    prefix_sum = 0
    count_map = {0: 1}
    result = 0

    for num in nums:
        if num % modulo == k:
            prefix_sum += 1
        target = (prefix_sum - k) % modulo
        result += count_map.get(target, 0)
        count_map[prefix_sum % modulo] = count_map.get(prefix_sum % modulo, 0) + 1

    return result


Solution = create_solution(count_interesting_subarrays)