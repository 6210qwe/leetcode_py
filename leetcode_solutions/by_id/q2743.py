# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2743
标题: Debounce
难度: medium
链接: https://leetcode.cn/problems/debounce/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2627. 函数防抖 - 请你编写一个函数，接收参数为另一个函数和一个以毫秒为单位的时间 t ，并返回该函数的 函数防抖 后的结果。 函数防抖 方法是一个函数，它的执行被延迟了 t 毫秒，如果在这个时间窗口内再次调用它，它的执行将被取消。你编写的防抖函数也应该接收传递的参数。 例如，假设 t = 50ms ，函数分别在 30ms 、 60ms 和 100ms 时调用。前两个函数调用将被取消，第三个函数调用将在 150ms 执行。如果改为 t = 35ms ，则第一个调用将被取消，第二个调用将在 95ms 执行，第三个调用将在 135ms 执行。 Debounce Schematic [https://assets.leetcode.com/uploads/2023/04/08/screen-shot-2023-04-08-at-11048-pm.png] 上图展示了了防抖函数是如何转换事件的。其中，每个矩形表示 100ms，反弹时间为 400ms。每种颜色代表一组不同的输入。 请在不使用 lodash 的 _.debounce() 函数的前提下解决该问题。 示例 1： 输入： t = 50 calls = [ {"t": 50, inputs: [1]}, {"t": 75, inputs: [2]} ] 输出：[{"t": 125, inputs: [2]}] 解释： let start = Date.now(); function log(...inputs) { console.log([Date.now() - start, inputs ]) } const dlog = debounce(log, 50); setTimeout(() => dlog(1), 50); setTimeout(() => dlog(2), 75); 第一次调用被第二次调用取消，因为第二次调用发生在 100ms 之前 第二次调用延迟 50ms，在 125ms 执行。输入为 (2)。 示例 2： 输入： t = 20 calls = [ {"t": 50, inputs: [1]}, {"t": 100, inputs: [2]} ] 输出：[{"t": 70, inputs: [1]}, {"t": 120, inputs: [2]}] 解释： 第一次调用延迟到 70ms。输入为 (1)。 第二次调用延迟到 120ms。输入为 (2)。 示例 3： 输入： t = 150 calls = [ {"t": 50, inputs: [1, 2]}, {"t": 300, inputs: [3, 4]}, {"t": 300, inputs: [5, 6]} ] 输出：[{"t": 200, inputs: [1,2]}, {"t": 450, inputs: [5, 6]}] 解释： 第一次调用延迟了 150ms，运行时间为 200ms。输入为 (1, 2)。 第二次调用被第三次调用取消 第三次调用延迟了 150ms，运行时间为 450ms。输入为 (5, 6)。 提示： * 0 <= t <= 1000 * 1 <= calls.length <= 10 * 0 <= calls[i].t <= 1000 * 0 <= calls[i].inputs.length <= 10
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用定时器来实现防抖功能。每次调用防抖函数时，清除之前的定时器并设置新的定时器。

算法步骤:
1. 定义一个闭包函数 `debounced`，用于存储当前的定时器。
2. 在 `debounced` 函数中，清除之前的定时器（如果有）。
3. 设置一个新的定时器，在 t 毫秒后执行原函数，并传递当前的参数。
4. 返回 `debounced` 函数。

关键点:
- 使用 `setTimeout` 和 `clearTimeout` 来管理定时器。
- 确保在新的调用发生时，之前的定时器被清除。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 每次调用防抖函数的时间复杂度是常数级的。
空间复杂度: O(1) - 只需要常数级的额外空间来存储定时器。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Callable, Any, List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def debounce(fn: Callable, t: int) -> Callable:
    """
    返回一个防抖后的函数，该函数会在 t 毫秒后执行 fn 函数。
    如果在这段时间内再次调用防抖函数，则会取消之前的定时器并重新设置。
    """
    timer_id = None

    def debounced(*args: Any, **kwargs: Any) -> None:
        nonlocal timer_id
        if timer_id is not None:
            clearTimeout(timer_id)
        timer_id = setTimeout(lambda: fn(*args, **kwargs), t)

    return debounced

# 辅助函数，模拟浏览器环境中的 setTimeout 和 clearTimeout
def setTimeout(func: Callable, delay: int) -> int:
    import time
    import threading
    timer_id = threading.Timer(delay / 1000.0, func)
    timer_id.start()
    return id(timer_id)

def clearTimeout(timer_id: int) -> None:
    import threading
    for timer in threading.enumerate():
        if id(timer) == timer_id:
            timer.cancel()

Solution = create_solution(debounce)