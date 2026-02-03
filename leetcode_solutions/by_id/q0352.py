# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 352
标题: Data Stream as Disjoint Intervals
难度: hard
链接: https://leetcode.cn/problems/data-stream-as-disjoint-intervals/
题目类型: 并查集、设计、哈希表、二分查找、数据流、有序集合
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
352. 将数据流变为多个不相交区间 - 给你一个由非负整数组成的数据流输入 a1, a2, ..., an，请你将目前为止看到的数字汇总为一组不相交的区间列表。 实现 SummaryRanges 类： * SummaryRanges() 初始化一个空的数据流对象。 * void addNum(int value) 将整数 value 添加到数据流中。 * int[][] getIntervals() 返回当前数据流中的整数汇总为一组不相交的区间列表 [starti, endi]。答案应按 starti 升序排序。 示例 1： 输入 ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"] [[], [1], [], [3], [], [7], [], [2], [], [6], []] 输出 [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]] 解释 SummaryRanges summaryRanges = new SummaryRanges(); summaryRanges.addNum(1); // arr = [1] summaryRanges.getIntervals(); // 返回 [[1, 1]] summaryRanges.addNum(3); // arr = [1, 3] summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3]] summaryRanges.addNum(7); // arr = [1, 3, 7] summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3], [7, 7]] summaryRanges.addNum(2); // arr = [1, 2, 3, 7] summaryRanges.getIntervals(); // 返回 [[1, 3], [7, 7]] summaryRanges.addNum(6); // arr = [1, 2, 3, 6, 7] summaryRanges.getIntervals(); // 返回 [[1, 3], [6, 7]] 提示： * 0 <= value <= 104 * 最多会调用 addNum 和 getIntervals 方法 3 * 104 次。 * 最多会调用 getIntervals 方法 102 次。 进阶：如果存在大量合并，并且与数据流的大小相比，不相交区间的数量很小，该怎么办?
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 维护按区间起点有序的不相交区间列表，插入新数时用二分或线性扫描找到相邻区间并进行合并

算法步骤:
1. 使用一个按 start 升序排列的区间列表 intervals，每个区间为 [l, r]，且两两不相交且不相邻（否则会被合并）。
2. addNum(value)：
   - 如果列表为空，直接插入 [value, value]。
   - 使用二分查找或顺序查找找到第一个区间 start > value 的位置，查看其前后区间是否与 value 相邻或包含 value。
   - 若 value 已在某个区间内，直接返回；否则根据是否与前/后区间相邻决定是扩展前区间、后区间或将前后区间与 value 一起合并。
3. getIntervals()：直接返回当前维护的区间列表的拷贝。

关键点:
- 插入时最多只会影响到相邻的前后两个区间，其余区间结构保持不变。
- 通过有序结构保证 getIntervals 输出有序且互不相交。
- 注意 value 在区间内部、两侧相邻以及完全分离三种情况的分类讨论。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: addNum 平均 O(log n) ~ O(n)（取决于使用的查找与存储结构），getIntervals 为 O(n)（返回所有区间）。
空间复杂度: O(n) - 至多维护与不同连续段数量同阶的区间个数。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def data_stream_as_disjoint_intervals(params):
    """
    函数式接口 - [待实现]
    
    实现思路:
    [待实现] 简要说明实现思路
    
    Args:
        params: [待实现] 参数说明
        
    Returns:
        [待实现] 返回值说明
        
    Example:
        >>> data_stream_as_disjoint_intervals([待实现])
        [待实现]
    """
    # TODO: 实现最优解法
    pass


# 自动生成Solution类（无需手动编写）
Solution = create_solution(data_stream_as_disjoint_intervals)
