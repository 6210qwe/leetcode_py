# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2034
标题: Minimum Absolute Difference Queries
难度: medium
链接: https://leetcode.cn/problems/minimum-absolute-difference-queries/
题目类型: 数组、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1906. 查询差绝对值的最小值 - 一个数组 a 的 差绝对值的最小值 定义为：0 <= i < j < a.length 且 a[i] != a[j] 的 |a[i] - a[j]| 的 最小值。如果 a 中所有元素都 相同 ，那么差绝对值的最小值为 -1 。 * 比方说，数组 [5,2,3,7,2] 差绝对值的最小值是 |2 - 3| = 1 。注意答案不为 0 ，因为 a[i] 和 a[j] 必须不相等。 给你一个整数数组 nums 和查询数组 queries ，其中 queries[i] = [li, ri] 。对于每个查询 i ，计算 子数组 nums[li...ri] 中 差绝对值的最小值 ，子数组 nums[li...ri] 包含 nums 数组（下标从 0 开始）中下标在 li 和 ri 之间的所有元素（包含 li 和 ri 在内）。 请你返回 ans 数组，其中 ans[i] 是第 i 个查询的答案。 子数组 是一个数组中连续的一段元素。 |x| 的值定义为： * 如果 x >= 0 ，那么值为 x 。 * 如果 x < 0 ，那么值为 -x 。 示例 1： 输入：nums = [1,3,4,8], queries = [[0,1],[1,2],[2,3],[0,3]] 输出：[2,1,4,1] 解释：查询结果如下： - queries[0] = [0,1]：子数组是 [1,3] ，差绝对值的最小值为 |1-3| = 2 。 - queries[1] = [1,2]：子数组是 [3,4] ，差绝对值的最小值为 |3-4| = 1 。 - queries[2] = [2,3]：子数组是 [4,8] ，差绝对值的最小值为 |4-8| = 4 。 - queries[3] = [0,3]：子数组是 [1,3,4,8] ，差的绝对值的最小值为 |3-4| = 1 。 示例 2： 输入：nums = [4,5,2,2,7,10], queries = [[2,3],[0,2],[0,5],[3,5]] 输出：[-1,1,1,3] 解释：查询结果如下： - queries[0] = [2,3]：子数组是 [2,2] ，差绝对值的最小值为 -1 ，因为所有元素相等。 - queries[1] = [0,2]：子数组是 [4,5,2] ，差绝对值的最小值为 |4-5| = 1 。 - queries[2] = [0,5]：子数组是 [4,5,2,2,7,10] ，差绝对值的最小值为 |4-5| = 1 。 - queries[3] = [3,5]：子数组是 [2,7,10] ，差绝对值的最小值为 |7-10| = 3 。 提示： * 2 <= nums.length <= 105 * 1 <= nums[i] <= 100 * 1 <= queries.length <= 2 * 104 * 0 <= li < ri < nums.length
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和来快速计算子数组中的唯一元素，并找到这些元素之间的最小差值。

算法步骤:
1. 构建前缀和数组，记录每个位置之前出现过的元素。
2. 对于每个查询，使用前缀和数组快速找到子数组中的唯一元素。
3. 计算这些唯一元素之间的最小差值。

关键点:
- 使用前缀和数组来快速查找子数组中的唯一元素。
- 通过排序和遍历唯一元素来找到最小差值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + q * log(max(nums)))，其中 n 是 nums 的长度，q 是 queries 的长度。
空间复杂度: O(n * max(nums))，用于存储前缀和数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def min_absolute_difference(nums: List[int], queries: List[List[int]]) -> List[int]:
    n = len(nums)
    max_num = max(nums)
    prefix_sum = [[0] * (max_num + 1) for _ in range(n + 1)]
    
    # 构建前缀和数组
    for i in range(1, n + 1):
        for j in range(1, max_num + 1):
            prefix_sum[i][j] = prefix_sum[i - 1][j]
        prefix_sum[i][nums[i - 1]] += 1
    
    def get_unique_elements(l: int, r: int) -> List[int]:
        unique_elements = []
        for num in range(1, max_num + 1):
            if prefix_sum[r + 1][num] > prefix_sum[l][num]:
                unique_elements.append(num)
        return unique_elements
    
    result = []
    for l, r in queries:
        unique_elements = get_unique_elements(l, r)
        if len(unique_elements) < 2:
            result.append(-1)
        else:
            unique_elements.sort()
            min_diff = float('inf')
            for i in range(1, len(unique_elements)):
                min_diff = min(min_diff, unique_elements[i] - unique_elements[i - 1])
            result.append(min_diff)
    
    return result

Solution = create_solution(min_absolute_difference)