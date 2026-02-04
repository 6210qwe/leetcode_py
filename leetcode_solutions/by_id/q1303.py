# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1303
标题: Minimum Moves to Reach Target Score
难度: medium
链接: https://leetcode.cn/problems/minimum-moves-to-reach-target-score/
题目类型: 贪心、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2139. 得到目标值的最少行动次数 - 你正在玩一个整数游戏。从整数 1 开始，期望得到整数 target 。 在一次行动中，你可以做下述两种操作之一： * 递增，将当前整数的值加 1（即， x = x + 1）。 * 加倍，使当前整数的值翻倍（即，x = 2 * x）。 在整个游戏过程中，你可以使用 递增 操作 任意 次数。但是只能使用 加倍 操作 至多 maxDoubles 次。 给你两个整数 target 和 maxDoubles ，返回从 1 开始得到 target 需要的最少行动次数。 示例 1： 输入：target = 5, maxDoubles = 0 输出：4 解释：一直递增 1 直到得到 target 。 示例 2： 输入：target = 19, maxDoubles = 2 输出：7 解释：最初，x = 1 。 递增 3 次，x = 4 。 加倍 1 次，x = 8 。 递增 1 次，x = 9 。 加倍 1 次，x = 18 。 递增 1 次，x = 19 。 示例 3： 输入：target = 10, maxDoubles = 4 输出：4 解释： 最初，x = 1 。 递增 1 次，x = 2 。 加倍 1 次，x = 4 。 递增 1 次，x = 5 。 加倍 1 次，x = 10 。 提示： * 1 <= target <= 109 * 0 <= maxDoubles <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 从 target 反向推导到 1，优先使用加倍操作，如果不能加倍则使用递增操作。

算法步骤:
1. 初始化步数为 0。
2. 当 target 大于 1 时：
   - 如果 maxDoubles > 0 且 target 是偶数，则使用加倍操作，target 减半，maxDoubles 减 1。
   - 否则，使用递增操作，target 减 1。
3. 返回步数。

关键点:
- 优先使用加倍操作，因为它能更快地减少 target 的值。
- 当 target 为奇数时，只能使用递增操作。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log(target))，因为每次加倍操作都会将 target 减半。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_moves_to_reach_target_score(target: int, maxDoubles: int) -> int:
    """
    函数式接口 - 计算从 1 到 target 所需的最少行动次数
    """
    steps = 0
    while target > 1:
        if maxDoubles > 0 and target % 2 == 0:
            target //= 2
            maxDoubles -= 1
        else:
            target -= 1
        steps += 1
    return steps


Solution = create_solution(min_moves_to_reach_target_score)