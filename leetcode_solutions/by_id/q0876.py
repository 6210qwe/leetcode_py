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
核心思想: 使用计数器和贪心算法来检查是否可以将手牌分成连续的组。

算法步骤:
1. 检查 `hand` 的长度是否是 `groupSize` 的倍数，如果不是，直接返回 `False`。
2. 使用 `Counter` 统计每张牌的数量。
3. 对 `hand` 进行排序。
4. 遍历排序后的 `hand`，对于每个牌，如果它在计数器中的数量大于 0，则尝试构建一个长度为 `groupSize` 的连续序列。
5. 如果在构建过程中发现某个牌的数量不足，则返回 `False`。
6. 如果成功构建所有组，返回 `True`。

关键点:
- 使用 `Counter` 来高效统计每张牌的数量。
- 通过排序和贪心算法来确保每次选择最小的牌开始构建连续序列。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 `hand` 的长度。排序操作的时间复杂度是 O(n log n)，遍历操作是 O(n)。
空间复杂度: O(n)，用于存储计数器。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import Counter

def is_n_straight_hand(hand: List[int], group_size: int) -> bool:
    if len(hand) % group_size != 0:
        return False
    
    count = Counter(hand)
    hand.sort()
    
    for card in hand:
        if count[card] == 0:
            continue
        for i in range(group_size):
            if count[card + i] == 0:
                return False
            count[card + i] -= 1
    
    return True

Solution = create_solution(is_n_straight_hand)