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
核心思想: 使用闭包来封装计数器的状态，并提供三个方法来操作这个状态。

算法步骤:
1. 定义一个内部类 `Counter`，包含三个方法 `increment`、`decrement` 和 `reset`。
2. 在 `createCounter` 函数中初始化计数器的初始值，并返回 `Counter` 类的实例。

关键点:
- 使用闭包来保持状态，避免全局变量。
- 每个方法都直接操作并返回当前计数器的值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 每个操作都是常数时间。
空间复杂度: O(1) - 只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def createCounter(init: int):
    """
    创建一个计数器对象，包含 increment, decrement 和 reset 方法。
    """
    current_value = init

    class Counter:
        def increment(self) -> int:
            nonlocal current_value
            current_value += 1
            return current_value

        def decrement(self) -> int:
            nonlocal current_value
            current_value -= 1
            return current_value

        def reset(self) -> int:
            nonlocal current_value
            current_value = init
            return current_value

    return Counter()


Solution = create_solution(createCounter)