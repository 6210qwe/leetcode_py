# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2809
标题: Create Hello World Function
难度: easy
链接: https://leetcode.cn/problems/create-hello-world-function/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2667. 创建 Hello World 函数 - 请你编写一个名为 createHelloWorld 的函数。它应该返回一个新的函数，该函数总是返回 "Hello World" 。 示例 1： 输入：args = [] 输出："Hello World" 解释： const f = createHelloWorld(); f(); // "Hello World" createHelloWorld 返回的函数应始终返回 "Hello World"。 示例 2： 输入：args = [{},null,42] 输出："Hello World" 解释： const f = createHelloWorld(); f({}, null, 42); // "Hello World" 可以传递任何参数给函数，但它应始终返回 "Hello World"。 提示： * 0 <= args.length <= 10
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 创建一个闭包函数，该闭包函数总是返回 "Hello World"。

算法步骤:
1. 定义一个外部函数 `createHelloWorld`。
2. 在 `createHelloWorld` 中定义一个内部函数 `inner_function`，该函数不接受任何参数并始终返回 "Hello World"。
3. 返回 `inner_function` 作为 `createHelloWorld` 的结果。

关键点:
- 使用闭包来确保内部函数可以访问外部函数的作用域。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 内部函数的执行时间是常数级别的。
空间复杂度: O(1) - 不需要额外的空间，只返回一个简单的字符串。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def createHelloWorld():
    """
    返回一个新的函数，该函数总是返回 "Hello World"。
    """
    def inner_function():
        return "Hello World"
    
    return inner_function


Solution = create_solution(createHelloWorld)