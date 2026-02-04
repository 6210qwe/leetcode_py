# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2330
标题: Maximum Total Beauty of the Gardens
难度: hard
链接: https://leetcode.cn/problems/maximum-total-beauty-of-the-gardens/
题目类型: 贪心、数组、双指针、二分查找、枚举、前缀和、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2234. 花园的最大总美丽值 - Alice 是 n 个花园的园丁，她想通过种花，最大化她所有花园的总美丽值。 给你一个下标从 0 开始大小为 n 的整数数组 flowers ，其中 flowers[i] 是第 i 个花园里已经种的花的数目。已经种了的花 不能 移走。同时给你 newFlowers ，表示 Alice 额外可以种花的 最大数目 。同时给你的还有整数 target ，full 和 partial 。 如果一个花园有 至少 target 朵花，那么这个花园称为 完善的 ，花园的 总美丽值 为以下分数之 和 ： * 完善 花园数目乘以 full. * 剩余 不完善 花园里，花的 最少数目 乘以 partial 。如果没有不完善花园，那么这一部分的值为 0 。 请你返回 Alice 种最多 newFlowers 朵花以后，能得到的 最大 总美丽值。 示例 1： 输入：flowers = [1,3,1,1], newFlowers = 7, target = 6, full = 12, partial = 1 输出：14 解释：Alice 可以按以下方案种花 - 在第 0 个花园种 2 朵花 - 在第 1 个花园种 3 朵花 - 在第 2 个花园种 1 朵花 - 在第 3 个花园种 1 朵花 花园里花的数目为 [3,6,2,2] 。总共种了 2 + 3 + 1 + 1 = 7 朵花。 只有 1 个花园是完善的。 不完善花园里花的最少数目是 2 。 所以总美丽值为 1 * 12 + 2 * 1 = 12 + 2 = 14 。 没有其他方案可以让花园总美丽值超过 14 。 示例 2： 输入：flowers = [2,4,5,3], newFlowers = 10, target = 5, full = 2, partial = 6 输出：30 解释：Alice 可以按以下方案种花 - 在第 0 个花园种 3 朵花 - 在第 1 个花园种 0 朵花 - 在第 2 个花园种 0 朵花 - 在第 3 个花园种 2 朵花 花园里花的数目为 [5,4,5,5] 。总共种了 3 + 0 + 0 + 2 = 5 朵花。 有 3 个花园是完善的。 不完善花园里花的最少数目为 4 。 所以总美丽值为 3 * 2 + 4 * 6 = 6 + 24 = 30 。 没有其他方案可以让花园总美丽值超过 30 。 注意，Alice可以让所有花园都变成完善的，但这样她的总美丽值反而更小。 提示： * 1 <= flowers.length <= 105 * 1 <= flowers[i], target <= 105 * 1 <= newFlowers <= 1010 * 1 <= full, partial <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和双指针来最大化总美丽值。

算法步骤:
1. 对花园进行排序。
2. 计算前缀和以便快速计算需要的花朵数量。
3. 使用双指针遍历花园，尝试将尽可能多的花园变为完善花园，并计算剩余花朵用于不完善花园的最大最小值。
4. 更新最大总美丽值。

关键点:
- 通过排序和前缀和优化计算。
- 使用双指针平衡完善和不完善花园的数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n) - 排序操作的时间复杂度。
空间复杂度: O(n) - 存储前缀和数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_total_beauty(flowers: List[int], new_flowers: int, target: int, full: int, partial: int) -> int:
    n = len(flowers)
    flowers.sort()
    
    # 如果所有花园都已经完善
    if flowers[0] >= target:
        return n * full
    
    # 计算前缀和
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + flowers[i - 1]
    
    max_beauty = 0
    j = n - 1
    
    while j >= 0 and new_flowers >= 0:
        # 将当前花园变为完善花园
        if flowers[j] < target:
            needed = target - flowers[j]
            if new_flowers >= needed:
                new_flowers -= needed
                flowers[j] = target
            else:
                break
        
        # 计算剩余不完善花园的最大最小值
        left = 0
        right = j
        while left < right:
            mid = (left + right + 1) // 2
            required = mid * flowers[mid] - prefix_sum[mid]
            if required <= new_flowers:
                left = mid
            else:
                right = mid - 1
        
        min_flowers = (new_flowers + prefix_sum[left]) // (left + 1)
        beauty = (n - j - 1) * full + min_flowers * partial
        max_beauty = max(max_beauty, beauty)
        
        j -= 1
    
    return max_beauty


Solution = create_solution(max_total_beauty)