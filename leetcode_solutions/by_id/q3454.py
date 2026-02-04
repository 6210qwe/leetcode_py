# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3454
标题: Minimum Operations to Make Array Equal to Target
难度: hard
链接: https://leetcode.cn/problems/minimum-operations-to-make-array-equal-to-target/
题目类型: 栈、贪心、数组、动态规划、单调栈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3229. 使数组等于目标数组所需的最少操作次数 - 给你两个长度相同的正整数数组 nums 和 target。 在一次操作中，你可以选择 nums 的任何子数组，并将该子数组内的每个元素的值增加或减少 1。 返回使 nums 数组变为 target 数组所需的 最少 操作次数。 示例 1： 输入： nums = [3,5,1,2], target = [4,6,2,4] 输出： 2 解释： 执行以下操作可以使 nums 等于 target： - nums[0..3] 增加 1，nums = [4,6,2,3]。 - nums[3..3] 增加 1，nums = [4,6,2,4]。 示例 2： 输入： nums = [1,3,2], target = [2,1,4] 输出： 5 解释： 执行以下操作可以使 nums 等于 target： - nums[0..0] 增加 1，nums = [2,3,2]。 - nums[1..1] 减少 1，nums = [2,2,2]。 - nums[1..1] 减少 1，nums = [2,1,2]。 - nums[2..2] 增加 1，nums = [2,1,3]。 - nums[2..2] 增加 1，nums = [2,1,4]。 提示： * 1 <= nums.length == target.length <= 105 * 1 <= nums[i], target[i] <= 108
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，通过维护一个单调栈来最小化操作次数。

算法步骤:
1. 初始化一个单调栈，用于存储需要调整的差值。
2. 遍历数组，计算每个位置的差值，并将其加入单调栈。
3. 对于每个差值，如果可以与栈顶元素合并，则合并并更新操作次数。
4. 最终返回操作次数。

关键点:
- 通过维护单调栈来最小化操作次数。
- 合并差值时，尽量减少操作次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def min_operations_to_target(nums: List[int], target: List[int]) -> int:
    """
    计算使 nums 数组变为 target 数组所需的最少操作次数。
    """
    n = len(nums)
    diff = [target[i] - nums[i] for i in range(n)]
    stack = []
    operations = 0

    for d in diff:
        if not stack or d * stack[-1] >= 0:
            stack.append(d)
        else:
            while stack and abs(stack[-1]) < abs(d):
                operations += abs(stack.pop())
            if stack and abs(stack[-1]) == abs(d):
                operations += abs(d)
                stack.pop()
            elif stack and abs(stack[-1]) > abs(d):
                operations += abs(d)
                stack[-1] += d
            else:
                stack.append(d)

    return operations + sum(abs(d) for d in stack)

Solution = create_solution(min_operations_to_target)