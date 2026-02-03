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
