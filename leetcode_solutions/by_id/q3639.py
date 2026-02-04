# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3639
标题: Zero Array Transformation I
难度: medium
链接: https://leetcode.cn/problems/zero-array-transformation-i/
题目类型: 数组、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3355. 零数组变换 I - 给定一个长度为 n 的整数数组 nums 和一个二维数组 queries，其中 queries[i] = [li, ri]。 对于每个查询 queries[i]： * 在 nums 的下标范围 [li, ri] 内选择一个下标 子集。 * 将选中的每个下标对应的元素值减 1。 零数组 是指所有元素都等于 0 的数组。 如果在按顺序处理所有查询后，可以将 nums 转换为 零数组 ，则返回 true，否则返回 false。 示例 1： 输入： nums = [1,0,1], queries = [[0,2]] 输出： true 解释： * 对于 i = 0： * 选择下标子集 [0, 2] 并将这些下标处的值减 1。 * 数组将变为 [0, 0, 0]，这是一个零数组。 示例 2： 输入： nums = [4,3,2,1], queries = [[1,3],[0,2]] 输出： false 解释： * 对于 i = 0： * 选择下标子集 [1, 2, 3] 并将这些下标处的值减 1。 * 数组将变为 [4, 2, 1, 0]。 * 对于 i = 1： * 选择下标子集 [0, 1, 2] 并将这些下标处的值减 1。 * 数组将变为 [3, 1, 0, 0]，这不是一个零数组。 提示： * 1 <= nums.length <= 105 * 0 <= nums[i] <= 105 * 1 <= queries.length <= 105 * queries[i].length == 2 * 0 <= li <= ri < nums.length
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用差分数组来高效地处理区间更新，并检查最终数组是否全为0。

算法步骤:
1. 初始化一个差分数组 diff，长度为 len(nums) + 1。
2. 对于每个查询 [li, ri]，在 diff[li] 位置加 1，在 diff[ri + 1] 位置减 1。
3. 通过差分数组计算最终的 nums 数组。
4. 检查最终的 nums 数组是否全为0。

关键点:
- 使用差分数组可以在 O(1) 时间内处理区间更新。
- 最终通过差分数组还原原数组并检查是否全为0。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 nums 的长度，m 是 queries 的长度。
空间复杂度: O(n)，需要额外的差分数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def can_transform_to_zero_array(nums: List[int], queries: List[List[int]]) -> bool:
    """
    函数式接口 - 判断是否可以通过给定的查询将 nums 转换为零数组。
    """
    n = len(nums)
    diff = [0] * (n + 1)

    # 处理每个查询
    for li, ri in queries:
        diff[li] += 1
        if ri + 1 < n:
            diff[ri + 1] -= 1

    # 通过差分数组计算最终的 nums 数组
    current_sum = 0
    for i in range(n):
        current_sum += diff[i]
        nums[i] -= current_sum
        if nums[i] < 0:
            return False

    # 检查最终的 nums 数组是否全为0
    return all(x == 0 for x in nums)


Solution = create_solution(can_transform_to_zero_array)