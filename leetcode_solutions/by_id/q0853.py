# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 853
标题: Most Profit Assigning Work
难度: medium
链接: https://leetcode.cn/problems/most-profit-assigning-work/
题目类型: 贪心、数组、双指针、二分查找、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
826. 安排工作以达到最大收益 - 你有 n 个工作和 m 个工人。给定三个数组： difficulty, profit 和 worker ，其中: * difficulty[i] 表示第 i 个工作的难度，profit[i] 表示第 i 个工作的收益。 * worker[i] 是第 i 个工人的能力，即该工人只能完成难度小于等于 worker[i] 的工作。 每个工人 最多 只能安排 一个 工作，但是一个工作可以 完成多次 。 * 举个例子，如果 3 个工人都尝试完成一份报酬为 $1 的同样工作，那么总收益为 $3 。如果一个工人不能完成任何工作，他的收益为 $0 。 返回 在把工人分配到工作岗位后，我们所能获得的最大利润 。 示例 1： 输入: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7] 输出: 100 解释: 工人被分配的工作难度是 [4,4,6,6] ，分别获得 [20,20,30,30] 的收益。 示例 2: 输入: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25] 输出: 0 提示: * n == difficulty.length * n == profit.length * m == worker.length * 1 <= n, m <= 104 * 1 <= difficulty[i], profit[i], worker[i] <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和双指针来最大化收益。

算法步骤:
1. 将工作按难度升序排序。
2. 创建一个数组 `max_profit`，其中 `max_profit[i]` 表示难度不超过 `difficulty[i]` 的最大收益。
3. 对于每个工人，使用二分查找找到他们能完成的最难的工作，并计算其收益。

关键点:
- 通过排序和预处理 `max_profit` 数组，可以在 O(log n) 时间内找到每个工人能完成的最难的工作。
- 使用双指针来优化遍历过程。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n + m log n)，其中 n 是工作的数量，m 是工人的数量。排序的时间复杂度是 O(n log n)，二分查找的时间复杂度是 O(m log n)。
空间复杂度: O(n)，用于存储 `max_profit` 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def maxProfitAssignment(difficulty: List[int], profit: List[int], worker: List[int]) -> int:
    """
    函数式接口 - 实现最优解法
    """
    # 将工作按难度升序排序
    jobs = sorted(zip(difficulty, profit))
    
    # 创建一个数组 max_profit，其中 max_profit[i] 表示难度不超过 difficulty[i] 的最大收益
    max_profit = [0] * len(jobs)
    max_profit[0] = jobs[0][1]
    for i in range(1, len(jobs)):
        max_profit[i] = max(max_profit[i-1], jobs[i][1])
    
    # 计算每个工人的最大收益
    total_profit = 0
    for w in worker:
        # 使用二分查找找到工人能完成的最难的工作
        left, right = 0, len(jobs) - 1
        while left <= right:
            mid = (left + right) // 2
            if jobs[mid][0] <= w:
                left = mid + 1
            else:
                right = mid - 1
        if right >= 0:
            total_profit += max_profit[right]
    
    return total_profit


Solution = create_solution(maxProfitAssignment)