# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2789
标题: Counter II
难度: easy
链接: https://leetcode.cn/problems/counter-ii/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2665. 计数器 II - 请你写一个函数 createCounter。这个函数接收一个初始的整数值 init。并返回一个包含三个函数的对象。 这三个函数是： * increment() 将当前值加 1 并返回。 * decrement() 将当前值减 1 并返回。 * reset() 将当前值设置为 init 并返回。 示例 1： 输入：init = 5, calls = ["increment","reset","decrement"] 输出：[6,5,4] 解释： const counter = createCounter(5); counter.increment(); // 6 counter.reset(); // 5 counter.decrement(); // 4 示例 2： 输入：init = 0, calls = ["increment","increment","decrement","reset","reset"] 输出：[1,2,1,0,0] 解释： const counter = createCounter(0); counter.increment(); // 1 counter.increment(); // 2 counter.decrement(); // 1 counter.reset(); // 0 counter.reset(); // 0 提示： * -1000 <= init <= 1000 * 0 <= calls.length <= 1000 * calls[i] 是 “increment”、“decrement” 和 “reset” 中的一个
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
