# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1829
标题: Maximum Units on a Truck
难度: easy
链接: https://leetcode.cn/problems/maximum-units-on-a-truck/
题目类型: 贪心、数组、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1710. 卡车上的最大单元数 - 请你将一些箱子装在 一辆卡车 上。给你一个二维数组 boxTypes ，其中 boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi] ： * numberOfBoxesi 是类型 i 的箱子的数量。 * numberOfUnitsPerBoxi 是类型 i 每个箱子可以装载的单元数量。 整数 truckSize 表示卡车上可以装载 箱子 的 最大数量 。只要箱子数量不超过 truckSize ，你就可以选择任意箱子装到卡车上。 返回卡车可以装载 单元 的 最大 总数。 示例 1： 输入：boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4 输出：8 解释：箱子的情况如下： - 1 个第一类的箱子，里面含 3 个单元。 - 2 个第二类的箱子，每个里面含 2 个单元。 - 3 个第三类的箱子，每个里面含 1 个单元。 可以选择第一类和第二类的所有箱子，以及第三类的一个箱子。 单元总数 = (1 * 3) + (2 * 2) + (1 * 1) = 8 示例 2： 输入：boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10 输出：91 提示： * 1 <= boxTypes.length <= 1000 * 1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000 * 1 <= truckSize <= 106
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 优先选择单位数量最多的箱子，直到卡车装满或箱子用完。

算法步骤:
1. 按照每个箱子的单位数量从大到小对箱子进行排序。
2. 依次选择单位数量最多的箱子，直到卡车装满或箱子用完。
3. 计算并返回装载的最大单元总数。

关键点:
- 使用贪心算法，优先选择单位数量最多的箱子。
- 通过排序确保每次选择的箱子都是当前最优的。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 boxTypes 的长度，因为排序操作的时间复杂度是 O(n log n)。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def maximum_units(box_types: List[List[int]], truck_size: int) -> int:
    """
    函数式接口 - 计算卡车可以装载的最大单元总数
    """
    # 按照每个箱子的单位数量从大到小排序
    box_types.sort(key=lambda x: -x[1])
    
    total_units = 0
    for boxes, units_per_box in box_types:
        if truck_size <= 0:
            break
        # 选择尽可能多的当前箱子
        boxes_to_load = min(boxes, truck_size)
        total_units += boxes_to_load * units_per_box
        truck_size -= boxes_to_load
    
    return total_units


Solution = create_solution(maximum_units)