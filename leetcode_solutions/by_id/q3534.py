# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3534
标题: Count Almost Equal Pairs I
难度: medium
链接: https://leetcode.cn/problems/count-almost-equal-pairs-i/
题目类型: 数组、哈希表、计数、枚举、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3265. 统计近似相等数对 I - 给你一个正整数数组 nums 。 如果我们执行以下操作 至多一次 可以让两个整数 x 和 y 相等，那么我们称这个数对是 近似相等 的： * 选择 x 或者 y 之一，将这个数字中的两个数位交换。 请你返回 nums 中，下标 i 和 j 满足 i < j 且 nums[i] 和 nums[j] 近似相等 的数对数目。 注意 ，执行操作后一个整数可以有前导 0 。 示例 1： 输入：nums = [3,12,30,17,21] 输出：2 解释： 近似相等数对包括： * 3 和 30 。交换 30 中的数位 3 和 0 ，得到 3 。 * 12 和 21 。交换12 中的数位 1 和 2 ，得到 21 。 示例 2： 输入：nums = [1,1,1,1,1] 输出：10 解释： 数组中的任意两个元素都是近似相等的。 示例 3： 输入：nums = [123,231] 输出：0 解释： 我们无法通过交换 123 或者 231 中的两个数位得到另一个数。 提示： * 2 <= nums.length <= 100 * 1 <= nums[i] <= 106
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过生成所有可能的交换后的数，并使用哈希表来记录这些数出现的次数，从而找到近似相等的数对。

算法步骤:
1. 对于每个数，生成所有可能的交换后的数。
2. 使用哈希表记录每个数及其交换后的数出现的次数。
3. 遍历哈希表，计算近似相等的数对数量。

关键点:
- 生成所有可能的交换后的数。
- 使用哈希表高效地记录和查找数对。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * d^2)，其中 n 是数组的长度，d 是数字的最大位数（最多为 6）。
空间复杂度: O(n * d^2)，用于存储哈希表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def generate_swapped_numbers(num: int) -> set:
    """生成 num 所有可能的交换后的数"""
    str_num = str(num)
    swapped_set = {num}
    for i in range(len(str_num)):
        for j in range(i + 1, len(str_num)):
            swapped_str = list(str_num)
            swapped_str[i], swapped_str[j] = swapped_str[j], swapped_str[i]
            swapped_set.add(int(''.join(swapped_str)))
    return swapped_set

def count_almost_equal_pairs(nums: List[int]) -> int:
    """
    函数式接口 - 计算近似相等的数对数量
    """
    num_count = {}
    for num in nums:
        swapped_set = generate_swapped_numbers(num)
        for swapped_num in swapped_set:
            if swapped_num in num_count:
                num_count[swapped_num] += 1
            else:
                num_count[swapped_num] = 1
    
    count = 0
    for num in nums:
        swapped_set = generate_swapped_numbers(num)
        for swapped_num in swapped_set:
            if swapped_num in num_count:
                count += num_count[swapped_num]
                if num == swapped_num:
                    count -= 1
        num_count[num] = 0  # 避免重复计算
    return count // 2  # 每个数对被计算了两次

Solution = create_solution(count_almost_equal_pairs)