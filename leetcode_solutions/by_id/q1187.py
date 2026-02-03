# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1187
标题: Print FooBar Alternately
难度: medium
链接: https://leetcode.cn/problems/print-foobar-alternately/
题目类型: 多线程
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1115. 交替打印 FooBar - 给你一个类： class FooBar { public void foo() { for (int i = 0; i < n; i++) { print("foo"); } } public void bar() { for (int i = 0; i < n; i++) { print("bar"); } } } 两个不同的线程将会共用一个 FooBar 实例： * 线程 A 将会调用 foo() 方法，而 * 线程 B 将会调用 bar() 方法 请设计修改程序，以确保 "foobar" 被输出 n 次。 示例 1： 输入：n = 1 输出："foobar" 解释：这里有两个线程被异步启动。其中一个调用 foo() 方法, 另一个调用 bar() 方法，"foobar" 将被输出一次。 示例 2： 输入：n = 2 输出："foobarfoobar" 解释："foobar" 将被输出两次。 提示： * 1 <= n <= 1000
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
