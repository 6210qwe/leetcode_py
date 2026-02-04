# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2749
标题: Promise Time Limit
难度: medium
链接: https://leetcode.cn/problems/promise-time-limit/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2637. 有时间限制的 Promise 对象 - 请你编写一个函数，它接受一个异步函数 fn 和一个以毫秒为单位的时间 t。它应根据限时函数返回一个有 限时 效果的函数。函数 fn 接受提供给 限时 函数的参数。 限时 函数应遵循以下规则： * 如果 fn 在 t 毫秒的时间限制内完成，限时 函数应返回结果。 * 如果 fn 的执行超过时间限制，限时 函数应拒绝并返回字符串 "Time Limit Exceeded" 。 示例 1： 输入： fn = async (n) => { await new Promise(res => setTimeout(res, 100)); return n * n; } inputs = [5] t = 50 输出：{"rejected":"Time Limit Exceeded","time":50} 解释： const limited = timeLimit(fn, t) const start = performance.now() let result; try { const res = await limited(...inputs) result = {"resolved": res, "time": Math.floor(performance.now() - start)}; } catch (err) { result = {"rejected": err, "time": Math.floor(performance.now() - start)}; } console.log(result) // 输出结果 提供的函数设置在 100ms 后执行完成，但是设置的超时时间为 50ms，所以在 t=50ms 时拒绝因为达到了超时时间。 示例 2： 输入： fn = async (n) => { await new Promise(res => setTimeout(res, 100)); return n * n; } inputs = [5] t = 150 输出：{"resolved":25,"time":100} 解释： 在 t=100ms 时执行 5*5=25 ，没有达到超时时间。 示例 3： 输入： fn = async (a, b) => { await new Promise(res => setTimeout(res, 120)); return a + b; } inputs = [5,10] t = 150 输出：{"resolved":15,"time":120} 解释： 在 t=120ms 时执行 5+10=15，没有达到超时时间。 示例 4： 输入： fn = async () => { throw "Error"; } inputs = [] t = 1000 输出：{"rejected":"Error","time":0} 解释： 此函数始终丢出 Error 提示： * 0 <= inputs.length <= 10 * 0 <= t <= 1000 * fn 返回一个 Promise 对象
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 `Promise.race` 来实现超时控制。创建两个 Promise，一个用于执行原函数，另一个用于超时处理。

算法步骤:
1. 创建一个 Promise，用于执行原函数。
2. 创建一个超时 Promise，在指定时间后拒绝，并返回 "Time Limit Exceeded"。
3. 使用 `Promise.race` 来等待两个 Promise 中先完成的那个。

关键点:
- 使用 `Promise.race` 来实现超时控制。
- 确保超时 Promise 在指定时间后拒绝。
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

from typing import Callable, Any
import asyncio

async def time_limit(fn: Callable, t: int, *args: Any, **kwargs: Any) -> Any:
    """
    限时函数 - 如果 fn 在 t 毫秒的时间限制内完成，限时 函数应返回结果。
    如果 fn 的执行超过时间限制，限时 函数应拒绝并返回字符串 "Time Limit Exceeded"。
    """
    # 创建一个 Promise 用于执行原函数
    promise = asyncio.create_task(fn(*args, **kwargs))
    
    # 创建一个超时 Promise
    timeout_promise = asyncio.create_task(asyncio.sleep(t / 1000))
    
    # 使用 Promise.race 来等待两个 Promise 中先完成的那个
    done, pending = await asyncio.wait(
        [promise, timeout_promise],
        return_when=asyncio.FIRST_COMPLETED
    )
    
    # 取消未完成的 Promise
    for task in pending:
        task.cancel()
    
    # 检查是否是超时 Promise 完成
    if timeout_promise in done:
        raise Exception("Time Limit Exceeded")
    
    # 返回原函数的结果
    return await promise

Solution = create_solution(time_limit)