# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3843
标题: Partition Array into Two Equal Product Subsets
难度: medium
链接: https://leetcode.cn/problems/partition-array-into-two-equal-product-subsets/
题目类型: 位运算、递归、数组、枚举
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3566. 等积子集的划分方案 - 给你一个整数数组 nums，其中包含的正整数 互不相同 ，另给你一个整数 target。 请判断是否可以将 nums 分成两个 非空、互不相交 的 子集 ，并且每个元素必须 恰好 属于 一个 子集，使得这两个子集中元素的乘积都等于 target。 如果存在这样的划分，返回 true；否则，返回 false。 子集 是数组中元素的一个选择集合。 示例 1： 输入： nums = [3,1,6,8,4], target = 24 输出： true 解释：子集 [3, 8] 和 [1, 6, 4] 的乘积均为 24。因此，输出为 true 。 示例 2： 输入： nums = [2,5,3,7], target = 15 输出： false 解释：无法将 nums 划分为两个非空的互不相交子集，使得它们的乘积均为 15。因此，输出为 false。 提示： * 3 <= nums.length <= 12 * 1 <= target <= 1015 * 1 <= nums[i] <= 100 * nums 中的所有元素互不相同。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用回溯法尝试所有可能的子集组合，检查是否存在两个子集的乘积等于目标值。

算法步骤:
1. 计算数组所有元素的乘积 total_product。
2. 如果 total_product 不是 target 的平方，则不可能找到两个子集，返回 False。
3. 使用回溯法尝试所有可能的子集组合，检查是否存在一个子集的乘积等于 target。
4. 如果找到一个子集的乘积等于 target，则另一个子集的乘积也必然等于 target，返回 True。
5. 如果遍历完所有组合仍未找到满足条件的子集，返回 False。

关键点:
- 使用回溯法来生成所有可能的子集组合。
- 通过计算总乘积和目标值的关系来提前判断是否可能找到解。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^n)，其中 n 是数组的长度。因为我们需要尝试所有可能的子集组合。
空间复杂度: O(n)，递归调用栈的深度最多为 n。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def can_partition_equal_product(nums: List[int], target: int) -> bool:
    def backtrack(index: int, current_product: int) -> bool:
        if current_product == target:
            return True
        if current_product > target or index == len(nums):
            return False
        for i in range(index, len(nums)):
            if backtrack(i + 1, current_product * nums[i]):
                return True
        return False

    total_product = 1
    for num in nums:
        total_product *= num

    if total_product != target ** 2:
        return False

    return backtrack(0, 1)


Solution = create_solution(can_partition_equal_product)