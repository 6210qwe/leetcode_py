# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100303
标题: 数据流中的中位数
难度: hard
链接: https://leetcode.cn/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/
题目类型: 设计、双指针、数据流、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 160. 数据流中的中位数 - 中位数 是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。 例如， [2,3,4] 的中位数是 3 [2,3] 的中位数是 (2 + 3) / 2 = 2.5 设计一个支持以下两种操作的数据结构： * void addNum(int num) - 从数据流中添加一个整数到数据结构中。 * double findMedian() - 返回目前所有元素的中位数。 示例 1： 输入： ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"] [[],[1],[2],[],[3],[]] 输出：[null,null,null,1.50000,null,2.00000] 示例 2： 输入： ["MedianFinder","addNum","findMedian","addNum","findMedian"] [[],[2],[],[3],[]] 输出：[null,null,2.00000,null,2.50000] 提示： * 最多会对 addNum、findMedian 进行 50000 次调用。 注意：本题与主站 295 题相同：https://leetcode.cn/problems/find-median-from-data-stream/ [https://leetcode.cn/problems/find-median-from-data-stream/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
