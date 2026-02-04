# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2893
标题: Visit Array Positions to Maximize Score
难度: medium
链接: https://leetcode.cn/problems/visit-array-positions-to-maximize-score/
题目类型: 数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2786. 访问数组中的位置使分数最大 - 给你一个下标从 0 开始的整数数组 nums 和一个正整数 x 。 你 一开始 在数组的位置 0 处，你可以按照下述规则访问数组中的其他位置： * 如果你当前在位置 i ，那么你可以移动到满足 i < j 的 任意 位置 j 。 * 对于你访问的位置 i ，你可以获得分数 nums[i] 。 * 如果你从位置 i 移动到位置 j 且 nums[i] 和 nums[j] 的 奇偶性 不同，那么你将失去分数 x 。 请你返回你能得到的 最大 得分之和。 注意 ，你一开始的分数为 nums[0] 。 示例 1： 输入：nums = [2,3,6,1,9,2], x = 5 输出：13 解释：我们可以按顺序访问数组中的位置：0 -> 2 -> 3 -> 4 。 对应位置的值为 2 ，6 ，1 和 9 。因为 6 和 1 的奇偶性不同，所以下标从 2 -> 3 让你失去 x = 5 分。 总得分为：2 + 6 + 1 + 9 - 5 = 13 。 示例 2： 输入：nums = [2,4,6,8], x = 3 输出：20 解释：数组中的所有元素奇偶性都一样，所以我们可以将每个元素都访问一次，而且不会失去任何分数。 总得分为：2 + 4 + 6 + 8 = 20 。 提示： * 2 <= nums.length <= 105 * 1 <= nums[i], x <= 106
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们维护两个变量 `even_score` 和 `odd_score`，分别表示当前在偶数位置和奇数位置的最大得分。

算法步骤:
1. 初始化 `even_score` 和 `odd_score` 为负无穷大。
2. 如果 `nums[0]` 是偶数，则 `even_score = nums[0]`，否则 `odd_score = nums[0]`。
3. 遍历数组 `nums`，对于每个位置 `i`：
   - 如果 `nums[i]` 是偶数，更新 `even_score` 为 `max(even_score + nums[i], odd_score + nums[i] - x)`。
   - 如果 `nums[i]` 是奇数，更新 `odd_score` 为 `max(odd_score + nums[i], even_score + nums[i] - x)`。
4. 返回 `max(even_score, odd_score)`。

关键点:
- 动态规划的状态转移方程依赖于当前元素的奇偶性和前一个状态的奇偶性。
- 通过维护两个变量来简化状态空间，避免使用二维数组。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组 `nums` 的长度。我们只需要遍历数组一次。
空间复杂度: O(1)，我们只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(nums: List[int], x: int) -> int:
    """
    函数式接口 - 实现最优解法
    """
    even_score = float('-inf')
    odd_score = float('-inf')

    if nums[0] % 2 == 0:
        even_score = nums[0]
    else:
        odd_score = nums[0]

    for i in range(1, len(nums)):
        if nums[i] % 2 == 0:
            even_score = max(even_score + nums[i], odd_score + nums[i] - x)
        else:
            odd_score = max(odd_score + nums[i], even_score + nums[i] - x)

    return max(even_score, odd_score)


Solution = create_solution(solution_function_name)