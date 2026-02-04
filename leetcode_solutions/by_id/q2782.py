# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2782
标题: Convert Callback Based Function to Promise Based Function
难度: medium
链接: https://leetcode.cn/problems/convert-callback-based-function-to-promise-based-function/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2782. 转换回调函数为 Promise 函数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Python 的 `concurrent.futures` 模块中的 `Future` 对象来模拟 Promise 行为。

算法步骤:
1. 定义一个 `Promise` 类，包含 `resolve` 和 `reject` 方法。
2. 在 `then` 方法中注册回调函数，并在 `Future` 对象完成时调用这些回调函数。
3. 将回调函数转换为 `Promise` 对象，并返回一个新的 `Promise` 对象。

关键点:
- 使用 `concurrent.futures.Future` 来模拟异步操作。
- 通过 `then` 方法链式调用多个回调函数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 创建和解析 Promise 对象的时间复杂度是常数级的。
空间复杂度: O(1) - 创建和解析 Promise 对象的空间复杂度是常数级的。
"""

# ============================================================================
# 代码实现
# ============================================================================

from concurrent.futures import Future
from typing import Callable, Any


class Promise:
    def __init__(self, future: Future):
        self.future = future
        self.callbacks = []

    def then(self, on_fulfilled: Callable[[Any], Any], on_rejected: Optional[Callable[[Exception], Any]] = None) -> 'Promise':
        def handle_future_result(future: Future):
            try:
                result = future.result()
                for callback in self.callbacks:
                    result = callback(result)
                if on_fulfilled:
                    result = on_fulfilled(result)
            except Exception as e:
                if on_rejected:
                    result = on_rejected(e)
                else:
                    raise e
            return result

        new_future = Future()
        self.future.add_done_callback(lambda f: new_future.set_result(handle_future_result(f)))
        return Promise(new_future)

    def resolve(self, value: Any):
        self.future.set_result(value)

    def reject(self, reason: Exception):
        self.future.set_exception(reason)


def convert_callback_to_promise(callback_function: Callable, *args, **kwargs) -> Promise:
    """
    将回调函数转换为 Promise 函数
    """
    future = Future()

    def wrapper():
        try:
            result = callback_function(*args, **kwargs)
            future.set_result(result)
        except Exception as e:
            future.set_exception(e)

    # 使用线程池执行回调函数
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor() as executor:
        executor.submit(wrapper)

    return Promise(future)


Solution = create_solution(convert_callback_to_promise)