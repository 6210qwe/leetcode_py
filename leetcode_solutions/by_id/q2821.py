# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2821
标题: Timeout Cancellation
难度: easy
链接: https://leetcode.cn/problems/timeout-cancellation/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2715. 执行可取消的延迟函数 - 给定一个函数 fn ，一个参数数组 args 和一个以毫秒为单位的超时时间 t ，返回一个取消函数 cancelFn 。 在 cancelTimeMs 的延迟后，返回的取消函数 cancelFn 将被调用。 setTimeout(cancelFn, cancelTimeMs) 最初，函数 fn 的执行应该延迟 t 毫秒。 如果在 t 毫秒的延迟之前调用了函数 cancelFn，它应该取消 fn 的延迟执行。否则，如果在指定的延迟 t 内没有调用 cancelFn，则应执行 fn，并使用提供的 args 作为参数。 示例 1: 输入：fn = (x) => x * 5, args = [2], t = 20 输出：[{"time": 20, "returned": 10}] 解释： const cancelTimeMs = 50; const cancelFn = cancellable((x) => x * 5, [2], 20); setTimeout(cancelFn, cancelTimeMs); 取消操作被安排在延迟了 cancelTimeMs（50毫秒）后进行，这发生在 fn(2) 在20毫秒时执行之后。 示例 2： 输入：fn = (x) => x**2, args = [2], t = 100 输出：[] 解释： const cancelTimeMs = 50; const cancelFn = cancellable((x) => x**2, [2], 100); setTimeout(cancelFn, cancelTimeMs); 取消操作被安排在延迟了 cancelTimeMs（50毫秒）后进行，这发生在 fn(2) 在100毫秒时执行之前，导致 fn(2) 从未被调用。 示例 3： 输入：fn = (x1, x2) => x1 * x2, args = [2,4], t = 30 输出：[{"time": 30, "returned": 8}] 解释： const cancelTimeMs = 100; const cancelFn = cancellable((x1, x2) => x1 * x2, [2,4], 30); setTimeout(cancelFn, cancelTimeMs); 取消操作被安排在延迟了 cancelTimeMs（100毫秒）后进行，这发生在 fn(2,4) 在30毫秒时执行之后。 提示： * fn 是一个函数 * args 是一个有效的 JSON 数组 * 1 <= args.length <= 10 * 20 <= t <= 1000 * 10 <= cancelTimeMs <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 JavaScript 的 setTimeout 和 clearTimeout 来实现延迟执行和取消。

算法步骤:
1. 定义一个内部函数 `execute`，该函数将在 t 毫秒后执行 fn 并传递 args。
2. 使用 setTimeout 设置一个定时器，在 t 毫秒后调用 `execute`。
3. 返回一个取消函数 `cancelFn`，该函数调用 clearTimeout 来取消定时器。

关键点:
- 使用闭包来保持对定时器 ID 的引用。
- 确保在调用 cancelFn 时能够正确取消定时器。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def cancellable(fn, args: List, t: int):
    """
    返回一个取消函数 cancelFn，可以在 t 毫秒内取消 fn 的延迟执行。
    """
    def execute():
        result = fn(*args)
        return {"time": t, "returned": result}

    timer_id = None

    def set_timer():
        nonlocal timer_id
        timer_id = setTimeout(execute, t)

    def cancel_fn():
        clearTimeout(timer_id)

    set_timer()
    return cancel_fn


Solution = create_solution(cancellable)