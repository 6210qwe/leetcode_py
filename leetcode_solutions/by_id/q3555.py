# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3555
标题: Final Array State After K Multiplication Operations I
难度: easy
链接: https://leetcode.cn/problems/final-array-state-after-k-multiplication-operations-i/
题目类型: 数组、数学、模拟、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3264. K 次乘运算后的最终数组 I - 给你一个整数数组 nums ，一个整数 k 和一个整数 multiplier 。 你需要对 nums 执行 k 次操作，每次操作中： * 找到 nums 中的 最小 值 x ，如果存在多个最小值，选择最 前面 的一个。 * 将 x 替换为 x * multiplier 。 请你返回执行完 k 次乘运算之后，最终的 nums 数组。 示例 1： 输入：nums = [2,1,3,5,6], k = 5, multiplier = 2 输出：[8,4,6,5,6] 解释： 操作 结果 1 次操作后 [2, 2, 3, 5, 6] 2 次操作后 [4, 2, 3, 5, 6] 3 次操作后 [4, 4, 3, 5, 6] 4 次操作后 [4, 4, 6, 5, 6] 5 次操作后 [8, 4, 6, 5, 6] 示例 2： 输入：nums = [1,2], k = 3, multiplier = 4 输出：[16,8] 解释： 操作 结果 1 次操作后 [4, 2] 2 次操作后 [4, 8] 3 次操作后 [16, 8] 提示： * 1 <= nums.length <= 100 * 1 <= nums[i] <= 100 * 1 <= k <= 10 * 1 <= multiplier <= 5
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用最小堆来高效地找到并更新数组中的最小值。

算法步骤:
1. 初始化一个最小堆，并将数组中的所有元素及其索引存入堆中。
2. 执行 k 次操作：
   - 从堆中取出最小值及其索引。
   - 更新该值为当前值乘以 multiplier。
   - 将更新后的值及其索引重新插入堆中。
3. 最后，从堆中取出所有元素，按原索引顺序重建数组。

关键点:
- 使用最小堆来高效地找到并更新数组中的最小值。
- 通过索引来保持元素的原始位置。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(k log n + n log n)
  - 构建堆的时间复杂度是 O(n log n)。
  - 每次操作的时间复杂度是 O(log n)，总共进行 k 次操作，因此总时间复杂度是 O(k log n)。
  - 最后重建数组的时间复杂度是 O(n log n)。

空间复杂度: O(n)
  - 使用了一个大小为 n 的堆来存储数组中的元素及其索引。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
import heapq

def final_array_state(nums: List[int], k: int, multiplier: int) -> List[int]:
    """
    函数式接口 - 返回执行完 k 次乘运算之后，最终的 nums 数组。
    """
    # 初始化最小堆
    min_heap = [(num, i) for i, num in enumerate(nums)]
    heapq.heapify(min_heap)

    # 执行 k 次操作
    for _ in range(k):
        num, index = heapq.heappop(min_heap)
        new_num = num * multiplier
        heapq.heappush(min_heap, (new_num, index))

    # 重建数组
    result = [0] * len(nums)
    while min_heap:
        num, index = heapq.heappop(min_heap)
        result[index] = num

    return result

Solution = create_solution(final_array_state)