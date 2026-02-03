# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 937
标题: Online Stock Span
难度: medium
链接: https://leetcode.cn/problems/online-stock-span/
题目类型: 栈、设计、数据流、单调栈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
901. 股票价格跨度 - 设计一个算法收集某些股票的每日报价，并返回该股票当日价格的 跨度 。 当日股票价格的 跨度 被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。 * 例如，如果未来 7 天股票的价格是 [100,80,60,70,60,75,85]，那么股票跨度将是 [1,1,1,2,1,4,6] 。 实现 StockSpanner 类： * StockSpanner() 初始化类对象。 * int next(int price) 给出今天的股价 price ，返回该股票当日价格的 跨度 。 示例： 输入： ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"] [[], [100], [80], [60], [70], [60], [75], [85]] 输出： [null, 1, 1, 1, 2, 1, 4, 6] 解释： StockSpanner stockSpanner = new StockSpanner(); stockSpanner.next(100); // 返回 1 stockSpanner.next(80); // 返回 1 stockSpanner.next(60); // 返回 1 stockSpanner.next(70); // 返回 2 stockSpanner.next(60); // 返回 1 stockSpanner.next(75); // 返回 4 ，因为截至今天的最后 4 个股价 (包括今天的股价 75) 都小于或等于今天的股价。 stockSpanner.next(85); // 返回 6 提示： * 1 <= price <= 105 * 最多调用 next 方法 104 次
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
