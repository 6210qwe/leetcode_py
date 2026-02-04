# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1872
标题: Can You Eat Your Favorite Candy on Your Favorite Day?
难度: medium
链接: https://leetcode.cn/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/
题目类型: 数组、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1744. 你能在你最喜欢的那天吃到你最喜欢的糖果吗？ - 给你一个下标从 0 开始的正整数数组 candiesCount ，其中 candiesCount[i] 表示你拥有的第 i 类糖果的数目。同时给你一个二维数组 queries ，其中 queries[i] = [favoriteTypei, favoriteDayi, dailyCapi] 。 你按照如下规则进行一场游戏： * 你从第 0 天开始吃糖果。 * 你在吃完 所有 第 i - 1 类糖果之前，不能 吃任何一颗第 i 类糖果。 * 在吃完所有糖果之前，你必须每天 至少 吃 一颗 糖果。 请你构建一个布尔型数组 answer ，用以给出 queries 中每一项的对应答案。此数组满足： * answer.length == queries.length 。answer[i] 是 queries[i] 的答案。 * answer[i] 为 true 的条件是：在每天吃 不超过 dailyCapi 颗糖果的前提下，你可以在第 favoriteDayi 天吃到第 favoriteTypei 类糖果；否则 answer[i] 为 false 。 注意，只要满足上面 3 条规则中的第二条规则，你就可以在同一天吃不同类型的糖果。 请你返回得到的数组 answer 。 示例 1： 输入：candiesCount = [7,4,5,3,8], queries = [[0,2,2],[4,2,4],[2,13,1000000000]] 输出：[true,false,true] 提示： 1- 在第 0 天吃 2 颗糖果(类型 0），第 1 天吃 2 颗糖果（类型 0），第 2 天你可以吃到类型 0 的糖果。 2- 每天你最多吃 4 颗糖果。即使第 0 天吃 4 颗糖果（类型 0），第 1 天吃 4 颗糖果（类型 0 和类型 1），你也没办法在第 2 天吃到类型 4 的糖果。换言之，你没法在每天吃 4 颗糖果的限制下在第 2 天吃到第 4 类糖果。 3- 如果你每天吃 1 颗糖果，你可以在第 13 天吃到类型 2 的糖果。 示例 2： 输入：candiesCount = [5,2,6,4,1], queries = [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]] 输出：[false,true,true,false,false] 提示： * 1 <= candiesCount.length <= 105 * 1 <= candiesCount[i] <= 105 * 1 <= queries.length <= 105 * queries[i].length == 3 * 0 <= favoriteTypei < candiesCount.length * 0 <= favoriteDayi <= 109 * 1 <= dailyCapi <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和来快速计算在某一天之前可以吃的糖果总数，并判断是否可以在指定的天数内吃到指定类型的糖果。

算法步骤:
1. 计算 candiesCount 的前缀和数组 prefix_sum。
2. 对于每个查询，计算在 favoriteDayi 天之前可以吃的最小糖果数和最大糖果数。
3. 判断这些范围是否包含 favoriteTypei 类糖果的数量。

关键点:
- 使用前缀和数组来快速计算某个区间的糖果总数。
- 确保在 favoriteDayi 天之前可以吃到 favoriteTypei 类糖果。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 candiesCount 的长度，m 是 queries 的长度。
空间复杂度: O(n)，用于存储前缀和数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def can_eat(candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
    # 计算前缀和数组
    prefix_sum = [0]
    for count in candiesCount:
        prefix_sum.append(prefix_sum[-1] + count)
    
    def can_eat_query(favorite_type: int, favorite_day: int, daily_cap: int) -> bool:
        min_candies = favorite_day + 1
        max_candies = (favorite_day + 1) * daily_cap
        start = prefix_sum[favorite_type]
        end = prefix_sum[favorite_type + 1]
        return not (min_candies > end or max_candies <= start)
    
    return [can_eat_query(favorite_type, favorite_day, daily_cap) for favorite_type, favorite_day, daily_cap in queries]

Solution = create_solution(can_eat)