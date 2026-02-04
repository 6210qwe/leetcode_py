# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1038
标题: Number of Squareful Arrays
难度: hard
链接: https://leetcode.cn/problems/number-of-squareful-arrays/
题目类型: 位运算、数组、哈希表、数学、动态规划、回溯、状态压缩
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
996. 平方数组的数目 - 如果一个数组的任意两个相邻元素之和都是 完全平方数 ，则该数组称为 平方数组 。 给定一个整数数组 nums，返回所有属于 平方数组 的 nums 的排列数量。 如果存在某个索引 i 使得 perm1[i] != perm2[i]，则认为两个排列 perm1 和 perm2 不同。 示例 1： 输入：nums = [1,17,8] 输出：2 解释：[1,8,17] 和 [17,8,1] 是有效的排列。 示例 2： 输入：nums = [2,2,2] 输出：1 提示： * 1 <= nums.length <= 12 * 0 <= nums[i] <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用回溯法生成所有可能的排列，并在每一步检查当前排列是否满足平方数组的条件。

算法步骤:
1. 定义一个辅助函数 `is_squareful` 来检查两个数的和是否为完全平方数。
2. 使用回溯法生成所有可能的排列。
3. 在每一步中，检查当前排列是否满足平方数组的条件。
4. 如果满足条件且排列长度等于输入数组的长度，则计数加一。

关键点:
- 使用集合来避免重复计算。
- 通过剪枝优化回溯过程。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n! * n) - 其中 n 是数组的长度，n! 是排列的数量，每个排列需要 O(n) 的时间来检查是否满足条件。
空间复杂度: O(n) - 递归调用栈的深度最多为 n。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def is_squareful(x: int, y: int) -> bool:
    """检查 x + y 是否是完全平方数"""
    s = (x + y) ** 0.5
    return s == int(s)


def backtrack(nums: List[int], used: List[bool], path: List[int]) -> int:
    if len(path) == len(nums):
        return 1
    count = 0
    for i in range(len(nums)):
        if used[i]:
            continue
        if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
            continue
        if len(path) == 0 or is_squareful(path[-1], nums[i]):
            used[i] = True
            path.append(nums[i])
            count += backtrack(nums, used, path)
            path.pop()
            used[i] = False
    return count


def solution_function_name(nums: List[int]) -> int:
    """
    函数式接口 - 计算平方数组的数目
    """
    nums.sort()
    used = [False] * len(nums)
    return backtrack(nums, used, [])


Solution = create_solution(solution_function_name)