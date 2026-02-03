# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000369
标题: 无人机方阵
难度: easy
链接: https://leetcode.cn/problems/0jQkd0/
题目类型: 数组、哈希表、计数、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 39. 无人机方阵 - 在 「力扣挑战赛」 开幕式的压轴节目 「无人机方阵」中，每一架无人机展示一种灯光颜色。 无人机方阵通过两种操作进行颜色图案变换： - 调整无人机的位置布局 - 切换无人机展示的灯光颜色 给定两个大小均为 `N*M` 的二维数组 `source` 和 `target` 表示无人机方阵表演的两种颜色图案，由于无人机切换灯光颜色的耗能很大，请返回从 `source` 到 `target` 最少需要多少架无人机切换灯光颜色。 **注意：** 调整无人机的位置布局时无人机的位置可以随意变动。 **示例 1：** > 输入：`source = [[1,3],[5,4]], target = [[3,1],[6,5]]` > > 输出：`1` > > 解释： > 最佳方案为 将 `[0,1]` 处的无人机移动至 `[0,0]` 处； 将 `[0,0]` 处的无人机移动至 `[0,1]` 处； 将 `[1,0]` 处的无人机移动至 `[1,1]` 处； 将 `[1,1]` 处的无人机移动至 `[1,0]` 处，其灯光颜色切换为颜色编号为 `6` 的灯光； 因此从`source` 到 `target` 所需要的最少灯光切换次数为 1。 >![8819ccdd664e91c78cde3bba3c701986.gif](https://pic.leetcode.cn/1628823765-uCDaux-8819ccdd664e91c78cde3bba3c701986.gif){:height=300px} **示例 2：** > 输入：`source = [[1,2,3],[3,4,5]], target = [[1,3,5],[2,3,4]]` > > 输出：`0` > 解释： > 仅需调整无人机的位置布局，便可完成图案切换。因此不需要无人机切换颜色 **提示：** `n == source.length == target.length` `m == source[i].length == target[i].length` `1 <= n, m <=100` `1 <= source[i][j], target[i][j] <=10^4`
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 统计source和target中每种颜色的数量，计算差值

算法步骤:
1. 统计source中每种颜色的数量
2. 统计target中每种颜色的数量
3. 对于每种颜色，如果target中的数量大于source，则需要切换
4. 返回需要切换的总数

关键点:
- 位置可以随意调整，只需统计颜色数量
- 贪心匹配
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n*m) - 遍历矩阵
空间复杂度: O(k) - k为不同颜色的数量
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from collections import Counter
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def minimum_switching_times(source: List[List[int]], target: List[List[int]]) -> int:
    """
    函数式接口 - 无人机方阵
    
    实现思路:
    统计source和target中每种颜色的数量，计算需要切换的数量。
    
    Args:
        source: 源矩阵
        target: 目标矩阵
        
    Returns:
        最少需要切换颜色的无人机数量
        
    Example:
        >>> minimum_switching_times([[1,3],[5,4]], [[3,1],[6,5]])
        1
    """
    source_count = Counter()
    target_count = Counter()
    
    for row in source:
        for val in row:
            source_count[val] += 1
    
    for row in target:
        for val in row:
            target_count[val] += 1
    
    # 计算需要切换的数量
    switch = 0
    for color, count in target_count.items():
        if count > source_count[color]:
            switch += count - source_count[color]
    
    return switch


Solution = create_solution(minimum_switching_times)
