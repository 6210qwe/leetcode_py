# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2447
标题: Merge Similar Items
难度: easy
链接: https://leetcode.cn/problems/merge-similar-items/
题目类型: 数组、哈希表、有序集合、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2363. 合并相似的物品 - 给你两个二维整数数组 items1 和 items2 ，表示两个物品集合。每个数组 items 有以下特质： * items[i] = [valuei, weighti] 其中 valuei 表示第 i 件物品的 价值 ，weighti 表示第 i 件物品的 重量 。 * items 中每件物品的价值都是 唯一的 。 请你返回一个二维数组 ret，其中 ret[i] = [valuei, weighti]， weighti 是所有价值为 valuei 物品的 重量之和 。 注意：ret 应该按价值 升序 排序后返回。 示例 1： 输入：items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]] 输出：[[1,6],[3,9],[4,5]] 解释： value = 1 的物品在 items1 中 weight = 1 ，在 items2 中 weight = 5 ，总重量为 1 + 5 = 6 。 value = 3 的物品在 items1 中 weight = 8 ，在 items2 中 weight = 1 ，总重量为 8 + 1 = 9 。 value = 4 的物品在 items1 中 weight = 5 ，总重量为 5 。 所以，我们返回 [[1,6],[3,9],[4,5]] 。 示例 2： 输入：items1 = [[1,1],[3,2],[2,3]], items2 = [[2,1],[3,2],[1,3]] 输出：[[1,4],[2,4],[3,4]] 解释： value = 1 的物品在 items1 中 weight = 1 ，在 items2 中 weight = 3 ，总重量为 1 + 3 = 4 。 value = 2 的物品在 items1 中 weight = 3 ，在 items2 中 weight = 1 ，总重量为 3 + 1 = 4 。 value = 3 的物品在 items1 中 weight = 2 ，在 items2 中 weight = 2 ，总重量为 2 + 2 = 4 。 所以，我们返回 [[1,4],[2,4],[3,4]] 。 示例 3： 输入：items1 = [[1,3],[2,2]], items2 = [[7,1],[2,2],[1,4]] 输出：[[1,7],[2,4],[7,1]] 解释： value = 1 的物品在 items1 中 weight = 3 ，在 items2 中 weight = 4 ，总重量为 3 + 4 = 7 。 value = 2 的物品在 items1 中 weight = 2 ，在 items2 中 weight = 2 ，总重量为 2 + 2 = 4 。 value = 7 的物品在 items2 中 weight = 1 ，总重量为 1 。 所以，我们返回 [[1,7],[2,4],[7,1]] 。 提示： * 1 <= items1.length, items2.length <= 1000 * items1[i].length == items2[i].length == 2 * 1 <= valuei, weighti <= 1000 * items1 中每个 valuei 都是 唯一的 。 * items2 中每个 valuei 都是 唯一的 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表来存储每个价值对应的总重量，然后将结果按价值升序排序。

算法步骤:
1. 初始化一个哈希表 `weight_map` 来存储每个价值对应的总重量。
2. 遍历 `items1` 和 `items2`，将每个价值的重量累加到 `weight_map` 中。
3. 将 `weight_map` 转换为列表，并按价值升序排序。
4. 返回排序后的列表。

关键点:
- 使用哈希表来高效地存储和累加重量。
- 最后对结果进行排序以满足题目要求。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 items1 和 items2 的长度之和。主要的时间开销在于最后的排序操作。
空间复杂度: O(n)，用于存储哈希表中的键值对。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def merge_similar_items(items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
    """
    函数式接口 - 合并相似的物品
    """
    # 初始化哈希表
    weight_map = {}
    
    # 遍历 items1 并累加重量
    for value, weight in items1:
        if value in weight_map:
            weight_map[value] += weight
        else:
            weight_map[value] = weight
    
    # 遍历 items2 并累加重量
    for value, weight in items2:
        if value in weight_map:
            weight_map[value] += weight
        else:
            weight_map[value] = weight
    
    # 将哈希表转换为列表并按价值升序排序
    result = sorted([[value, weight] for value, weight in weight_map.items()])
    
    return result

Solution = create_solution(merge_similar_items)