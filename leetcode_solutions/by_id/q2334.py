# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2334
标题: Number of Flowers in Full Bloom
难度: hard
链接: https://leetcode.cn/problems/number-of-flowers-in-full-bloom/
题目类型: 数组、哈希表、二分查找、有序集合、前缀和、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2251. 花期内花的数目 - 给你一个下标从 0 开始的二维整数数组 flowers ，其中 flowers[i] = [starti, endi] 表示第 i 朵花的 花期 从 starti 到 endi （都 包含）。同时给你一个下标从 0 开始大小为 n 的整数数组 people ，people[i] 是第 i 个人来看花的时间。 请你返回一个大小为 n 的整数数组 answer ，其中 answer[i]是第 i 个人到达时在花期内花的 数目 。 示例 1： [https://assets.leetcode.com/uploads/2022/03/02/ex1new.jpg] 输入：flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11] 输出：[1,2,2,2] 解释：上图展示了每朵花的花期时间，和每个人的到达时间。 对每个人，我们返回他们到达时在花期内花的数目。 示例 2： [https://assets.leetcode.com/uploads/2022/03/02/ex2new.jpg] 输入：flowers = [[1,10],[3,3]], people = [3,3,2] 输出：[2,2,1] 解释：上图展示了每朵花的花期时间，和每个人的到达时间。 对每个人，我们返回他们到达时在花期内花的数目。 提示： * 1 <= flowers.length <= 5 * 104 * flowers[i].length == 2 * 1 <= starti <= endi <= 109 * 1 <= people.length <= 5 * 104 * 1 <= people[i] <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用差分数组和前缀和来计算每个时间点的花的数量，然后使用二分查找来确定每个人到达时的花的数量。

算法步骤:
1. 将所有花的开始时间和结束时间分别存储在两个列表中。
2. 对这两个列表进行排序。
3. 使用二分查找来确定每个人到达时的花的数量。

关键点:
- 使用差分数组来记录每个时间点的花的变化。
- 使用前缀和来计算每个时间点的花的总数。
- 使用二分查找来高效地确定每个人到达时的花的数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O((m + n) log m)，其中 m 是 flowers 的长度，n 是 people 的长度。
空间复杂度: O(m + n)，用于存储开始时间和结束时间的列表以及结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import bisect

def full_bloom_flowers(flowers: List[List[int]], persons: List[int]) -> List[int]:
    start_times = []
    end_times = []

    for start, end in flowers:
        start_times.append(start)
        end_times.append(end + 1)  # 结束时间加1，表示花期结束后的第一个时间点

    start_times.sort()
    end_times.sort()

    def count_flowers_at_time(time: int) -> int:
        started = bisect.bisect_right(start_times, time)
        ended = bisect.bisect_left(end_times, time)
        return started - ended

    return [count_flowers_at_time(time) for time in persons]

Solution = create_solution(full_bloom_flowers)