# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1203
标题: Print in Order
难度: easy
链接: https://leetcode.cn/problems/print-in-order/
题目类型: 多线程
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1114. 按序打印 - 给你一个类： public class Foo { public void first() { print("first"); } public void second() { print("second"); } public void third() { print("third"); } } 三个不同的线程 A、B、C 将会共用一个 Foo 实例。 * 线程 A 将会调用 first() 方法 * 线程 B 将会调用 second() 方法 * 线程 C 将会调用 third() 方法 请设计修改程序，以确保 second() 方法在 first() 方法之后被执行，third() 方法在 second() 方法之后被执行。 提示： * 尽管输入中的数字似乎暗示了顺序，但是我们并不保证线程在操作系统中的调度顺序。 * 你看到的输入格式主要是为了确保测试的全面性。 示例 1： 输入：nums = [1,2,3] 输出："firstsecondthird" 解释： 有三个线程会被异步启动。输入 [1,2,3] 表示线程 A 将会调用 first() 方法，线程 B 将会调用 second() 方法，线程 C 将会调用 third() 方法。正确的输出是 "firstsecondthird"。 示例 2： 输入：nums = [1,3,2] 输出："firstsecondthird" 解释： 输入 [1,3,2] 表示线程 A 将会调用 first() 方法，线程 B 将会调用 third() 方法，线程 C 将会调用 second() 方法。正确的输出是 "firstsecondthird"。 提示： * nums 是 [1, 2, 3] 的一组排列
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
