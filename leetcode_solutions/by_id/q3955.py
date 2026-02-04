# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3955
标题: Threshold Majority Queries
难度: hard
链接: https://leetcode.cn/problems/threshold-majority-queries/
题目类型: 数组、哈希表、二分查找、分治、计数、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3636. 查询超过阈值频率最高元素 - 给你一个长度为 n 的整数数组 nums 和一个查询数组 queries，其中 queries[i] = [li, ri, thresholdi]。 返回一个整数数组 ans，其中 ans[i] 等于子数组 nums[li...ri] 中出现 至少 thresholdi 次的元素，选择频率 最高 的元素（如果频率相同则选择 最小 的元素），如果不存在这样的元素则返回 -1。 示例 1: 输入： nums = [1,1,2,2,1,1], queries = [[0,5,4],[0,3,3],[2,3,2]] 输出： [1,-1,2] 解释： 查询 子数组 阈值 频率表 答案 [0, 5, 4] [1, 1, 2, 2, 1, 1] 4 1 → 4, 2 → 2 1 [0, 3, 3] [1, 1, 2, 2] 3 1 → 2, 2 → 2 -1 [2, 3, 2] [2, 2] 2 2 → 2 2 示例 2: 输入：nums = [3,2,3,2,3,2,3], queries = [[0,6,4],[1,5,2],[2,4,1],[3,3,1]] 输出：[3,2,3,2] 解释： 查询 子数组 阈值 频率表 答案 [0, 6, 4] [3, 2, 3, 2, 3, 2, 3] 4 3 → 4, 2 → 3 3 [1, 5, 2] [2, 3, 2, 3, 2] 2 2 → 3, 3 → 2 2 [2, 4, 1] [3, 2, 3] 1 3 → 2, 2 → 1 3 [3, 3, 1] [2] 1 2 → 1 2 提示： * 1 <= nums.length == n <= 104 * 1 <= nums[i] <= 109 * 1 <= queries.length <= 5 * 104 * queries[i] = [li, ri, thresholdi] * 0 <= li <= ri < n * 1 <= thresholdi <= ri - li + 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和和离散化来处理每个查询。

算法步骤:
1. 对 nums 进行离散化处理，将大范围的数值映射到较小的范围内。
2. 构建前缀和数组，记录每个位置上各个离散化后的值的频率。
3. 对于每个查询，使用前缀和数组快速计算子数组中每个元素的频率。
4. 找出满足条件的频率最高的元素。

关键点:
- 使用离散化减少空间复杂度。
- 使用前缀和数组快速计算子数组中的频率。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + q * log n)，其中 n 是 nums 的长度，q 是 queries 的长度。
空间复杂度: O(n + m)，其中 n 是 nums 的长度，m 是离散化后的值的数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import defaultdict

def solution_function_name(nums: List[int], queries: List[List[int]]) -> List[int]:
    def discretize(nums):
        unique_vals = sorted(set(nums))
        val_to_id = {val: idx for idx, val in enumerate(unique_vals)}
        return [val_to_id[num] for num in nums], len(unique_vals)

    def build_prefix_sum(discretized_nums, m):
        prefix_sum = [[0] * (m + 1) for _ in range(len(discretized_nums) + 1)]
        for i in range(1, len(discretized_nums) + 1):
            for j in range(m + 1):
                prefix_sum[i][j] = prefix_sum[i - 1][j]
            prefix_sum[i][discretized_nums[i - 1]] += 1
        return prefix_sum

    def query_range(prefix_sum, l, r, threshold):
        freq = defaultdict(int)
        for i in range(m):
            if prefix_sum[r + 1][i] - prefix_sum[l][i] >= threshold:
                freq[i] = prefix_sum[r + 1][i] - prefix_sum[l][i]
        if not freq:
            return -1
        max_freq = max(freq.values())
        return min([k for k, v in freq.items() if v == max_freq])

    discretized_nums, m = discretize(nums)
    prefix_sum = build_prefix_sum(discretized_nums, m)
    result = []
    for l, r, threshold in queries:
        result.append(query_range(prefix_sum, l, r, threshold))
    return result

Solution = create_solution(solution_function_name)