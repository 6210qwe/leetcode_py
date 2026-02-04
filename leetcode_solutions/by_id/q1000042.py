# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000042
标题: Pairs With Sum LCCI
难度: medium
链接: https://leetcode.cn/problems/pairs-with-sum-lcci/
题目类型: 数组、哈希表、双指针、计数、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 16.24. 数对和 - 设计一个算法，找出数组中两数之和为指定值的所有整数对。一个数只能属于一个数对。 示例 1： 输入：nums = [5,6,5], target = 11 输出：[[5,6]] 示例 2： 输入：nums = [5,6,5,6], target = 11 输出：[[5,6],[5,6]] 提示： * nums.length <= 100000 * -105 <= nums[i], target <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表记录每个数出现的次数，然后遍历数组，找到所有满足条件的数对。

算法步骤:
1. 初始化一个哈希表 `count` 来记录每个数出现的次数。
2. 初始化一个结果列表 `result`。
3. 遍历数组 `nums`，对于每个数 `num`：
   - 计算 `complement = target - num`。
   - 如果 `complement` 在哈希表中且其计数大于 0，则将 `[num, complement]` 添加到结果列表中，并减少 `complement` 和 `num` 的计数。
4. 返回结果列表 `result`。

关键点:
- 使用哈希表记录每个数的出现次数，可以在 O(1) 时间内查找和更新。
- 确保每个数只能属于一个数对。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组 `nums` 的长度。我们只需要遍历数组一次。
空间复杂度: O(n)，哈希表 `count` 最多存储 n 个不同的数。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(nums: List[int], target: int) -> List[List[int]]:
    """
    函数式接口 - 找出数组中两数之和为指定值的所有整数对
    """
    count = {}
    result = []

    # 记录每个数出现的次数
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    # 遍历数组，找到所有满足条件的数对
    for num in nums:
        complement = target - num
        if complement in count and count[complement] > 0 and count[num] > 0:
            if num == complement and count[num] < 2:
                continue
            result.append([num, complement])
            count[complement] -= 1
            count[num] -= 1

    return result


Solution = create_solution(solution_function_name)