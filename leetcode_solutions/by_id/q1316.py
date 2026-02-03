# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1316
标题: Fizz Buzz Multithreaded
难度: medium
链接: https://leetcode.cn/problems/fizz-buzz-multithreaded/
题目类型: 多线程
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1195. 交替打印字符串 - 编写一个可以从 1 到 n 输出代表这个数字的字符串的程序，但是： * 如果这个数字可以被 3 整除，输出 "fizz"。 * 如果这个数字可以被 5 整除，输出 "buzz"。 * 如果这个数字可以同时被 3 和 5 整除，输出 "fizzbuzz"。 例如，当 n = 15，输出： 1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz。 假设有这么一个类： class FizzBuzz { public FizzBuzz(int n) { ... } // constructor public void fizz(printFizz) { ... } // only output "fizz" public void buzz(printBuzz) { ... } // only output "buzz" public void fizzbuzz(printFizzBuzz) { ... } // only output "fizzbuzz" public void number(printNumber) { ... } // only output the numbers } 请你实现一个有四个线程的多线程版 FizzBuzz， 同一个 FizzBuzz 实例会被如下四个线程使用： 1. 线程A将调用 fizz() 来判断是否能被 3 整除，如果可以，则输出 fizz。 2. 线程B将调用 buzz() 来判断是否能被 5 整除，如果可以，则输出 buzz。 3. 线程C将调用 fizzbuzz() 来判断是否同时能被 3 和 5 整除，如果可以，则输出 fizzbuzz。 4. 线程D将调用 number() 来实现输出既不能被 3 整除也不能被 5 整除的数字。 提示： * 本题已经提供了打印字符串的相关方法，如 printFizz() 等，具体方法名请参考答题模板中的注释部分。
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
