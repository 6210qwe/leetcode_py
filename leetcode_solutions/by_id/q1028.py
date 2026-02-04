# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1028
标题: Interval List Intersections
难度: medium
链接: https://leetcode.cn/problems/interval-list-intersections/
题目类型: 数组、双指针、扫描线
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
986. 区间列表的交集 - 给定两个由一些 闭区间 组成的列表，firstList 和 secondList ，其中 firstList[i] = [starti, endi] 而 secondList[j] = [startj, endj] 。每个区间列表都是成对 不相交 的，并且 已经排序 。 返回这 两个区间列表的交集 。 形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <= b 。 两个闭区间的 交集 是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3] 。 示例 1： [https://assets.leetcode.com/uploads/2019/01/30/interval1.png] 输入：firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]] 输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]] 示例 2： 输入：firstList = [[1,3],[5,9]], secondList = [] 输出：[] 示例 3： 输入：firstList = [], secondList = [[4,8],[10,12]] 输出：[] 示例 4： 输入：firstList = [[1,7]], secondList = [[3,10]] 输出：[[3,7]] 提示： * 0 <= firstList.length, secondList.length <= 1000 * firstList.length + secondList.length >= 1 * 0 <= starti < endi <= 109 * endi < starti+1 * 0 <= startj < endj <= 109 * endj < startj+1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针遍历两个区间列表，找到交集区间。

算法步骤:
1. 初始化两个指针 i 和 j 分别指向 firstList 和 secondList 的起始位置。
2. 比较当前指针所指向的两个区间的起点和终点，找到交集区间。
3. 如果存在交集区间，将其加入结果列表。
4. 移动指针，继续比较下一个区间，直到遍历完其中一个列表。

关键点:
- 通过比较区间的起点和终点来确定交集区间。
- 使用双指针可以高效地遍历两个列表。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 和 m 分别是 firstList 和 secondList 的长度。
空间复杂度: O(1)，除了输出结果外，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    """
    函数式接口 - 找到两个区间列表的交集
    """
    i, j = 0, 0
    result = []
    
    while i < len(firstList) and j < len(secondList):
        # 找到两个区间的交集
        start_max = max(firstList[i][0], secondList[j][0])
        end_min = min(firstList[i][1], secondList[j][1])
        
        if start_max <= end_min:
            result.append([start_max, end_min])
        
        # 移动指针
        if firstList[i][1] < secondList[j][1]:
            i += 1
        else:
            j += 1
    
    return result

Solution = create_solution(intervalIntersection)