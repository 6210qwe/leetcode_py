# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3026
标题: Find the Minimum Possible Sum of a Beautiful Array
难度: medium
链接: https://leetcode.cn/problems/find-the-minimum-possible-sum-of-a-beautiful-array/
题目类型: 贪心、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2834. 找出美丽数组的最小和 - 给你两个正整数：n 和 target 。 如果数组 nums 满足下述条件，则称其为 美丽数组 。 * nums.length == n. * nums 由两两互不相同的正整数组成。 * 在范围 [0, n-1] 内，不存在 两个 不同 下标 i 和 j ，使得 nums[i] + nums[j] == target 。 返回符合条件的美丽数组所可能具备的 最小 和，并对结果进行取模 109 + 7。 示例 1： 输入：n = 2, target = 3 输出：4 解释：nums = [1,3] 是美丽数组。 - nums 的长度为 n = 2 。 - nums 由两两互不相同的正整数组成。 - 不存在两个不同下标 i 和 j ，使得 nums[i] + nums[j] == 3 。 可以证明 4 是符合条件的美丽数组所可能具备的最小和。 示例 2： 输入：n = 3, target = 3 输出：8 解释： nums = [1,3,4] 是美丽数组。 - nums 的长度为 n = 3 。 - nums 由两两互不相同的正整数组成。 - 不存在两个不同下标 i 和 j ，使得 nums[i] + nums[j] == 3 。 可以证明 8 是符合条件的美丽数组所可能具备的最小和。 示例 3： 输入：n = 1, target = 1 输出：1 解释：nums = [1] 是美丽数组。 提示： * 1 <= n <= 109 * 1 <= target <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，选择尽可能小的数来构建美丽数组。

算法步骤:
1. 计算可以使用的最大数 `max_num`，即 `target // 2`。
2. 从 1 开始，依次选择不超过 `max_num` 的数，直到选择了 `min(n, max_num)` 个数。
3. 如果还需要更多的数，则从 `target` 开始，依次选择更大的数，直到选择了 `n` 个数。
4. 计算这些数的总和，并对结果进行取模 109 + 7。

关键点:
- 通过选择尽可能小的数来构建美丽数组，确保总和最小。
- 使用取模操作防止结果溢出。
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


def find_min_beautiful_array_sum(n: int, target: int) -> int:
    """
    函数式接口 - 找出美丽数组的最小和
    """
    MOD = 10**9 + 7
    max_num = min(n, (target - 1) // 2)
    sum_first_part = (1 + max_num) * max_num // 2
    remaining = n - max_num
    start = target
    sum_second_part = (start + (start + remaining - 1)) * remaining // 2 if remaining > 0 else 0
    total_sum = (sum_first_part + sum_second_part) % MOD
    return total_sum


Solution = create_solution(find_min_beautiful_array_sum)