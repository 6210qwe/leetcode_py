# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2863
标题: Calculator with Method Chaining
难度: easy
链接: https://leetcode.cn/problems/calculator-with-method-chaining/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2726. 使用方法链的计算器 - 设计一个类 Calculator 。该类应提供加法、减法、乘法、除法和乘方等数学运算功能。同时，它还应支持连续操作的方法链式调用。Calculator 类的构造函数应接受一个数字作为 result 的初始值。 你的 Calculator 类应包含以下方法： * add - 将给定的数字 value 与 result 相加，并返回更新后的 Calculator 对象。 * subtract - 从 result 中减去给定的数字 value ，并返回更新后的 Calculator 对象。 * multiply - 将 result 乘以给定的数字 value ，并返回更新后的 Calculator 对象。 * divide - 将 result 除以给定的数字 value ，并返回更新后的 Calculator 对象。如果传入的值为 0 ，则抛出错误 "Division by zero is not allowed" 。 * power - 计算 result 的幂，指数为给定的数字 value ，并返回更新后的 Calculator 对象。（result = result ^ value ） * getResult - 返回 result 的值。 结果与实际结果相差在 10-5 范围内的解被认为是正确的。 示例 1： 输入：actions = ["Calculator", "add", "subtract", "getResult"], values = [10, 5, 7] 输出：8 解释： new Calculator(10).add(5).subtract(7).getResult() // 10 + 5 - 7 = 8 示例 2： 输入：actions = ["Calculator", "multiply", "power", "getResult"], values = [2, 5, 2] 输出：100 解释： new Calculator(2).multiply(5).power(2).getResult() // (2 * 5) ^ 2 = 100 示例 3： 输入：actions = ["Calculator", "divide", "getResult"], values = [20, 0] 输出："Division by zero is not allowed" 解释： new Calculator(20).divide(0).getResult() // 20 / 0 由于不能除以零，因此应抛出错误。 提示： * actions 是一个有效的 JSON 字符串数组 * values 是一个有效的 JSON 字符串数组 * 2 <= actions.length <= 2 * 104 * 1 <= values.length <= 2 * 104 - 1 * actions[i] 是 "Calculator", "add", "subtract", "multiply", "divide", "power", 和 "getResult" 其中的元素 * 第一个操作总是 "Calculator" * 最后一个操作总是 "getResult"
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用类来实现计算器的功能，并通过方法链来支持连续操作。

算法步骤:
1. 初始化 Calculator 类，设置初始值 result。
2. 实现 add 方法，将给定的值加到 result 上，并返回 self。
3. 实现 subtract 方法，从 result 中减去给定的值，并返回 self。
4. 实现 multiply 方法，将 result 乘以给定的值，并返回 self。
5. 实现 divide 方法，将 result 除以给定的值（如果值为 0，则抛出异常），并返回 self。
6. 实现 power 方法，计算 result 的幂，并返回 self。
7. 实现 getResult 方法，返回 result 的值。

关键点:
- 每个方法都返回 self，以便支持方法链。
- 在 divide 方法中处理除以零的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 每个操作都是常数时间复杂度。
空间复杂度: O(1) - 只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class Calculator:
    def __init__(self, value: float):
        self.result = value

    def add(self, value: float) -> 'Calculator':
        self.result += value
        return self

    def subtract(self, value: float) -> 'Calculator':
        self.result -= value
        return self

    def multiply(self, value: float) -> 'Calculator':
        self.result *= value
        return self

    def divide(self, value: float) -> 'Calculator':
        if value == 0:
            raise ValueError("Division by zero is not allowed")
        self.result /= value
        return self

    def power(self, value: float) -> 'Calculator':
        self.result **= value
        return self

    def getResult(self) -> float:
        return self.result


def solution_function_name(actions: List[str], values: List[float]) -> Optional[float]:
    """
    函数式接口 - 根据给定的操作和值序列执行计算器操作。
    """
    if actions[0] != "Calculator":
        raise ValueError("First action must be 'Calculator'")
    if actions[-1] != "getResult":
        raise ValueError("Last action must be 'getResult'")

    calc = Calculator(values[0])
    for i in range(1, len(actions) - 1):
        action = actions[i]
        value = values[i]
        if action == "add":
            calc.add(value)
        elif action == "subtract":
            calc.subtract(value)
        elif action == "multiply":
            calc.multiply(value)
        elif action == "divide":
            try:
                calc.divide(value)
            except ValueError as e:
                return str(e)
        elif action == "power":
            calc.power(value)

    return calc.getResult()


Solution = create_solution(solution_function_name)