# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3729
标题: Unit Conversion I
难度: medium
链接: https://leetcode.cn/problems/unit-conversion-i/
题目类型: 深度优先搜索、广度优先搜索、图
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3528. 单位转换 I - 有 n 种单位，编号从 0 到 n - 1。给你一个二维整数数组 conversions，长度为 n - 1，其中 conversions[i] = [sourceUniti, targetUniti, conversionFactori] ，表示一个 sourceUniti 类型的单位等于 conversionFactori 个 targetUniti 类型的单位。 请你返回一个长度为 n 的数组 baseUnitConversion，其中 baseUnitConversion[i] 表示 一个 0 类型单位等于多少个 i 类型单位。由于结果可能很大，请返回每个 baseUnitConversion[i] 对 109 + 7 取模后的值。 示例 1： 输入： conversions = [[0,1,2],[1,2,3]] 输出： [1,2,6] 解释： * 使用 conversions[0]：将一个 0 类型单位转换为 2 个 1 类型单位。 * 使用 conversions[0] 和 conversions[1] 将一个 0 类型单位转换为 6 个 2 类型单位。 [https://pic.leetcode.cn/1745660099-FZhVTM-example1.png] 示例 2： 输入： conversions = [[0,1,2],[0,2,3],[1,3,4],[1,4,5],[2,5,2],[4,6,3],[5,7,4]] 输出： [1,2,3,8,10,6,30,24] 解释： * 使用 conversions[0] 将一个 0 类型单位转换为 2 个 1 类型单位。 * 使用 conversions[1] 将一个 0 类型单位转换为 3 个 2 类型单位。 * 使用 conversions[0] 和 conversions[2] 将一个 0 类型单位转换为 8 个 3 类型单位。 * 使用 conversions[0] 和 conversions[3] 将一个 0 类型单位转换为 10 个 4 类型单位。 * 使用 conversions[1] 和 conversions[4] 将一个 0 类型单位转换为 6 个 5 类型单位。 * 使用 conversions[0]、conversions[3] 和 conversions[5] 将一个 0 类型单位转换为 30 个 6 类型单位。 * 使用 conversions[1]、conversions[4] 和 conversions[6] 将一个 0 类型单位转换为 24 个 7 类型单位。 提示： * 2 <= n <= 105 * conversions.length == n - 1 * 0 <= sourceUniti, targetUniti < n * 1 <= conversionFactori <= 109 * 保证单位 0 可以通过 唯一 的转换路径（不需要反向转换）转换为任何其他单位。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来遍历单位转换图，计算每个单位相对于单位 0 的转换因子。

算法步骤:
1. 构建一个图，其中每个节点表示一个单位，边表示单位之间的转换关系和转换因子。
2. 从单位 0 开始进行 DFS，计算每个单位相对于单位 0 的转换因子。
3. 使用一个数组 `base_unit_conversion` 来存储每个单位相对于单位 0 的转换因子，并对结果取模。

关键点:
- 使用 DFS 遍历图，确保每个单位只访问一次。
- 在计算转换因子时，使用乘法并取模以防止溢出。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是单位的数量。每个单位只会被访问一次。
空间复杂度: O(n)，用于存储图和递归调用栈。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

MOD = 10**9 + 7


def unit_conversion(conversions: List[List[int]]) -> List[int]:
    """
    计算每个单位相对于单位 0 的转换因子。
    """
    n = len(conversions) + 1
    graph = [[] for _ in range(n)]
    
    # 构建图
    for src, tgt, factor in conversions:
        graph[src].append((tgt, factor))
        graph[tgt].append((src, 1 / factor))
    
    # 存储每个单位相对于单位 0 的转换因子
    base_unit_conversion = [0] * n
    base_unit_conversion[0] = 1
    
    def dfs(unit: int, parent: int, factor: float):
        for next_unit, next_factor in graph[unit]:
            if next_unit == parent:
                continue
            new_factor = factor * next_factor
            base_unit_conversion[next_unit] = int(new_factor) % MOD
            dfs(next_unit, unit, new_factor)
    
    dfs(0, -1, 1)
    return base_unit_conversion


Solution = create_solution(unit_conversion)