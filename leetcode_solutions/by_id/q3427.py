# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3427
标题: Special Array II
难度: medium
链接: https://leetcode.cn/problems/special-array-ii/
题目类型: 数组、二分查找、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3152. 特殊数组 II - 如果数组的每一对相邻元素都是两个奇偶性不同的数字，则该数组被认为是一个 特殊数组 。 你有一个整数数组 nums 和一个二维整数矩阵 queries，对于 queries[i] = [fromi, toi]，请你帮助你检查 子数组 nums[fromi..toi] 是不是一个 特殊数组 。 返回布尔数组 answer，如果 nums[fromi..toi] 是特殊数组，则 answer[i] 为 true ，否则，answer[i] 为 false 。 示例 1： 输入：nums = [3,4,1,2,6], queries = [[0,4]] 输出：[false] 解释： 子数组是 [3,4,1,2,6]。2 和 6 都是偶数。 示例 2： 输入：nums = [4,3,1,6], queries = [[0,2],[2,3]] 输出：[false,true] 解释： 1. 子数组是 [4,3,1]。3 和 1 都是奇数。因此这个查询的答案是 false。 2. 子数组是 [1,6]。只有一对：(1,6)，且包含了奇偶性不同的数字。因此这个查询的答案是 true。 提示： * 1 <= nums.length <= 105 * 1 <= nums[i] <= 105 * 1 <= queries.length <= 105 * queries[i].length == 2 * 0 <= queries[i][0] <= queries[i][1] <= nums.length - 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和来快速判断子数组是否为特殊数组。

算法步骤:
1. 计算前缀和数组，记录每个位置之前奇数和偶数的数量。
2. 对于每个查询，使用前缀和数组快速判断子数组是否满足条件。

关键点:
- 前缀和数组可以快速计算任意子数组中奇数和偶数的数量。
- 检查子数组的第一个和最后一个元素的奇偶性，并确保子数组长度为奇数时，奇数和偶数的数量相等。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 nums 的长度，m 是 queries 的长度。
空间复杂度: O(n)，用于存储前缀和数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def is_special_array(nums: List[int], queries: List[List[int]]) -> List[bool]:
    n = len(nums)
    prefix_sum = [[0, 0] for _ in range(n + 1)]
    
    # 计算前缀和数组
    for i in range(n):
        prefix_sum[i + 1][0] = prefix_sum[i][0] + (nums[i] % 2 == 0)
        prefix_sum[i + 1][1] = prefix_sum[i][1] + (nums[i] % 2 != 0)
    
    def is_special(start: int, end: int) -> bool:
        even_count = prefix_sum[end + 1][0] - prefix_sum[start][0]
        odd_count = prefix_sum[end + 1][1] - prefix_sum[start][1]
        length = end - start + 1
        
        if length % 2 == 0:
            return even_count == odd_count
        else:
            return abs(even_count - odd_count) == 1 and (nums[start] % 2 != nums[end] % 2)
    
    result = []
    for query in queries:
        start, end = query
        result.append(is_special(start, end))
    
    return result

Solution = create_solution(is_special_array)