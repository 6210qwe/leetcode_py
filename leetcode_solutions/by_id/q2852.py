# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2852
标题: Customers with Maximum Number of Transactions on Consecutive Days
难度: hard
链接: https://leetcode.cn/problems/customers-with-maximum-number-of-transactions-on-consecutive-days/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2752. 在连续天数上进行了最多交易次数的顾客 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口来找到每个顾客在连续天数上的最大交易次数。

算法步骤:
1. 将输入数据按顾客ID和日期排序。
2. 使用滑动窗口遍历每个顾客的交易记录，找到每个顾客在连续天数上的最大交易次数。
3. 记录每个顾客的最大连续交易次数及其对应的起始日期。
4. 返回结果。

关键点:
- 使用滑动窗口来找到连续天数上的最大交易次数。
- 确保滑动窗口内的日期是连续的。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是交易记录的数量。排序操作的时间复杂度为 O(n log n)，滑动窗口遍历的时间复杂度为 O(n)。
空间复杂度: O(1)，除了输出结果外，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def solution_function_name(transactions: List[List[str]]) -> List[List[str]]:
    """
    函数式接口 - 找到在连续天数上进行了最多交易次数的顾客
    """
    from collections import defaultdict
    from itertools import groupby

    # 将输入数据按顾客ID和日期排序
    transactions.sort(key=lambda x: (x[0], int(x[1])))

    # 初始化变量
    max_transactions = defaultdict(lambda: [0, []])
    current_window = []

    for customer_id, group in groupby(transactions, key=lambda x: x[0]):
        group = list(group)
        start = 0
        for i in range(1, len(group)):
            if int(group[i][1]) != int(group[i-1][1]) + 1:
                # 更新当前窗口
                window_size = i - start
                if window_size > max_transactions[customer_id][0]:
                    max_transactions[customer_id] = [window_size, [group[start][1]]]
                elif window_size == max_transactions[customer_id][0]:
                    max_transactions[customer_id][1].append(group[start][1])
                start = i
        # 处理最后一个窗口
        window_size = len(group) - start
        if window_size > max_transactions[customer_id][0]:
            max_transactions[customer_id] = [window_size, [group[start][1]]]
        elif window_size == max_transactions[customer_id][0]:
            max_transactions[customer_id][1].append(group[start][1])

    # 构造结果
    result = []
    for customer_id, (max_count, dates) in max_transactions.items():
        for date in dates:
            result.append([customer_id, date, str(max_count)])

    return result

Solution = create_solution(solution_function_name)