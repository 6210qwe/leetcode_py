# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2413
标题: Smallest Number in Infinite Set
难度: medium
链接: https://leetcode.cn/problems/smallest-number-in-infinite-set/
题目类型: 设计、哈希表、有序集合、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2336. 无限集中的最小数字 - 现有一个包含所有正整数的集合 [1, 2, 3, 4, 5, ...] 。 实现 SmallestInfiniteSet 类： * SmallestInfiniteSet() 初始化 SmallestInfiniteSet 对象以包含 所有 正整数。 * int popSmallest() 移除 并返回该无限集中的最小整数。 * void addBack(int num) 如果正整数 num 不 存在于无限集中，则将一个 num 添加 到该无限集中。 示例： 输入 ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"] [[], [2], [], [], [], [1], [], [], []] 输出 [null, null, 1, 2, 3, null, 1, 4, 5] 解释 SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet(); smallestInfiniteSet.addBack(2); // 2 已经在集合中，所以不做任何变更。 smallestInfiniteSet.popSmallest(); // 返回 1 ，因为 1 是最小的整数，并将其从集合中移除。 smallestInfiniteSet.popSmallest(); // 返回 2 ，并将其从集合中移除。 smallestInfiniteSet.popSmallest(); // 返回 3 ，并将其从集合中移除。 smallestInfiniteSet.addBack(1); // 将 1 添加到该集合中。 smallestInfiniteSet.popSmallest(); // 返回 1 ，因为 1 在上一步中被添加到集合中， // 且 1 是最小的整数，并将其从集合中移除。 smallestInfiniteSet.popSmallest(); // 返回 4 ，并将其从集合中移除。 smallestInfiniteSet.popSmallest(); // 返回 5 ，并将其从集合中移除。 提示： * 1 <= num <= 1000 * 最多调用 popSmallest 和 addBack 方法 共计 1000 次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个有序集合来维护当前集合中的元素，并使用一个变量来记录当前最小未被移除的整数。

算法步骤:
1. 初始化时，设置 current_min 为 1。
2. popSmallest 时，如果有序集合为空，返回 current_min 并递增 current_min；否则，从有序集合中弹出最小值。
3. addBack 时，如果 num 小于 current_min 且不在有序集合中，将其添加到有序集合中。

关键点:
- 使用有序集合来高效地管理被添加回来的元素。
- 使用 current_min 来跟踪当前最小未被移除的整数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n) - 有序集合的插入和删除操作的时间复杂度。
空间复杂度: O(n) - 有序集合的空间复杂度，n 为被添加回来的元素数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
from sortedcontainers import SortedSet

class SmallestInfiniteSet:

    def __init__(self):
        self.current_min = 1
        self.added_back = SortedSet()

    def popSmallest(self) -> int:
        if not self.added_back:
            result = self.current_min
            self.current_min += 1
            return result
        else:
            result = self.added_back[0]
            self.added_back.discard(result)
            return result

    def addBack(self, num: int) -> None:
        if num < self.current_min and num not in self.added_back:
            self.added_back.add(num)

Solution = create_solution(SmallestInfiniteSet)