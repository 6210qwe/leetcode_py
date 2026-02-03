# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 876
标题: Hand of Straights
难度: medium
链接: https://leetcode.cn/problems/hand-of-straights/
题目类型: 贪心、数组、哈希表、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
846. 一手顺子 - Alice 手中有一把牌，她想要重新排列这些牌，分成若干组，使每一组的牌数都是 groupSize ，并且由 groupSize 张连续的牌组成。 给你一个整数数组 hand 其中 hand[i] 是写在第 i 张牌上的数值。如果她可能重新排列这些牌，返回 true ；否则，返回 false 。 示例 1： 输入：hand = [1,2,3,6,2,3,4,7,8], groupSize = 3 输出：true 解释：Alice 手中的牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。 示例 2： 输入：hand = [1,2,3,4,5], groupSize = 4 输出：false 解释：Alice 手中的牌无法被重新排列成几个大小为 4 的组。 提示： * 1 <= hand.length <= 104 * 0 <= hand[i] <= 109 * 1 <= groupSize <= hand.length 注意：此题目与 1296 重复：https://leetcode.cn/problems/divide-array-in-sets-of-k-consecutive-numbers/ [https://leetcode.cn/problems/divide-array-in-sets-of-k-consecutive-numbers/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
